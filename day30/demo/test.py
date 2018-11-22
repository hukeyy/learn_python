#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import subprocess, os

res = 'dir'
cmd_res = subprocess.Popen(res, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout = cmd_res.stdout.read()
stderr = cmd_res.stderr.read()
res = stdout if stdout else stderr
print(res.decode('gbk'))
# print(cmd_res.stderr.read())
# x = cmd_res.stdout.read() if cmd_res.stdout.read() else cmd_res.stderr.read()
# print(cmd_res.stdout.read())
# print(cmd_res.stderr.read())
# print(cmd_res.stderr)