#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket, struct

sk_client = socket.socket()
sk_client.connect(('127.0.0.1', 8080))
while True:
    cmd = input('>>>').strip()
    if not cmd: continue
    sk_client.send(cmd.encode())
    server_f_size = sk_client.recv(4)
    data_size = struct.unpack('i', server_f_size)[0]
    revice_size = 0
    while revice_size != data_size:
        data = sk_client.recv(1024)
        revice_size += len(data)
        print(data.decode('gbk'))





