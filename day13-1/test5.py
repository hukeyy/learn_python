#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


def foo():
    print(123)
    context = yield 1
    print('---------', context)
    print(456)
    yield 2

f = foo()
ret = f.__next__()
print(ret)
ret = f.send('hello')
print(ret)