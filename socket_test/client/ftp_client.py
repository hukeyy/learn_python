#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 8080))
f_info = sk.recv(1024).decode()
f_name, f_size = f_info.split('|')
f_size = int(f_size)
sk.send(b'200')
print(f_name, f_size)
revice_size = 0
with open(f_name, 'wb') as f:
    while revice_size != f_size:
        content = sk.recv(1024)
        revice_size += len(content)
        f.write(content)


# with open(f_name, 'wb') as f:
#     while f_size:
#         if f_size >= 1024:
#             content = sk.recv(1024)
#             f.write(content)
#             f_size -= 1024
#         else:
#             content = sk.recv(f_size)
#             f.write(content)
#             break
sk.close()


