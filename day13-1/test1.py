#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


def generator():
    yield 1
    yield 2
    print('111')
    print('222')

g = generator()
for i in g:
    print(i)






