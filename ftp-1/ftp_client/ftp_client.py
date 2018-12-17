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

    def cd(self, command):
        self.__universal_method_none(command)

    def __universal_method_none(self, command):
        self.client.sendall(command.encode())
        status_code = self.client.recv(1024).decode()
        if status_code == '202':
            print('command right.')
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

    def put(self, command):
        if len(command) > 1:
            filename = command.split()[1]
            if os.path.isfile(filename):
                self.client.sendall(command.encode())
                reponse = self.client.recv(1024)
                print('filename:', filename)
                f_size = os.path.getsize(filename)
                print('f_size:', f_size)
                self.client.sendall(str(f_size).encode())
                status_code = self.client.recv(1024).decode()
                print(status_code)
                if status_code == '202':
                    with open(filename, 'rb') as f:
                         while True:
                            send_size = f.tell()
                            data = f.read(1024)
                            if not data:
                                break
                            self.client.sendall(data)
                            self.__progress(send_size, f_size, '上传中')
                else:
                    print('\033[31;1m空间不足.\033[0m')
                    
            else:
                print('\033[31;1m文件不存在.\033[0m')

    def get(self, command):
        self.client.sendall(command.encode())
        status_code = self.client.recv(1024).decode()
        if status_code == '200':
            filename = command.split()[1]
            if os.path.isfile(filename):
                self.client.sendall(b'403') # 本地文件存在
                response = self.client.recv(1024)
                revice_size = os.path.getsize(filename)
                self.client.sendall(str(revice_size).encode())
                status_code = self.client.recv(1024).decode()
                if status_code == '502':    # 续传
                    response = self.client.sendall(b'000')
                    print('[%s]续传' % status_code)
                elif status_code == '505':  # 文件一致
                    print('\033[32;1m服务器端和客户端文件一致.\033[0m')
                    return
            else:
                self.client.sendall(b'203') # 本地文件不存在
                revice_size = 0

            file_size = int(self.client.recv(1024).decode())
            with open(filename, 'ab') as f:
                while revice_size != file_size:
                    data = self.client.recv(1024)
                    revice_size += len(data)
                    f.write(data)
                    self.__progress(revice_size, file_size, '下载中')

        else:
            print('\033[31;1m[%s] Error!\033[0m' % status_code)

    def __progress(self, trans_size, file_size, mode):
        bar_length = 100
        percent = float(trans_size) / float(file_size)
        hashes = '=' * int(percent * bar_length)
        spaces = ' ' * int(bar_length - len(hashes))
        sys.stdout.write('\r%s:%.2fM/%.2fM %d%% [%s]'
                         %(mode, trans_size/1048576, file_size/1048576, percent*100, hashes+spaces))


if __name__ == '__main__':
    ftp_client = MyClient(('localhost', 8080))
    ftp_client.start()



