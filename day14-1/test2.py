#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# li = [x*x for x in range(10)]
# print(li)
#
# # 执行结果：
# # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# li = [x for x in range(10) if x % 3 == 0]
# print(li)

# 执行结果：
# [0, 3, 6, 9]

# g = (x for x in range(10) if x % 3 == 0)
#
# print(g)    # generator 这里的g就是一个生成器了，将中括号换成小括号就变成了生成器表达式
#
# for i in g:
#     print(i)
#
# # 执行结果：
# # <generator object <genexpr> at 0x00000194C9FA34C0>
# # 0
# # 3
# # 6
# # 9

# g = (x for x in range(10) if x % 3 == 0)
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#
# # 执行结果：
# # 0
# # 3
# # 6
# # 9

# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
#
# # for name in names:
# #     for i in name:
# #         if i.count('e') == 2:
# #             print(i)
#
# # 如果无法一次写出嵌套的列表生成式，可以先使用for循环写出来
# list_name = [x for name in names for x in name if x.count('e') == 2]
# print(list_name)
#
# # 执行结果：
# # ['Jefferson', 'Wesley', 'Steven', 'Jennifer']


# mcase = {'a': 10, 'b': 34}
#
# # 注意字典推导式中，返回的一定是一个字典类型：mcase[i]:i
# dic = {mcase[i]:i for i in mcase}
# print(dic)
#
# # 执行结果：
# # {10: 'a', 34: 'b'}

# mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
#
# dic = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase}
# print(dic)
#
# # 执行结果：
# # {'a': 17, 'b': 34, 'z': 3}
#
# # 这个示例中用到了 get() 这个知识点：
# #     mcase.get(k.lower(), 0) 当字典mcase中存在k.lower()的时候则直接返回，否则返回默认填写的0

# squared = {x**2 for x in [1, -1, 2]}
#
# print(squared)
#
# # 执行结果：
# # {1, 4}

# 例1:  过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母

li = ['a', 'abc', 'c', 'dddd']

l1 = [i.upper() for i in li if len(i) >= 3]
print(l1)

# 例2:  求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表

l1 = [(x, y) for x in range(1, 5) if x%2==0 for y in range(1, 5) if y%3==0]
print(l1)

# 例3:  求M中3,6,9组成的列表M = [[1,2,3],[4,5,6],[7,8,9]]

M = [[1,2,3],[4,5,6],[7,8,9]]
l1 = [i[2] for i in M]
print(l1)












