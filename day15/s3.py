# -*- coding: utf-8 -*-
# Author: hkey

# def log(func):
#
#     def wrapper(*args, **kwargs):
#         print('call %s():' % func.__name__)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @log
# def now():
#     print('2018-07-03')
#
# now()


# import time
#
# def run_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         print('app run time:', time.time() - start_time)
#         return func
#     return wrapper
#
#
# @run_time
# def test():
#     time.sleep(1)
#     print('app run finish.')
#
# test()
# import time
#
# def foo():
#     print('你好啊')
#     time.sleep(1)
#
#
# def test(func):
#     start_time = time.time()
#     func()
#     print('运行时间：', time.time() -  start_time)
#
# test(foo)

# def foo():
#     print('from the foo')
#
# def test(func):
#     return func
#
# foo = test(foo)
# foo()

# def father(name):
#     # print('from father %s' %name)
#     def son():
#         name = 'hkey_1'
#         print('我的罢罢是 %s' % name)
#     # print(locals())
#     son()
# father('hkey')

# 装饰器框架
# def timmer(func):
#     def wrapper():
#         print(func)
#         func()
#     return wrapper

import time


def timmer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print('程序运行时间是:', time.time() - start_time)
        return res
    return wrapper


@timmer
def test():
    time.sleep(2)
    print('test函数执行完毕。')
    return '这是test函数返回值'


res = test()
print(res)
