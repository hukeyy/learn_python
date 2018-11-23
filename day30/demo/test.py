#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import socket
import os
# print(os.getcwd())
f = 'server.py'
f_size = os.stat(f).st_size
print('%s|%s' % (f, f_size))

