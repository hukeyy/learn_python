#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socketserver, struct
import subprocess


class Ftp_server(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                cmd = self.request.recv(1024).decode()
                if not cmd: continue
                if hasattr(self, cmd):
                    getattr(self, cmd)()
            except ConnectionResetError as e:
                print('Error:', e)
                break


    def ipconfig(self):
        p = subprocess.Popen('ipconfig', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout = p.stdout.read()
        stderr = p.stderr.read()
        res = stdout if stdout else stderr
        s = struct.pack('i', len(res))
        self.request.send(s)
        self.request.sendall(res)


server = socketserver.ThreadingTCPServer(('127.0.0.1', 9090), Ftp_server)
server.serve_forever()






