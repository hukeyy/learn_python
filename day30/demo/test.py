#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import subprocess
res = 'dir'
cmd_res = subprocess.Popen(res, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# print(cmd_res.stdout.read().decode('gbk'))
# print(cmd_res.stderr.read().decode('gbk'))

print(cmd_res.stdout.read())
# print(cmd_res.stderr.read())
# x = cmd_res.stdout.read() if cmd_res.stdout.read() else cmd_res.stderr.read()
# print(x.decode('gbk'))