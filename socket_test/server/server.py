#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
# import socket
#
# sk_server = socket.socket()
# sk_server.bind(('127.0.0.1', 8080))
# sk_server.listen(5)
# conn, addr = sk_server.accept()
# f_info = conn.recv(1024).decode()
# file, f_size = f_info.split('|')
# f_size = int(f_size)
# conn.send(b'200')
# revice_size = 0
# with open(file, 'wb') as f:
#     while revice_size != f_size:
#         data = conn.recv(1024)
#         revice_size += len(data)
#         f.write(data)
#         print(revice_size, f_size)
# conn.close()
# sk_server.close()


import socket, json

sk_server = socket.socket()
sk_server.bind(('127.0.0.1', 8080))
sk_server.listen(5)
conn, addr = sk_server.accept()
f_json = conn.recv(1024).decode()
f_info = json.loads(f_json)
conn.send(b'200')
revice_size = 0
with open(f_info['filename'], 'wb') as f:
    while revice_size != f_info['filesize']:
        data = conn.recv(1024)
        revice_size += len(data)
        f.write(data)
        print(revice_size, f_info['filesize'])

conn.close()
sk_server.close()
























