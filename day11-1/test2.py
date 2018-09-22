#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


def log1(func):
    def wrapper(*args, **kwargs):
        print('func: log1 before')
        ret = func(*args, **kwargs)
        print('func: log1 after')
        return ret
    return wrapper


def log2(func):
    def wrapper(*args, **kwargs):
        print('func: log2 before')
        ret = func(*args, **kwargs)
        print('func: log2 after')
        return ret
    return wrapper

@log1   # func = log2(func) = log2(wrapper)
@log2   # func = log2(func) = wrapper
def func(x, y):
    print('-------------')


func(1, 2)