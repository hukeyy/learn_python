#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import subprocess, struct

# p = subprocess.Popen('dirr', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# stdout = p.stdout.read()
# stderr = p.stderr.read()
# res = stdout if stdout else stderr
# print(res.decode('gbk'))

s = struct.pack('i', 1234)
print(s)
print(len(s))










