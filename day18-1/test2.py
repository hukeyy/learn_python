#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import re

s = '+1--1+-2++1'
def wipe(s):
    res = s.replace('+-', '-').replace('++', '+').replace('--', '+').replace('-+', '-')
    return res


res = wipe(s)
num = re.findall("([+\-]?\d+\.?\d*)", res)
print(num)
k = 0
for i in num:
    k += float(i)

print(k)
