# -*- coding: utf-8 -*-
# Author: hkey
import time


# def timmer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = func()
#         print('程序时间：', time.time()-start_time)
#         return res
#     return wrapper
#
#
# @timmer
# def foo():
#     time.sleep(2)
#     print('foo函数运行完毕')
#     return 'return foo'
#
#
# f = foo()
# print(f)

user_list = [
    {'name': 'hkey', 'passwd': '123'},
    {'name': 'xiaofei', 'passwd': '123'},
]
for index, user_dic in enumerate(user_list):
    print(index, user_dic)