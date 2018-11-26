#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
# import socket
#
# sock = socket.socket()  # 创建 socket 对象
# sock.connect(('127.0.0.1', 8080))   # 去连接服务端的socket
# sock.send(b'hello server.') # 发送信息给服务端的socket
# res = sock.recv(1024)   # 接收服务端socket发送过来的信息
# print(res)
# sock.close()    # 关闭客户端连接


import socket
ip_port = ('127.0.0.1', 8080)   # 建立ip、port元组
udp_sk = socket.socket(type=socket.SOCK_DGRAM)  # 创建一个服务器的套接字,这里必须要定义 type=socket.SOCK_DGRAM
udp_sk.sendto(b'hello server.', ip_port)    # 发送消息给服务器端，在udp中第一次交互由客户端发起
back_msg, addr = udp_sk.recvfrom(1024)  # 接收数据包括（服务器端数据，套接字信息）
print(back_msg)
udp_sk.close()  # 关闭套接字
















