#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import shelve
import hashlib

md5 = hashlib.md5()
md5.update('hkey'.encode())
print(md5.hexdigest())

md_5 = hashlib.md5()
md_5.update('hkey'.encode())
print(md_5.hexdigest())











