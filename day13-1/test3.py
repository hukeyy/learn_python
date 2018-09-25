#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

def foo():
    print('1111')
    yield 1
    print('22222')
    yield 2

f = foo()
print('type f:', type(f))
print(f.__next__())
print(f.__next__())

# 执行结果：
# type f: <class 'generator'>
# 1111
# 1
# 22222
# 2









