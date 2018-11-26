#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket, os
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen(5)
conn, addr = sk.accept()
f_name = 's1.mp4'
f_size = os.path.getsize(f_name)
f_info = '%s|%s' % (f_name, f_size)
conn.send(f_info.encode())
response = conn.recv(1024)
with open(f_name, 'rb') as f:
    for line in f:
        conn.sendall(line)

# with open(f_name, 'rb') as f:
#     while f_size:
#         if f_size >= 1024:
#             conn.send(f.read(1024))
#             f_size -= 1024
#         else:
#             conn.send(f.read(f_size))
#             break

conn.close()
sk.close()























