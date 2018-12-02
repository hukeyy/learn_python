#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

import socket, hashlib
md5 = hashlib.md5()
sk_server = socket.socket()
sk_server.bind(('127.0.0.1', 8080))
sk_server.listen(5)
sk_server.settimeout(30)
conn, addr = sk_server.accept()
f_info = conn.recv(1024).decode()
f_name, f_size = f_info.split('|')
f_size = int(f_size)
conn.send(b'200')
revice_size = 0
with open(f_name, 'wb') as f:
    while revice_size != f_size:
        data = conn.recv(1024)
        md5.update(data)
        revice_size += len(data)
        f.write(data)
md5_num = md5.hexdigest()
conn.send(md5_num.encode())
conn.close()
sk_server.close()

























