#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# print(globals() == locals())
# print(locals())
# print(globals())
#
# # 执行结果：
# # True
# # {'__cached__': None, '__doc__': None, ......}
# # {'__cached__': None, '__doc__': None, ......}

# def func():
#     name = 'jay'
#     print(locals())
#
# func()
# print(globals())
# print('name' in globals())
#
# # 执行结果：
# # {'name': 'jay'}
# # {'__file__': 'E:/learn_python/day15-1/test4.py', '__name__': '__main__', 'func': <function func at 0x0000019865D57268>}
# # False

# def func():
#     name = 'jay'
#     age = 20
#     print(locals())
#     print(globals())
#     print('name' in globals())
#
# func()
#
# # 执行结果：
# # {'age': 20, 'name': 'jay'}
# # {'func': <function func at 0x0000024665227268>, '__name__': '__main__'......}
# # False

# name = 'hkey'
#
# def func():
#     # print('局部变量 name:', name)
#     # global name # 通过 global 关键字获取全局变量 name
#     name = 'jay'    # 在局部作用域中直接定义了 name 变量，因此在局部获取 name 变量的时候，根据引用顺序，直接就从局部获取
#     print('局部变量 name: ', name)
#
# func()
# print('全局变量 name:', name)   # 全局变量未更改
#
# # 执行结果：
# # 局部变量 name:  jay
# # 全局变量 name: hkey

# def func():
#     name = 'hkey'
#     def foo():
#         nonlocal name   # 使用 nonlocal 关键字，获取外层（非全局）变量
#         name = 'jay'    # 修改外层（非全局）变量
#         print('函数foo 局部变量 name:', name)
#     return foo
#
# f = func()
# f()
#
# # 执行结果：
# # 函数foo 局部变量 name: jay


















