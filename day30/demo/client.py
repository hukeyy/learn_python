#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))
user = input('用户名:')
pwd = input('密码:')
user_info = '%s:%s' % (user, pwd)
sk.send(user_info.encode())
res = sk.recv(1024).decode()
if res == '200':
    print('\033[32;1m登录成功.\033[0m')
    while True:
        cmd = input('>>>').strip()
        sk.send(cmd.encode())

else:
    print('\033[31;1m[%s]登录失败.\033[0m' % res)

sk.close()






