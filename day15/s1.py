# -*- coding: utf-8 -*-
# Author: hkey
import time


# def timmer(func):
#     def wrapper():
#         start_time = time.time()
#         res = func()
#         print('程序运行时间：', time.time() - start_time)
#         return res
#
#     return wrapper
#
#
# @timmer
# def test():
#     time.sleep(3)
#     print('程序运行完成！')
#     return '这是test返回值'
#
#
# t = test()
# print(t)


# def shopping_car(func):
#
#     def wrapper(*args, **kwargs):
#         username = input('-->')
#         passwd = input('-->')
#         if username == 'admin' and passwd == '123':
#             func(*args, **kwargs)
#         else:
#             print('account wrong!')
#         return func
#     return wrapper
#
#
# @shopping_car
# def index(name):
#     print('欢迎登录主页 %s' % name)
#
# @shopping_car
# def home():
#     print('个人家目录')
#
# @shopping_car
# def car():
#     print('购物车：[%s, %s]' % ('车子', '椅子'))
#
# index('abc')
# home()
# car()


















