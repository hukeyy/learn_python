#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


# def fib(max):
#     x, a, b = 0, 0, 1
#     while x < max:
#         print(b)
#         a, b = b, a + b
#         x += 1
#
# fib(10)

# count = 0
# def fibo(n,a=0,b=1):
#     global count
#     count += 1
#     if count < n-1:
#         return fibo(n,a=b,b=a+b)
#     elif count >= n-1:
#         return (a+b)
#
# f = fibo(2)
# print(f)


# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n -1) + fib(n -2)
#
# f = fib(50)
# print(f)

# 定义全局变量 count
count = 0

def fib(n, a=0, b=1):
    # 每次递归获取全局变量count = 0
    global count
    # 在递归函数中，count = 1
    count += 1
    # 当 1 < n -1 时，进行函数的递归计算
    if count < n-1:
        return fib(n, b, a+b)
    # 当 1 >= n -1 时，n = 2 或者 n =1 返回 a + b = 0 + 1 = 1
    elif count >= n -1:
        return a+b


f = fib(10)
print(f)





























