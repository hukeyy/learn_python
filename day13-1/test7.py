#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# def demo():
#     for i in range(4):
#         yield i
#
#
# g = demo()
#
#
#
# g1 = (i for i in g)
# g2 = (i for i in g1)
# print(list(g1))
# print(list(g2))


import os

def init(func):
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        next(f)
        return f

    return wrapper


@init
def list_files(target):
    while 1:
        dir_to_search = yield
        for top_dir, dir, files in os.walk(dir_to_search):
            for file in files:
                # 取到目录下的每个文件的绝对路径
                target.send(os.path.join(top_dir, file))

# g=list_files(opener(cat(grep('python',printer()))))

@init
def opener(target):
    while 1:
        file = yield
        fn = open(file, encoding='utf-8')
        target.send((file, fn))

@init
def cat(target):
    while 1:
        file, fn = yield
        for line in fn:
            target.send((file, line))

@init
def grep(pattern, target):
    while 1:
        file, line = yield
        if pattern in line:
            target.send(file)

@init
def printer():
    while 1:
        file = yield
        if file:
            print('-----', file)

# p = printer()
# p.send('D:\OneDrive\python\上课笔记')

g=list_files(opener(cat(grep('python',printer()))))
g.send('D:\OneDrive\python\上课笔记')

