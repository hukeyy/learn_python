#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))
while True:
    info = input('>>>')
    if info == 'bye':
        sk.send(b'bye.')
        break
    sk.send(info.encode('utf-8'))
    res = sk.recv(1024).decode()
    if res == 'bye':
        break
    print(res)
sk.close()




















