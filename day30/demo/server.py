#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

import socket, subprocess

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen(5)
conn, addr = sk.accept()
while True:
    user_info = conn.recv(1024).decode()
    print(user_info)
    user, pwd = user_info.split(':')
    if user == 'hkey' and pwd == '123':
        conn.send('200'.encode())
        while True:
            res = conn.recv(1024).decode()
            print('res:', res)
            cmd_res = subprocess.Popen(res, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(cmd_res.stdout.read())
            print(cmd_res.stderr.read())
            # cmd_result = cmd_res.stdout.read().decode('gbk') if cmd_res.stdout.read().decode('gbk') \
            #     else cmd_res.stderr.read().decode('gbk')
            # print(cmd_result)
            # conn.send(cmd_res)
    else:
        conn.send('403'.encode())
        break

conn.close()
sk.close()

















