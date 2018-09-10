#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# li = ['xiaofei', 'hkey']
# li.append('zhangsan')
# print(li)

# 执行结果：
# ['xiaofei', 'hkey', 'zhangsan']

# li = ['xiaofei', 'hkey']
# li.insert(1, 'zhangsan')
# print(li)
#
# # 执行结果：
# # ['xiaofei', 'zhangsan', 'hkey']
# li = ['xiaofei', 'hkey']
# li.extend('jack')  # == for i in 'jack': li.append(i)
# print(li)
#
# # 执行结果：
# # ['xiaofei', 'hkey', 'j', 'a', 'c', 'k']

# li = ['xiaofei', 'hkey']
# name = li.pop() # 删除最后一个元素并获取到删除的元素
# print(name) # 最后一个元素是 'hkey'
# print(li)
#
# # 执行结果：
# # hkey
# # ['xiaofei']

# li = ['xiaofei', 'hkey']
#
# li.remove('xiaofei')    # 参数为指定的元素，删除指定元素。
# print(li)
#
# # 执行结果：
# # ['hkey']

# li = ['xiaofei', 'hkey']
# li.clear()
# print(li)
#
# # 执行结果：
# # []


# li = ['xiaofei', 'hkey']
# del li  # 直接删除内存中的 li 列表
#
# print(li)
#
# # 执行结果：
# # NameError: name 'li' is not defined

# li = ['xiaofei', 'hkey', 'zhangsan']
#
# del li[:2]  # 删除索引位置 2 之前的元素 [0, 1, 2]，不包括 2
# print(li)
#
# # 执行结果：
# # ['zhangsan']

# li = ['xiaofei', 'hkey', 'zhangsan']
#
# li[2] = 'jay'   # 列表的修改操作，就直接通过索引修改元素内容
# print(li)
#
# # 执行结果：
# # ['xiaofei', 'hkey', 'jay']

# li = [6, 5, 3, 1, 2, 4]
# li.sort()   # 先进行排序，然后在打印列表,正向排序
# print(li)
#
# # 执行结果：
# # [1, 2, 3, 4, 5, 6]

# li = [6, 5, 3, 1, 2, 4]
# li.sort(reverse=True)   # 先进行排序，然后在打印列表,逆向排序
# print(li)
#
# # 执行结果：
# # [6, 5, 4, 3, 2, 1]

# li = [6, 5, 3, 1, 2, 4]
# li.reverse()    # 反转排序，将元素倒过来。
# print(li)

# 执行结果：
# [4, 2, 1, 3, 5, 6]

# li = ['xiaofei', 'hkey', 'jay']
#
# print(len(li))
#
# # 执行结果：
# # 3

# li = ['xiaofei', 'hkey', 'jay', 'hkey']
# print(li.count('hkey')) # 统计同一个元素，在列表中出现几次。
#
# # 执行结果：
# # 2

# li = ['xiaofei', 'hkey', 'jay', 'hkey']

# print(li.index('hkey')) # 通过元素信息查找索引位置，默认获取第一个匹配到的元素索引

# 执行结果：
# 1

# s1 = 'a+b+c+d'
#
# li = s1.split('+')
# print(li)
#
# # 执行结果：
# # ['a', 'b', 'c', 'd']


# # 输出 3 次 hello, world
# for i in range(3):
#     print('hello, world')
#
# # 执行结果：
# # hello, world
# # hello, world
# # hello, world


# 输出 10 以内的 奇数 或者 偶数
#
# # 奇数
# print(list(range(2, 10, 2)))
#
# # 执行结果：
# # [2, 4, 6, 8]
#
#
# # 偶数
# print(list(range(1, 10, 2)))
#
# # 执行结果：
# # [1, 3, 5, 7, 9]










