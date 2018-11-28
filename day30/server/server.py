#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket, os
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen(5)
conn, addr = sk.accept()
file = '04 python fullstack s9day28 hashlib进阶.mp4'
f_size = os.stat(file).st_size
f_info = '%s|%s' % (file, str(f_size))
conn.send(f_info.encode())
code = conn.recv(1024)

with open(file, 'rb') as f:
    conn.sendall(f.read())


