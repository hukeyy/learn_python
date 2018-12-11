#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket

sk_client = socket.socket()
sk_client.connect(('127.0.0.1', 8080))
while True:
    cmd = input('>>>').strip()
    if not cmd: continue
    if cmd == 'q':
        break
    sk_client.send(cmd.encode())
    response = sk_client.recv(1024)
    print(response)


