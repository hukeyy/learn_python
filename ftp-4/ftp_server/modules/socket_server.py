#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os
from os.path import getsize, join
import socketserver
import subprocess
from conf import settings
from modules.auth import Auth


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                auth_info = self.request.recv(1024).decode()
                auth_type, user, pwd = auth_info.split(':')
                auth_user = Auth(user, pwd)
                if auth_type == 'register':
                    status_code = auth_user.register()
                    self.request.sendall(status_code.encode())
                elif auth_type == 'login':
                    user_dict = auth_user.login()
                    if user_dict:
                        self.request.sendall(b'200')
                        self.user_current_path = user_dict['home_path']
                        self.user_home_path = user_dict['home_path']
                        self.user_limit_size = user_dict['limit_size']
                        while True:
                            command = self.request.recv(1024).decode()
                            if not command: continue
                            command_str = command.split()[0]
                            if hasattr(self, command_str):
                                func = getattr(self, command_str)
                                func(command)
                    else:
                        self.request.sendall(b'400')
        except ConnectionResetError as e:
            print('Error:', e)

    def dir(self, command):
        if len(command.split()) == 1:
            self.request.sendall(b'201')
            response = self.request.recv(1024)
            cmd_res = subprocess.Popen('dir %s' %self.user_current_path, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, shell=True)
            stdout = cmd_res.stdout.read()
            stderr = cmd_res.stderr.read()
            result = stdout if stdout else stderr
            self.request.sendall(result)
        else:
            self.request.sendall(b'401')

    def pwd(self, command):
        if len(command.split()) == 1:
            self.request.sendall(b'201')
            response = self.request.recv(1024)
            self.request.sendall(self.user_current_path.encode())
        else:
            self.request.sendall(b'401')

    def mkdir(self, command):
        if len(command.split()) > 1:
            dir_name = command.split()[1]
            dir_path = os.path.join(self.user_current_path, dir_name)
            if not os.path.isdir(dir_path):
                self.request.sendall(b'201')
                reponse = self.request.recv(1024)
                os.makedirs(dir_path)
            else:
                self.request.sendall(b'402')

        else:
            self.request.sendall(b'401')

    def cd(self, command):
        if len(command.split()) > 1:
            dir_name = command.split()[1]
            dir_path = os.path.join(self.user_current_path, dir_name)
            if dir_name == '..' and len(self.user_current_path) > len(self.user_home_path):
                self.request.sendall(b'201')
                reponse = self.request.recv(1024)
                self.user_current_path = os.path.dirname(self.user_current_path)
            elif os.path.isdir(dir_path):
                self.request.sendall(b'201')
                reponse = self.request.recv(1024)
                if dir_name != '.' and dir_name != '..':
                    self.user_current_path = dir_path
            else:
                self.request.sendall(b'402')

        else:
            self.request.sendall(b'401')

    def put(self, command):
        filename = command.split()[1]
        file_path = os.path.join(self.user_current_path, filename)
        self.request.sendall(b'000')
        file_size = self.request.recv(1024).decode()
        file_size = int(file_size)
        used_size = self.__getdirsize(self.user_home_path)
        if self.user_limit_size > file_size + used_size:
            self.request.sendall(b'201')
            recv_size = 0
            with open(file_path, 'wb') as f:
                while recv_size != file_size:
                    data = self.request.recv(1024)
                    recv_size += len(data)
                    f.write(data)
        else:
            self.request.sendall(b'401')

    def __getdirsize(self, user_home_path):
        size = 0
        for root, dirs, files in os.walk(user_home_path):
            size += sum([getsize(join(root, name)) for name in files])
        return size
























