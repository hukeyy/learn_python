# -*- coding: utf-8 -*-
# Author: hkey

# print(abs(-10))
# a = abs
# print(a(-10))

# def foo():
#     print('from foo')
#
# def test(func):
#     return func
#
# # foo 函数作为参数传入另一个函数
# t = test(foo)
# print(t)
#
# # 运行结果：
# # <function foo at 0x0000026A2A4E9048>

# import time
#
# def timmer(func):
#     start_time = time.time()
#     func()
#     print('foo函数运行时间：', time.time()-start_time)
#
#
# def foo():
#     time.sleep(2)
#     print('hello, foo.')
#
# timmer(foo)
#
# # 运行结果：
# # hello, foo.
# # foo函数运行时间： 2.0004444122314453


# def foo():
#     def test():
#         print('test.')
# name = 'hkey'
#
# def foo():
#     name = 'xiaofei'
#     def test():
#         print(locals())
#         print(name)
#     print(locals())
#     test()
# foo()
#
# # 执行结果：
# # {'test': <function foo.<locals>.test at 0x000002494DA55950>, 'name': 'hkey'}
# # {'name': 'hkey'}
# # hkey

# def foo(n):
#     def test():
#         return n + 1
#     return test
# import time
# def timmer(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         print('程序运行时间：', time.time()-start_time)
#     return wrapper
#
# @timmer
# def foo():
#     time.sleep(2)
#     print('foo run finish.')
#
# foo()
#
# # 运行结果：
# # foo run finish.
# # 程序运行时间： 2.0003890991210938

# import time
# def timmer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         print('app runtime:', time.time()-start_time)
#     return wrapper
#
# @timmer
# def foo(name):
#     time.sleep(2)
#     print('hello,', name)
#
# foo('hkey')
#
# # 运行结果：
# # hello, hkey
# # app runtime: 2.0005948543548584

import time
def timmer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print('app runtime:', time.time()-start_time)
        return res
    return wrapper

@timmer
def foo(name):
    time.sleep(2)
    print('hello,', name)
    return '返回foo'

f = foo('hkey')
print(f)

# 运行结果：
# hello, hkey
# app runtime: 2.0003833770751953
# 返回foo












