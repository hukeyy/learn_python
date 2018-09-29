#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


# def is_odd(x):
#     return isinstance(x, str)
#
#
# ret = filter(is_odd, [1,2,'hello',4,'world'])
#
# # print(ret)
# #
# for i in ret:
#     print(i)


# from math import sqrt
#
# def kpf(x):
#     return sqrt(x) % 1 == 0
#
# ret = filter(kpf, range(100))
#
# for i in ret:
#     print(i)


# t1 = (('a'), ('b'))
# t2 = (('c'), ('d'))
#
# dic = lambda t1, t2: [{x: y} for x, y in zip(t1, t2)]
# print(dic(t1, t2))

# ret = zip((('a'), ('b')), (('c'), ('d')))
#
# dic = list(map(lambda dic: {dic[0]: dic[-1]}, ret))
# print(dic)

def multipliers():
    return (lambda x: i* x for i in range(4))


print([m(2) for m in multipliers()])








# print([m(2) for m in [lambda x: 0* x, lambda x: 1* x, lambda x: 2* x, lambda x: 3* x]])


# print([lambda x: 0* x, lambda x: 1* x, lambda x: 2* x, lambda x: 3* x])
