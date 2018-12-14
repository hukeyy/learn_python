#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socketserver
import os
from modules.log import Logger
from conf import settings
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
                    self.request.sendall(auth_code.encode())
                    print('auth_code:', auth_code)
                    if auth_code != '200':
                        continue
                    while True:
                        print('==============================')
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

    
# server = socketserver.ThreadingTCPServer((), MyServer)
# server.serve_forever()
