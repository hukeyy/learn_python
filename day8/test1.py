#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

with open('test.txt', encoding='utf-8') as f, open('test1.txt', 'w', encoding='utf-8') as f1:
    data = f.read()
    print(data)
    data = data.replace('hkey', 'xiaofei')
    f1.write(data)

