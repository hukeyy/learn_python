#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

s = 'wsder'

ite = iter(s)   # 转换为可迭代对象

while True:
    try:
        each = next(ite)    # 使用next循环调用，直到抓到报错退出.
    except StopIteration:
        break
    print(each)


