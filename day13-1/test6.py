#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# 移动平均值


def init(func):
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        next(f)
        return f
    return wrapper


@init
def foo():
    sum = 0
    count = 0
    avg = 0
    while True:
        num = yield avg
        sum += num
        count += 1
        avg = sum / count


f = foo()
ret = f.send(10)
print(ret)
ret = f.send(20)
print(ret)
ret = f.send(30)
print(ret)
ret = f.send(40)
print(ret)









