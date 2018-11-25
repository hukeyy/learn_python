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

# import socket
#
# sk = socket.socket()
# sk.bind(('127.0.0.1', 8080))
# sk.listen(5)
# while True:
#     conn, addr = sk.accept()
#     while True:
#         res = conn.recv(1024).decode('utf-8')
#         if res == 'bye':
#             break
#         print(res)
#         info = input('>>>')
#         if info == 'bye':
#             conn.send(b'bye')
#             break
#         conn.send(info.encode('utf-8'))
#     conn.close()
# sk.close()



# import socket, subprocess
# sk = socket.socket()
# sk.bind(('127.0.0.1', 8080))
# sk.listen(5)
# conn, addr = sk.accept()
# while True:
#     cmd = conn.recv(1024).decode()
#     cmd_res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout = cmd_res.stdout.read()
#     stderr = cmd_res.stderr.read()
#     result = stdout if stdout else stderr
#     result_size = len(result)
#     conn.send(str(result_size).encode())
#     response = conn.recv(1024)
#     conn.sendall(result)


import socket, os, json, struct
# buffer = 1024
sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen(5)
conn, addr = sk.accept()
head = {'filename': '05 python fullstack s9day32 strcuct模块定制报头的理论.mp4',
        'filepath': 'E:\python资料\Python全栈开发9期\day32', 'filesize': None}
f_name = os.path.join(head['filepath'], head['filename'])
f_path = os.path.join(head['filepath'], f_name)
f_size = os.path.getsize(f_name)
head['filesize'] = f_size
print(head)
bytes_head = json.dumps(head).encode()
head_len = len(bytes_head)
print(head_len)
pack_len = struct.pack('i', head_len)
print('pack_len:', pack_len)
conn.send(pack_len)
conn.send(bytes_head)
has_file_size = 0
while f_size != has_file_size:
    with open(f_path, 'rb') as f:
        content = f.read(1024)
        conn.send(content)
        has_file_size += 1024

conn.close()
sk.close()








































