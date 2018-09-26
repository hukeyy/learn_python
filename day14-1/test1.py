#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# g = (x**2 for x in range(10))
# for i in g:
#     print(i)

# l = [i*i for i in range(30) if not i % 3]
# print(l)
# 例三:找到嵌套列表中名字含有两个‘e’的所有名字
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

# for name in names:
#     for i in name:
#         if i.count('e') > 1:
#             print(i)

# list_name = [i for name in names for i in name if i.count('e') > 1]
# print(list_name)

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
for k in mcase:
    dic = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)}

dic1 = {k.lower(): mcase.get(k.lower(), 0)+mcase.get(k.upper(), 0) for k in mcase}
print(dic1)










