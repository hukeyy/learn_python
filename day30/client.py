#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
# import socket, time


# sk = socket.socket()
# sk.connect(('127.0.0.1', 8080))
# while True:
#     res = sk.recv(1024).decode('utf-8')
#     t = float(res)
#     current_time = time.strftime('%Y%m%d %H:%M:%S', time.localtime(t))
#     print(type(res), current_time)

# sk = socket.socket()
# sk.connect(('127.0.0.1', 8080))
# while True:
#     ins = input('>>>').encode('utf-8')
#     sk.send(ins)
#     res = sk.recv(1024).decode('utf-8')
#     print(res)
#     if res == 'bye':
#         break
#
# sk.close()


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





















