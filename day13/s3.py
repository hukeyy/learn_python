# -*- coding: utf-8 -*-
# Author: hkey

# name = 'hkey'
#
# def test1():
#     name = 'xiaofei'
#     print(name)
#
# def test2():
#     global name
#     name = 'xxxx'
#
# test1()
# test2()
# print('name:', name)

# 执行结果：
# xiaofei
# name: xxxx

# NAME = ['xiaofei', 'hkey']
#
# def test():
#     NAME = 'sky'
#     print('name:', NAME)
#
# test()
#
# # 执行结果：
# # name: sky


# NAME = ['xiaofei', 'hkey']
#
# def test():
#     NAME.append('sky')
#     print('name:', NAME)
#
# test()
#
# # 执行结果：
# # name: ['xiaofei', 'hkey', 'sky']


# NAME = ['xiaofei', 'hkey']
#
# def test():
#     # 获取全局变量 NAME
#     global NAME
#     # 打印全局变量 NAME
#     print('global NAME:', NAME)
#     # 将全局变量 NAME 修改为 'test_func'
#     NAME = 'test_func'
#     # 打印修改后的全局变量
#     print('name:', NAME)
#
# test()
#
# # 执行结果：
# # global NAME: ['xiaofei', 'hkey']
# # name: test_func

# NAME = ['xiaofei', 'hkey']
#
# def test():
#     # 获取全局变量 NAME
#     global NAME
#     # 打印全局变量 NAME
#     print(NAME)
#     # 修改全局变量为 ['sky']
#     NAME = ['sky']
#     # 追加全局变量
#     NAME.append('blue')
#     # 打印修改后的全局变量
#     print(NAME)
#
# test()
#
# # 执行结果：
# # ['sky', 'blue']



