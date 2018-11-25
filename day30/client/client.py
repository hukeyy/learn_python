#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))
f_info = sk.recv(1024).decode()
sk.send(b'200')
f_name, f_size = f_info.split('|')
if f_size.isdigit():
    f_size = int(f_size)
revice_size = 0
with open(f_name, 'ab') as f:
    while revice_size != f_size:
        data = sk.recv(1024)
        revice_size += len(data)
        f.write(data)



