#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# set1 = {'hkey', 'xiaofei', 'xixi', 'haha'}
# del set1

set1 = {1, 2, 3, 4}
set2 = {2, 3, 4, 7}

print(set1 - set2)

# 执行结果：
# {1}



# print(set1 ^ set2)  # 计算交集

# 执行结果：
# {1, 4}

# print(set1 | set2)  # 计算并集

# 执行结果：
# {1, 2, 3, 4}  # 集合中的元素是不可重复的

# set1.clear()    # 清空整个集合
# print(set1)

# 执行结果：
# set()

# set1.remove('haha') # 按照元素删除
# print(set1)

# 执行结果：
# {'hkey', 'xixi', 'xiaofei'}

# print(set1.pop())   # 随机删除集合中的元素，并返回该元素
# print(set1)

# 执行结果：
# hkey
# {'xiaofei', 'xixi', 'haha'}




# set1.update('abc')  # 将字符串 abc 分别作为三个元素插入到集合中
# print(set1)

# 执行结果：
# {'c', 'xiaofei', 'xixi', 'hkey', 'a', 'haha', 'b'}

# set1.add('vivi')
# print(set1)

# 执行结果：
# {'xiaofei', 'vivi', 'haha', 'xixi', 'hkey'}




# print(type(set1))

# 执行结果：
# <class 'set'>



