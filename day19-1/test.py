#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# values = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
#
# my_dict = {}
#
# for value in values:
#     if value > 60:
#         if 'k1' in my_dict:
#             my_dict['k1'].append(value)
#         else:
#             my_dict['k1'] = [value, ]
#     elif value < 60:
#         if 'k2' in my_dict:
#             my_dict['k2'].append(value)
#         else:
#             my_dict['k2'] = [value, ]
#
# print(my_dict)

from collections import defaultdict

values = [11, 22, 33,44,55,66,77,88,99,90]

my_dict = defaultdict(list) # 设置字典中，每个元素都是一个list，list的key值由下面随意定义

for value in values:
    if value > 60:
        my_dict['k1'].append(value)
    elif value < 60:
        my_dict['k2'].append(value)


print(my_dict)
print(my_dict['aaaaaaa']) # 随意定义的key值都会对应一个list

# 执行结果：
# []
# defaultdict(<class 'list'>, {'k1': [66, 77, 88, 99, 90], 'asdfadfasdf': [], 'k2': [11, 22, 33, 44, 55]})


