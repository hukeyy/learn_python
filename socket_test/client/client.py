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



# import socket, os, json
#
# dic = {'filename': 'test.txt', 'filesize':None}
# dic['filesize'] = os.path.getsize(dic['filename'])
# dic_json = json.dumps(dic)
# sk_client = socket.socket()
# sk_client.connect(('127.0.0.1', 8080))
# sk_client.send(dic_json.encode())
# res_code = sk_client.recv(1024).decode()
# with open(dic['filename'], 'rb') as f:
#     while True:
#         data = f.read(1024)
#         if not data:
#             break
#         sk_client.send(data)
# sk_client.close()

import socket, hashlib
md5 = hashlib.md5()
sk_client = socket.socket()
sk_client.connect(('127.0.0.1', 8080))
cmd = input('>>>').strip()
sk_client.send(cmd.encode())
f_info = sk_client.recv(1024).decode()
sk_client.send(b'200')
f_name, f_size = f_info.split('|')
f_size = int(f_size)

revice_size = 0
with open(f_name, 'wb') as f:
    while revice_size != f_size:
        data = sk_client.recv(1024)
        md5.update(data)
        revice_size += len(data)
        print(revice_size, f_size)
        f.write(data)
sk_client.send(b'ok')
sf_md5 = sk_client.recv(1024)
if sf_md5.decode() == md5.hexdigest():
    print(sf_md5.decode(), md5.hexdigest())
    print('文件传输完成。')
sk_client.close()









































