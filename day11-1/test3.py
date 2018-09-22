#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# def log(f):
#     def wrapper(*args, **kwargs):
#         print('func 函数运行前')
#         ret = f(*args, **kwargs)
#         print('func 函数运行后')
#         return ret
#     return wrapper

# def log(text):  # log('我是带参数的装饰器')
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print('函数之前执行')
#             print('装饰器说明：', text)
#             ret = func(*args, **kwargs) # func(x, y)
#             print('函数之后执行')
#             return ret
#         return wrapper
#     return decorator

# def log1(func): # log(wrapper2)
#     def wrapper1(*args, **kwargs):
#         print('before: log1')
#         ret = func(*args, **kwargs)
#         print('after: log1')
#         return ret
#     return wrapper1
#
# def log2(func): # log2(func)
#     def wrapper2(*args, **kwargs):
#         print('before: log2')
#         ret = func(*args, **kwargs)
#         print('after: log2')
#         return ret
#     return wrapper2
#
# @log1   # --> func = log1(func) --> log1(wrapper2) 首先执行
# @log2   # --> func = log2(func) --> wrapper2
# def func():
#     print('hello')
#
# func()
#
#
# # 执行结果：
# # before: log1
# # before: log2
# # hello
# # after: log2
# # after: log1

Flag = False  # Flag = True的时候使用装饰器中附加功能，否则不使用装饰器中的附加功能


def log(flag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if flag:  # 通过 flag 参数来控制是否要使用装饰器中的内容。
                print('----')
                ret = func(*args, **kwargs)
                print('#####')
                return ret
            else:
                ret = func(*args, **kwargs)
                return ret

        return wrapper

    return decorator


@log(Flag)
def func1():
    print('func: func1.')


@log(Flag)
def func2():
    print('func: func2.')


@log(Flag)
def func3():
    print('func: func3.')


func1()
func2()
func3()
