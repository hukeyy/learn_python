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
            cmd_res = subprocess.Popen(res, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            stdout = cmd_res.stdout.read()
            stderr = cmd_res.stderr.read()
            result = stdout if stdout else stderr
            conn.send(result)
    else:
        conn.send('403'.encode())
        break

conn.close()
sk.close()


class Command:
    def __init__(self, command):
        self.command = command














