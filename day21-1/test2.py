#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


def log(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return wrapper


@log
def foo():
    print('hello foo')


foo()
