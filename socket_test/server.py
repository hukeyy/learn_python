#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
# import socket
#
# sock = socket.socket()  # 创建 socket 对象
# sock.bind(('127.0.0.1', 8080))  # 绑定ip和port
# sock.listen(5)  # 建立监听链接
# conn, addr = sock.accept()  # 阻塞，随时准备接收客户端链接
# print(conn)
# print(addr)
# res = conn.recv(1024)   # 阻塞，等待接收客户端发送过来的数据
# print(res)
# conn.send(b'hello client.') # 向客户端发送信息
# conn.close()    # 关闭本次链接
# sock.close()    # 关闭服务器socket




import socket
udp_sk = socket.socket(type=socket.SOCK_DGRAM)  # 创建一个服务器的套接字,这里必须要定义 type=socket.SOCK_DGRAM
udp_sk.bind(('127.0.0.1', 8080))    # 绑定服务器套接字
msg, addr = udp_sk.recvfrom(1024)   # udp服务器端第一次通信必须是接收信息
print(msg)
udp_sk.sendto(b'hello, client.', addr)  # 发送信息
udp_sk.close()  # 关闭服务器套接字























