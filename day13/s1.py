# -*- coding: utf-8 -*-
# Author: hkey

# set1 = {'a', 'z', 'b', 4, 6, 1}
# set1.add('x')
# print(set1)

# set1 = {'a', 'z', 'b', 4, 6, 1}
# set1.add(8)
# set1.add('hello')
# print(set1)
#
# # 执行结果：
# # {'b', 1, 'a', 4, 6, 8, 'hello', 'z'}


# set1 = {'a', 'z', 'b', 4, 6, 1}
# set1.clear()
# print(set1)
#
# # 执行结果：
# # set()

# set1 = {'a', 'z', 'b', 4, 6, 1}
# set2 =set1.copy()
# print(set2)
#
# # 执行结果：
# # {1, 'a', 4, 6, 'b', 'z'}

# set1 = {'a', 'z', 'b', 4, 6, 1}
# ys = set1.pop()
# print('set1集合：', set1)
# print('删除的元素：', ys)
#
# # 执行结果：
# # set1集合： {4, 6, 'z', 'a', 'b'}
# # 删除的元素： 1

# set1 = {'a', 'z', 'b', 4, 6, 1}
# set1.remove('a')
# print(set1)
# set1.remove('x')
# print(set1)
#
# # 执行结果：
# # {1, 4, 6, 'b', 'z'}
# # Traceback (most recent call last):
# #   File "D:/learn_python/learn_python/day13/s1.py", line 43, in <module>
# #     set1.remove('x')
# # KeyError: 'x'

# set1 = {'a', 'z', 'b', 4, 6, 1}
# set1.discard('a')
# print(set1)
# set1.discard('y')
# print(set1)
#
# # 执行结果：
# # {1, 4, 6, 'b', 'z'}
# # {1, 4, 6, 'b', 'z'}

# set1 = {'a', 'b', 'x', 'y'}
# set2 = {'i', 'j', 'b', 'a'}
#
# # 交集
# print(set1 & set2)
# print(set1.intersection(set2))
#
# # 执行结果：
# # {'a', 'b'}
# # {'a', 'b'}
#
#
# # 并集
# print(set1 | set2)
# print(set1.union(set2))
#
# # 执行结果：
# # {'y', 'j', 'a', 'b', 'x', 'i'}
# # {'y', 'j', 'a', 'b', 'x', 'i'}
#
# # 差集
# print(set1 - set2)
# print(set1.difference(set2))
# print(set2 - set1)
# print(set2.difference(set1))
#
# # 执行结果：
# # {'y', 'x'}
# # {'y', 'x'}
# # {'j', 'i'}
# # {'j', 'i'}

# set1 = {'a', 'b', 'x', 'y'}
# set2 = {'i', 'j', 'b', 'a'}
# set1.difference_update(set2)
# print(set1)
#
# # 执行结果：
# # {'y', 'x'}


# set1 = {'a', 'b', 'x', 'y'}
# set2 = {'i', 'j', 'b', 'a'}
#
# set1.intersection_update(set2)
# print(set1)
#
# # 执行结果：
# # {'b', 'a'}

# set1 = {'a', 'b', 'x', 'y'}
# set2 = {'i', 'j', 'b', 'a'}
#
# print('symmetric_difference:', set1.symmetric_difference(set2))
# print('^:', set1 ^ set2)
#
# # 执行结果：
# # symmetric_difference: {'x', 'i', 'y', 'j'}
# # ^: {'x', 'i', 'y', 'j'}

# set1 = {'a', 'b', 'x', 'y'}
# set2 = {'i', 'j', 'b', 'a'}
#
# set1.symmetric_difference_update(set2)
# print(set1)
#
# # 执行结果：
# # {'y', 'i', 'j', 'x'}

# set1 = {'a', 'b', 'x', 'y'}
#
# set1.update(('hello', 'world'))
# print(set1)
#
# # 执行结果：
# # {'hello', 'world', 'b', 'a', 'y', 'x'}

# s = frozenset('hello')
# print(s)
#
# # 执行结果：
# # frozenset({'h', 'e', 'o', 'l'})











