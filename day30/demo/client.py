#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket


class FtpClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = int(port)
        self.sk = socket.socket()

    def run(self):
        self.sk.connect((self.ip, self.port))
        while True:
            cmd = input('>>>').strip()
            self.sk.send(cmd.encode())
            res = self.sk.recv(1024).decode('gbk')
            print(res)


if __name__ == '__main__':
    ftp_client = FtpClient('127.0.0.1', 8080)
    ftp_client.run()












