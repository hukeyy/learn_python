#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socketserver, struct
import subprocess


class Ftp_server(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            cmd = self.request.recv(1024).decode()
            if not cmd: continue
            if hasattr(self, cmd):
                getattr(self, cmd)()

    def ipconfig(self):
        p = subprocess.Popen('ipconfig', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout = p.stdout.read()
        stderr = p.stderr.read()
        res = stdout if stdout else stderr
        s = struct.pack('i', len(res))
        self.request.send(s)
        self.request.sendall(res)


server = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), Ftp_server)
server.serve_forever()






