#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import shelve

f = shelve.open('user', writeback=True)
print(f['user'])
f['user'] = 'hkey'
print(f['user'])

f.close()

