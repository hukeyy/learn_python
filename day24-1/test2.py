#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import shelve

shl = shelve.open('school')
# shl['上海'] = {'上海': '上海市'}
print(shl['上海'])
shl.update({'kkkk':{'kkk':'111111'}})
print(shl['kkkk'])
# shl.close()


