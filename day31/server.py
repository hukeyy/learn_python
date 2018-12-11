#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                if not self.data: continue
                print('{} wrote:'.format(self.client_address[0]))
                print(self.data)
                self.request.sendall(self.data.upper())
            except ConnectionResetError as e:
                print(self.client_address, '已断开连接.')
                break


if __name__ == '__main__':
    HOST, PORT = '127.0.0.1', 8080
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()



