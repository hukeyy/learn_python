#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         a, b = b, a+b
#         n += 1
#         print(b)
#
# fab(5)


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
#             self.a, self.b = self.b, self.a+self.b
#             self.n += 1
#             return r
#         raise StopIteration()
#
#
# f = Fab(5)
# for i in f:
#     print(i)


# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         a, b = b, a+b
#         n += 1
#         yield b
#
#
# f = fab(10)
# print(next(f))
# def deco(func):
#     def wrapper(*args, **kwargs):
#         ret = func(*args, **kwargs)
#         next(ret)
#         return ret
#
#     return wrapper
#
#
# @deco
# def foo():
#     sum = 0
#     count = 0
#     avg = 0
#     while True:
#         num = yield avg
#         sum += num
#         count += 1
#         avg = sum / count
#
#
# f = foo()
# ret = f.send(10)
# print(ret)
# ret = f.send(20)
# print(ret)
# ret = f.send(30)
# print(ret)
# ret = f.send(40)
# print(ret)

import os


def deco(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        next(ret)
        return ret

    return wrapper


@deco
def search(target):
    while True:
        PATH = yield    # 接收目录
        for top_dir, _, files in os.walk(PATH):
            for file in files:
                target.send(os.path.join(top_dir, file))    # 传递目录+文件


@deco
def opener(target, pattern=None):
    while True:
        file_path = yield   # 接收 目录+文件
        with open(file_path, encoding='utf-8') as f:
            target.send((file_path, f)) # 传递 目录+文件、文件句柄

@deco
def cat(target):
    while True:
        filepath, f = yield # 接收 目录+文件、文件句柄
        for line in f:
            tag = target.send((filepath, line)) # 接收 目录+文件、行

            if tag:
                break

@deco
def grep(target, pattern):
    tag = False
    while True:
        filepath, line = yield tag  # 接收 目录+文件、行 返回
        tag = False
        if pattern in line: # 如果要查找的字符串在行中，则tag=True
            target.send(filepath)
            tag = True

@deco
def printer():
    while True:
        filename = yield
        print(filename)

PATH1 = r'D:\OneDrive\python\上课笔记'
search(opener(cat(grep(printer(), 'python')))).send(PATH1)











