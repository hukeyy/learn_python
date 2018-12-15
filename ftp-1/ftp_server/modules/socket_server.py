#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socketserver
import os
from os.path import getsize, join
from modules.log import Logger
from modules.auth import Auth


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                user_info = self.request.recv(1024).decode()
                if not user_info: continue
                Logger.info('[%s:%s] 连接成功.' % self.client_address)
                auth_type = user_info.split(':')[-1]
                auth = Auth(user_info)
                if auth_type == 'register':
                    auth_code = auth.register()
                    self.request.sendall(auth_code.encode())
                    # if auth_code != '201':
                    #     continue
                elif auth_type == 'login':
                    auth_code, user_dict = auth.login()
                    self.user_home_path = user_dict['home_path']
                    self.user_current_path = user_dict['home_path']
                    self.limit_size = user_dict['limit_size']
                    self.request.sendall(auth_code.encode())
                    print('auth_code:', auth_code)
                    if auth_code != '200':
                        continue
                    while True:
                        command = self.request.recv(1024).decode()
                        print(command)
                        if not command: continue
                        command_str = command.split()[0]
                        if hasattr(self, command_str):
                            func = getattr(self, command_str)
                            func(command)
                # cmd = self.request.recv(1024).decode()
            # cmd = input('>>>')
            except ConnectionResetError as e:
                print('Error:', e)
                Logger.info('[%s:%s] 断开连接.' % self.client_address)
                break

    def dir(self, command):
        if len(command.split()) == 1:
            self.request.sendall(b'203')
            Logger.info('[%s] 执行 %s' % (self.client_address, command))
            response = self.request.recv(1024)
            send_data = os.popen('dir %s' % self.user_current_path)
            self.request.sendall(send_data.read().encode())
        else:
            self.request.sendall('403'.encode())

    def pwd(self, command):
        if len(command.split()) == 1:
            self.request.sendall(b'203')
            Logger.info('[%s] 执行 %s' % (self.client_address, command))
            response = self.request.recv(1024)
            self.request.sendall(self.user_current_path.encode())
        else:
            self.request.sendall('403'.encode())

    def mkdir(self, command):
        if len(command.split()) > 1:
            dir_name = command.split()[1]
            dir_path = os.path.join(self.user_current_path, dir_name)
            if not os.path.isdir(dir_path):
                self.request.sendall(b'202')
                response = self.request.recv(1024)
                os.makedirs(dir_path)
            else:
                self.request.sendall(b'403')
        else:
            self.request.sendall(b'404')
            # print(command, new_path)

    def cd(self, command):
        if len(command.split()) > 1:
            dir_name = command.split()[1]
            dir_path = os.path.join(self.user_current_path, dir_name)
            print('dir_path', dir_path)
            if dir_name == '..' and len(self.user_current_path) > len(self.user_home_path):
                self.request.sendall(b'202')
                response = self.request.recv(1024)
                self.user_current_path = os.path.dirname(self.user_current_path)
            elif os.path.isdir(dir_path):
                self.request.sendall(b'202')
                response = self.request.recv(1024)
                if dir_name != '.' and dir_name != '..':
                    self.user_current_path = os.path.join(self.user_current_path, dir_name)
                    print(self.user_current_path)
            else:
                Logger.error('%s 目录不存在.' % dir_path)
                self.request.sendall(b'403')

        else:
            self.request.sendall(b'404')


    def put(self, command):
        filename = command.split()[1]
        file_path = os.path.join(self.user_current_path, filename)
        self.request.sendall(b'000')
        f_size = self.request.recv(1024).decode()
        f_size = int(f_size)
        print('f_size:', f_size)
        used_size = self.__getdirsize(self.user_home_path)
        print(self.limit_size)
        print(used_size + f_size)
        if self.limit_size >= used_size + f_size:
            self.request.sendall(b'202')
            revice_size = 0
            with open(file_path, 'wb') as f:
                while revice_size != f_size:
                    data = self.request.recv(1024)
                    revice_size += len(data)
                    f.write(data)
        else:
            self.request.sendall(b'405')

    def get(self, command):
        if len(command.split()) > 1:
            filename = command.split()[1]
            file_path = os.path.join(self.user_current_path, filename)
            if os.path.isfile(file_path):
                self.request.sendall(b'200')
                file_size = os.path.getsize(file_path)
                status_code = self.request.recv(1024).decode()
                if status_code == '403':    # 客户端文件存在
                    self.request.sendall(b'000')
                    has_send_size = int(self.request.recv(1024).decode())
                    if file_size > has_send_size:
                        self.request.sendall(b'502') # 续传
                        response = self.request.recv(1024)
                    elif file_size == has_send_size:
                        self.request.sendall(b'505') # 文件一致
                else:
                    has_send_size = 0   # 客户端文件不存在

                self.request.sendall(str(file_size).encode())
                with open(file_path, 'rb') as f:
                    f.seek(has_send_size)
                    self.request.sendall(f.read())

        else:
            self.request.sendall(b'404')



















    def __getdirsize(self, home_path):
        size = 0
        for root, dirs, files in os.walk(home_path):
            size += sum([getsize(join(root, name)) for name in files])
        return size



# server = socketserver.ThreadingTCPServer((), MyServer)
# server.serve_forever()
