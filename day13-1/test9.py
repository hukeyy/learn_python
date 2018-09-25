#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


# class Fab(object):
#     def __init__(self, max):
#         self.n, self.a, self.b = 0, 0, 1
#         self.max = max
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n < self.max:
#             r = self.b
#             self.a, self.b = self.b, self.a + self.b
#             self.n += 1
#             return r
#         raise StopIteration()

# f = Fab(5)
# for i in f:
#     print(i)

# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         print('---------------')
#         a, b = b, a+b
#         n += 1
#
# # print(list(fab(10)))
# f = fab(10)
# print(next(f))
# print('######################')
# print(next(f))

# def foo():
#     print('123')
#     context = yield 1
#     print('-------', context)
#     yield 2
#
#
# f = foo()
# next(f)
# x = f.send('hello')
# print('x:', x)

# 移动平均值

def foo():
    '''
    sum 计算总和
    count 计算有几个数
    avg 平均数
    :yield: 返回计算出的平均数
    '''
    sum = 0
    count = 0
    avg = 0
    while True:
        num = yield avg # 接收num，返回avg
        sum += num
        count += 1
        avg = sum / count


f = foo()
next(f)
ret = f.send(10)
print(ret)
ret = f.send(20)
print(ret)
ret = f.send(30)
print(ret)
ret = f.send(40)
print(ret)

# 执行结果：
# 10.0
# 15.0
# 20.0
# 25.0



