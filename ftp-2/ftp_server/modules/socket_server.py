#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys
import socketserver
from conf import settings
from modules.auth import Auth


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        auth_info = self.request.recv(1024).decode()
        auth_type = auth_info.split(':')[0]
        auth = Auth(auth_info)
        if auth_type == 'register':
            status_code = auth.register()
            self.request.sendall(status_code.encode())
        elif auth_type == 'login':
            status_code = auth.login()[0]
            self.request.sendall(status_code.encode())
            if status_code == '200':
                pass


        
    
    

