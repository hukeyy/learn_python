#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# 1. 没有返回值和参数的装饰器


# def log(f):
#     def wrapper():
#         print('test log:')
#         f()
#     return wrapper
#
# @log
# def func():
#     print('hello world')
#
# func()


# 2. 有参数没有返回值的装饰器


# def log(f):
#     def wrapper(*args, **kwargs):
#         print('test log:')
#         return f(*args, **kwargs)
#
#     return wrapper
#
# @log
# def func(x, y):
#     print('param:' ,x ,y)
#
# func(1, 2)


# 3. 没有参数有返回值的装饰器


# def log(f):
#     def wrapper():
#         print('test log:')
#         ret = f()
#         return ret
#     return wrapper
#
# @log
# def func():
#     return 'hello world'
#
# print(func())


# 4. 既有参数又有返回值的装饰器


# def log(func):
#     def wrapper(*args, **kwargs):
#         print('test log:')
#         return func(*args, **kwargs)
#     return wrapper
#
# @log
# def func(x, y):
#     return x, y
#
# print(func(2, 3))

# 5. 带参数的装饰器




