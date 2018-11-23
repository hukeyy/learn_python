#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))
f_info = sk.recv(1024).decode()
sk.send(b'200')
f_name, f_size = f_info.split('|')
while f_size > 0:
    with open(f_name, 'a') as f:
        f_data = sk.recv(1024).decode()
        f_size -= 1024
        f.write(f_data)



