#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
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
            user_type = input('请选择：').strip()
            if not user_type: continue
            if user_type == 'register' or user_type == 'login':
                username = input('输入用户名:').strip()
                password = input('输入密码:').strip()
                auth_info = '%s:%s:%s' %(username, password, user_type)
                self.client.send(auth_info.encode())
                auth_code = self.client.recv(1024).decode()
                print('auth_code:', auth_code)
                if auth_code == '200':
                    print('\033[32;1m登录成功.\033[0m')
                    self.interactive()
                elif auth_code == '201':
                    print('\033[32;1m注册成功，请登录.\033[0m')
                elif auth_code == '401':
                    print('\033[31;1m用户名已使用，请重新注册.\033[0m')

            else:
                print('\033[31;1m输入错误，请重新输入.\033[0m')

    def interactive(self):
        while True:
            command = input('>>>').strip()
            if not command: continue
            command_str = command.split()[0]
            if hasattr(self, command_str):
                func = getattr(self, command_str)
                func(command)

    def dir(self, command):
        self.__unviersal_method_data(command)

    def pwd(self, command):
        self.__unviersal_method_data(command)

    def mkdir(self, command):
        self.__universal_method_none(command)

    def __universal_method_none(self, command):
        self.client.sendall(command.encode())
        status_code = self.client.recv(1024)
        if status_code == '202':
            self.client.sendall(b'000')
        else:
            print('[%s] Error!' % status_code)

    def __unviersal_method_data(self, command):
        self.client.sendall(command.encode())
        status_code = self.client.recv(1024).decode()
        if status_code == '203':
            self.client.sendall(b'000')
            result = self.client.recv(1024).decode()
            print(result)
        else:
            print('[%s] Error!' % status_code)



    # def __del__(self):
    #     self.client.close()


if __name__ == '__main__':
    ftp_client = MyClient(('localhost', 8080))
    ftp_client.start()



