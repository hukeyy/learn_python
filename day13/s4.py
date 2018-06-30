# -*- coding: utf-8 -*-
# Author: hkey

# def f(x):
#     return x * x
#
#
# m = map(f, [1, 2, 3, 4])
# # iterator 是惰性序列，因此通过 list() 函数让它把整个序列都计算出来并返回一个list
# print(list(m))
#
# # 执行结果：
# # [1, 4, 9, 16]

# def is_odd(n):
#     return n % 2 == 1
#
# # f = filter(is_odd, [1,2,3,4,5,6,7])
# # 等价于
# f = filter(lambda n: n % 2 == 1, [1,2,3,4,5,6,7])
# print(list(f))
#
# # 执行结果：
# # [1, 3, 5, 7]

# from functools import reduce
# def foo(x, y):
#     return x + y
#
# # r = reduce(foo, [1,2,3,4])
# # 等价于：
# r = reduce(lambda x, y: x + y, [1,2,3,4])
# print(r)

# s = str({'a':1, 'b':2})
# m = eval(s)
# print(type(m))

# z = zip('hello', 'world')
# print(list(z))

# d1 = {'xiaofei':19, 'hkey': 20, 'xiaoA': 18}

# print(sorted(zip(d1.values(), d1.keys())))
# print(list(zip(d1.values(), d1.keys())))

























