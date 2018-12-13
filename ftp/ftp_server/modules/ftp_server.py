#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socketserver, subprocess
from modules.log import logger


class Ftp_server(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            print(self.client_address)
            logger.info('%s 连接成功.' % self.client_address[0])
            cmd = self.request.recv(1024)
            if not cmd: continue
            if hasattr(self, cmd):
                getattr(self, cmd)()

    def ls(self):
        subprocess.Popen('dir', stdout=subprocess.PIPE, stderr=subprocess.PIPE)


