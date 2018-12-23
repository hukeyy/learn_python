#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket, struct, json
import subprocess

sk_server = socket.socket()
sk_server.bind(('localhost', 8080))
sk_server.listen(5)

conn, addr = sk_server.accept()
while True:
    command = conn.recv(1024).decode()
    cmd_res = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout = cmd_res.stdout.read()
    stderr = cmd_res.stderr.read()
    result = stdout if stdout else stderr
    headers = {'res_size': len(result)} # 将head信息组合成 字典类型
    head_json = json.dumps(headers) # 转换为 json 类型
    head_json_bytes = bytes(head_json, encoding='utf-8')
    conn.send(struct.pack('i', len(head_json_bytes)))   # 首先发送 head 信息的大小
    conn.send(head_json_bytes)  # 再次发送 head 信息
    conn.send(result)   # 最后 发送 执行命令的结果集合



























