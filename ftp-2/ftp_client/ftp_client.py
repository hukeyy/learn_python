#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys
import socket


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
            if auth_type == 'register' or auth_type == 'login':
                user = input('用户名:')
                pwd = input('密码:')
                auth_info = '%s:%s:%s' %(auth_type, user, pwd)
                self.client.sendall(auth_info.encode())
                status_code = self.client.recv(1024)


            else:
                print('\033[31;1m输入错误，请重新输入.\033[0m')


























