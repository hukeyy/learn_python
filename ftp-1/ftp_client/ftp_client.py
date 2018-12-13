#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket
# import os, sys, pickle


class Myclient:
    def __init__(self, ip_port):
        self.client = socket.socket()
        self.ip_port = ip_port

    def connect(self):
        self.client.connect(self.ip_port)

    def start(self):
        self.connect()
        while True:
            print('1.注册\n2.登录\n')

            choice = input('>>>').strip()
            if choice == '1':
                # self.client.send(b'register')
                self.auth('register')
            elif choice == '2':
                # self.client.send(b'login')
                self.auth('login')
            else:
                print('\033[31;1m输入错误，请重新输入')

    def auth(self, type):
        username = input('username:').strip()
        password = input('password:').strip()
        login_info = '%s:%s:%s' % (username, password, type)
        self.client.sendall(login_info.encode())
        status_code = self.client.recv(1024).decode()
        print(status_code)
        if status_code == '400':
            print('[%s] 用户密码错误!' % status_code)
        elif status_code == '200':
            print('[%s] 登录成功！' % status_code)
            self.interactive()

    def interactive(self):
        pass

if __name__ == '__main__':
    ftp_client = Myclient(('127.0.0.1', 8080))
    ftp_client.start()



