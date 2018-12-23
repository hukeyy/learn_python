#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket, struct, json

sk_client = socket.socket()
sk_client.connect(('localhost', 8080))
while True:
    cmd = input('>>>').strip()
    if not cmd: continue
    sk_client.send(cmd.encode())
    res_size = struct.unpack('i', sk_client.recv(1024))[0]  # 首先获取 head 大小
    head_json = sk_client.recv(res_size).decode()   # 通过 head 大小获取 head 信息
    head_dict = json.loads(head_json)   # 转为 字典 类型
    data_len = head_dict['res_size']    # 取出 结果集 大小
    revice_size = 0
    while revice_size != data_len:  # 循环接收 结果集
        data = sk_client.recv(1024)
        revice_size += len(data)
        print(data.decode('gbk'))
























