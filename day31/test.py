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


# class Server:
#     def __init__(self, type):
#         self.type = type
#
#     def interactive(self):
#         if hasattr(self, self.type):
#             func = getattr(self, self.type)
#             func()
#
#     def hello(self):
#         print('hello')
#
#     def world(self):
#         print('world')
#
#
# server = Server('hello')
# print(server.interactive())


# import os
# print(os.getcwd())
# print(type(os.getcwd()))
# print(len(os.getcwd()))

# from os.path import getsize, join
#
# size = 0
# for root, dirs, files in os.walk(os.getcwd()):
#     size += sum([getsize(join(root, name)) for name in files])
filename = 'D:\svn\python\python-3.5.3-amd64.exe'

f_size = os.path.getsize(filename)
f_size1 = os.stat(filename).st_size

print(f_size)
print(f_size1)







































