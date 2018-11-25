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


# import socket
#
# sk = socket.socket()
# sk.connect(('127.0.0.1', 8080))
# while True:
#     info = input('>>>')
#     if info == 'bye':
#         sk.send(b'bye.')
#         break
#     sk.send(info.encode('utf-8'))
#     res = sk.recv(1024).decode()
#     if res == 'bye':
#         break
#     print(res)
# sk.close()

# import socket
#
# sk = socket.socket()
# sk.connect(('127.0.0.1', 8080))
# while True:
#     cmd = input('>>>').strip()
#     sk.send(cmd.encode())
#     cmd_res_size = int(sk.recv(1024).decode())
#     sk.send(b'200')
#     has_send_data = 0
#     while has_send_data != cmd_res_size:
#         result = sk.recv(1024)
#         has_send_data += len(result)
#         print(result.decode('gbk'))
import socket, struct, json
buffer = 1024
sk = socket.socket()
sk.connect(('127.0.0.1', 8080))
pack_len = sk.recv(4)
head_len = struct.unpack('i', pack_len)[0]
head_json = sk.recv(head_len).decode()
head = json.loads(head_json)
f_size = head['filesize']
with open(head['filename'], 'wb') as f:
    while f_size:
        if f_size >= buffer:
            content = sk.recv(buffer)
            f.write(content)
            f_size -= buffer
        else:
            content = sk.recv(f_size)
            f.write(content)
            break
sk.close()
























