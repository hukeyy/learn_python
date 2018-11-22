#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket, time

# sk = socket.socket()
# sk.bind(('127.0.0.1', 8080))
# sk.listen(5)
# conn, addr = sk.accept()
# while True:
#     time.sleep(10)
#     t = time.time()
#     conn.send(bytes(str(t), encoding='utf-8'))

# sk = socket.socket()
# sk.bind(('127.0.0.1', 8080))
# sk.listen(5)
# conn, addr = sk.accept()
# while True:
#     res = conn.recv(1024).decode('utf-8')
#     if res == 'bye':
#         break
#     print(res)
#     ins = input('>>>').encode('utf-8')
#     conn.send(ins)
# conn.close()
# sk.close()

import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen(5)
while True:
    conn, addr = sk.accept()
    while True:
        res = conn.recv(1024).decode('utf-8')
        if res == 'bye':
            break
        print(res)
        info = input('>>>')
        if info == 'bye':
            conn.send(b'bye')
            break
        conn.send(info.encode('utf-8'))
    conn.close()
sk.close()

























