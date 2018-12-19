#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys
import socketserver
from conf import settings
from modules import auth


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                auth_info = self.request.recv(1024).decode()
                auth_type, user, pwd = auth_info.split(':')
                auth_info = auth.Auth(user, pwd)
                if auth_type == 'register':
                    status_code = auth_info.register()
                    self.request.sendall(status_code.encode())
                elif auth_type == 'login':
                    pass
            except ConnectionResetError as e:
                print('Error:', e)
                break

    def authication(self):
        pass