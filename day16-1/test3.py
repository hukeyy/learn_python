#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
# n = 0
# for i in range(11):
#     n += i
#
# print(n)

# from functools import reduce
# print(reduce(lambda x, y: x+y, range(11)))

# n = 0
# for i in range(11):
#     n += i
#
# print(n)


# def my_sum(n):
#     if n == 1:
#         return n
#     return n + my_sum(n -1)
#
# res = my_sum(10)
# print(res)

def add(n):     # n = 5
    if n == 1:
        return n
    else:
        return n + add(n -1)    # 5 + add(5 -1)

def add(n):    # add(4)
    if n == 1:
        return n
    else:
        return n + add(n -1)    # 4 + add(4 -1)

def add(n):    # add(3)
    if n == 1:
        return n
    else:
        return n + add(n -1)    # 3 + add(3 -1)

def add(n):    # add(2)
    if n == 1:
        return n
    else:
        return n + add(n -1)    # 2 + add(2 -1)

def add(n):    # add(1)
    if n == 1:  # n = 1
        return n    # return 1
    else:
        return n + add(n -1)


print(add(9))

















