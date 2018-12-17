#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket
import os, sys

class MyClient:
    def __init__(self, ip_port):
        self.client = socket.socket()
        self.ip_port = ip_port
        
    def connect(self):
        self.client.connect(self.ip_port)
        
    def start(self):
        self.connect()
        while True:
            print('注册(register)\n登录(login)')
            auth_type = input('>>>').strip()
            if not auth_type: continue
            if auth_type == 'register' or auth_type == 'login':
                user = input('username:').strip()
                pwd = input('password:').strip()
                auth_info = '%s:%s:%s' %(auth_type, user, pwd)
                self.client.sendall(auth_info.encode())
                status_code = self.client.recv(1024).decode()
                if status_code == '200':    # 登录成功
                    print('\033[32;1m登录成功.\033[0m')
                    self.interactive()
                elif status_code == '201':   # 注册成功
                    print('\033[32;1m注册成功.\033[0m')
                elif status_code == '400':  # 用户名或密码错误
                    print('\033[3;1m[%s]用户名或密码错误!\03[0m' % status_code)
                elif status_code == '401':  # 用户名已存在
                    print('\033[3;1m[%s]用户名已存在!\03[0m' % status_code)
                else:
                    print('[%s] Error!' % status_code) 

    def interactive(self):
        while True:
            cmd = input('>>>').strip()
            if hasattr(self, cmd):
                func = getattr(self, cmd)
                func()



























                    
if __name__ == '__main__':
    ftp_client = MyClient(('localhost', 8080))
    ftp_client.start()

























