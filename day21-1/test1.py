#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import time


def log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print('%s 执行时间: %s' % (func.__name__, time.time() - start_time))
        return res

    return wrapper


@log
def func():
    time.sleep(1)
    print('func():')


func()
