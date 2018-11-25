#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket, os
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen(5)
conn, addr = sk.accept()
f_size = os.stat('test.txt').st_size
f_info = 'test.txt|%s' % str(f_size)
conn.send(f_info.encode())
code = conn.recv(1024)

with open('test.txt', 'rb') as f:
    conn.sendall(f.read())


