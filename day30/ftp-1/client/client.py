#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

import socket, os, hashlib

md5 = hashlib.md5()
sk_client = socket.socket()
sk_client.connect(('127.0.0.1', 8080))
f_size = os.path.getsize('test.txt')
f_info = '%s|%s' %('test.txt', f_size)
sk_client.send(f_info.encode())
response = sk_client.recv(1024)
print(response)
with open('test.txt', 'rb') as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        md5.update(data)
        sk_client.send(data)

md5_num = md5.hexdigest()
server_md5 = sk_client.recv(1024).decode()
print(server_md5)
print(md5_num)
if md5_num == server_md5:
    print('\033[32;1m文件传输完成。\033[0m')

sk_client.close()





















