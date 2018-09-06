#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
# from decimal import Decimal
#
# l1 = ['123.2', '123.4', '1312.12', '3']
#
# res = [Decimal(x) for x in l1]
# print(sum(res))
# print(type(sum(res)))
#
# # 执行结果：
# # 1561.72
# # <class 'decimal.Decimal'>
# d = {'k1':'v1', 'k2':[1,2,3], ('k', '3'):{1,2,3}}

# 输出上述字典中 values 为列表的 key
# print([x for x in d if isinstance(d[x], list)])

# 如果字典中的key是一个元组，请输出对应value值
# print([d[x] for x in d if isinstance(x, tuple)])

# d[('k', '3')] 对应的value是一个什么数据类型
# print(type(d[('k', '3')]))


def wrapper(func):
    def inner(*args, **kw):
        print('hello')
        func(*args, **kw)
    return inner

# @wrapper
# def a(arg):
#     print(arg)
# a = wrapper(a)
# a('hkey')

# with open('test.txt', 'r') as f:
#     for line in f:
#         if line.startswith('T'):
#             print(line)
# count = 0
# for x in range(1, 5):
#     for y in range(1, 5):
#         for z in range(1, 5):
#             if x == y or x == z or y == z:
#                 continue
#             count += 1
#             print(str(x)+str(y)+str(z))
























