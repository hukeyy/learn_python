#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os
import socket
import subprocess


class FtpServer:
    current_path = os.getcwd()

    def __init__(self, ip, port):
        self.ip = ip
        self.port = int(port)
        self.sk = socket.socket()

    def run(self):
        self.sk.bind((self.ip, self.port))
        self.sk.listen(5)
        self.conn, self.addr = self.sk.accept()
        while True:
            cmd = self.conn.recv(1024).decode()
            if not cmd: continue
            if len(cmd.split()) == 1:
                if hasattr(self, cmd):
                    getattr(self, cmd)()
                else:
                    self.conn.send('\033[31;1m-bash: command not found!\033[0m'.encode())
            elif len(cmd.split()) == 2:
                cmd, file = cmd.split()
                if cmd.startswith('get') or cmd.startswith('put') or cmd.startswith('cd'):
                    if hasattr(self, cmd):
                        getattr(self, cmd)(file)
            else:
                self.conn.send('\033[31;1m-bash: command not found!\033[0m'.encode())

    def ls(self):
        cmd_exec = subprocess.Popen('dir %s' % FtpServer.current_path, shell=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = cmd_exec.stdout.read()
        stderr = cmd_exec.stderr.read()
        cmd_res = stdout if stdout else stderr
        self.conn.send(cmd_res)

    def cd(self, dir):
        if os.path.exists(os.path.join(FtpServer.current_path, dir)):
            FtpServer.current_path = os.path.join(FtpServer.current_path, dir)
            self.conn.send(b'200')
        else:
            self.conn.send(('\033[31;1m-bash: cd: %s: No such file or directory\033[0m'
                            % FtpServer.current_path).encode())

    def get(self, file):
        pass









    def __del__(self):
        self.conn.close()
        self.sk.close()


if __name__ == '__main__':
    ftp_server = FtpServer('127.0.0.1', 8080)
    ftp_server.run()














