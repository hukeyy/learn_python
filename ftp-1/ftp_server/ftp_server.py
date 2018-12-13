#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socketserver, sys
from conf import settings
from modules.auth import Auth


class Ftp_server(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            user, pwd, auth_type = self.request.recv(1024).decode().split(':')
            auth = Auth(user, pwd)
            if auth_type == 'register':
                auth_code = auth.register()
            elif auth_type == 'login':
                auth_code = auth.login()
            self.request.sendall(auth_code.encode())


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(settings.IP_PORT, Ftp_server)
    server.serve_forever()










