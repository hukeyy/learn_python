#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import subprocess, struct, logging, sys

# p = subprocess.Popen('dirr', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# stdout = p.stdout.read()
# stderr = p.stderr.read()
# res = stdout if stdout else stderr
# print(res.decode('gbk'))

# s = struct.pack('i', 1234)
# print(s)
# print(len(s))

# print(sys.argv[0].split('/')[-1].split('.')[0] + '.log')

# with open('user.txt', 'r') as f:
#     user_list = f.read()
#
# print(user_list.split('\n')[:-1])

import os

# os.makedirs('test/a/b/c')


class Server:
    def __init__(self, type):
        self.type = type

    def interactive(self):
        if hasattr(self, self.type):
            func = getattr(self, self.type)
            func()

    def hello(self):
        print('hello')

    def world(self):
        print('world')


server = Server('hello')
print(server.interactive())


