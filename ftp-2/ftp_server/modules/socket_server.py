#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys
import socketserver
from modules.auth import Auth


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                auth_info = self.request.recv(1024).decode()
                auth_type = auth_info.split(':')[0]
                auth = Auth(auth_info)
                if auth_type == 'register': # 注册
                    status_code = auth.register()
                elif auth_type == 'login':  # 登录
                    status_code = auth.login()
                self.request.sendall(status_code.encode())
            except ConnectionResetError as e:
                print('Error:', e)
                break


























