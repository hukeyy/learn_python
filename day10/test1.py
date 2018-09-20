#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# def my_max(x, y):
#     m = x if x > y else y
#     return m
#
# bigger = my_max(10, 20)
# print(bigger)

# print(globals())
# print(locals())
#
# print(globals() == locals())
#
# # 执行结果：
# # ......
# # True

# def func():
#     a = 1
#     print(globals())
#     print(locals())
#
# func()


# a = 10
#
# def func():
#     global a    # 获取全局空间中的变量
#     a = 20      # 修改变量a
#
# print(a)    # 打印全局变量中的a
# func()
# print(a)    # 打印修改后的变量a

# def f1():
#     print('in f1')
#     def f2():
#         print('in f2')
#     f2()
#
# f1()

# 执行结果：
# in f1
# in f2

# def f1():
#     def f2():
#         def f3():
#             print('in f3')
#         print('in f2')
#         f3()
#
#     print('in f1')
#     f2()
#
# f1()
#
# # 执行结果：
# # in f1
# # in f2
# # in f3

# def f1():
#     a = 1
#     def f2():
#         print(a)
#
#     f2()
#
# f1()


# def f1():
#     a = 1
#     def f2():
#         def f3():
#             print(a)
#
#         f3()
#     f2()
#
# f1()
#
# # 执行结果：
# # 1
# def f1():
#     a = 1
#     def f2():
#         a = 2
#     f2()
#     print('a in f1 : ',a)
#
# f1()
#
# # 执行结果：
# # a in f1 :  1

# def f1():
#     a = 1
#     def f2():
#         nonlocal a
#         a = 2
#
#     f2()
#     print('a in f1:', a)
#
# f1()
#
# # 运行结果：
# # a in f1: 2

# def func():
#     print('hello world')
#
# f = func
# f()
#
# # 执行结果：
# # hello world

# def f1():
#     print('func: f1')
#
# def f2():
#     print('func: f2')
#
# def f3():
#     print('func: f3')
#
# l = [f1, f2, f3]
#
# for i in l:
#     i()
#
# # 执行结果：
# # func: f1
# # func: f2
# # func: f3

# def f():
#     print('func: f')
#
# def func(f):
#     print('func: func')
#     return f
#
# c = func(f)
# c()
#
# # 执行结果：
# # func: func
# # func: f

# def func():
#     name = 'xiaofei'
#     def inner():
#         print(name)
#     return inner
#
# f = func()
# f()
#
# # 执行结果：
# # xiaofei

# def calc_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
#
#
# c = calc_sum(1,2,3)
# print(c)

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs
#
#
# f1, f2, f3 = count()
#
# print(f1())
# print(f2())
# print(f3())

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
#
# f1, f2, f3 = count()
#
# print(f1())
# print(f2())
# print(f3())

def createCounter():
    n = 0
    def counter():
        nonlocal n
        n += 1
        return n
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')



