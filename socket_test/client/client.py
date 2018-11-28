#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
# import socket, os
# file = '04 python fullstack s9day28 hashlib进阶.mp4'
# f_size = os.path.getsize(file)
# f_info = '%s|%s' %(file, str(f_size))
#
# sk_client = socket.socket()
# sk_client.connect(('127.0.0.1', 8080))
# sk_client.send(f_info.encode())
# res_code = sk_client.recv(1024)
#
# with open(file, 'rb') as f:
#     while True:
#         filedata = f.read(1024)
#         if not filedata:
#             break
#         sk_client.send(filedata)
#     # sk_client.sendall(f.read())
#
# sk_client.close()



import socket, os, json

dic = {'filename': 'test.txt', 'filesize':None}
dic['filesize'] = os.path.getsize(dic['filename'])
dic_json = json.dumps(dic)
sk_client = socket.socket()
sk_client.connect(('127.0.0.1', 8080))
sk_client.send(dic_json.encode())
res_code = sk_client.recv(1024).decode()
with open(dic['filename'], 'rb') as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        sk_client.send(data)
sk_client.close()






















