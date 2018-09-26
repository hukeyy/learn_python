#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


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
        PATH = yield
        for top_dir, _, files in os.walk(PATH):
            for file in files:
                target.send(os.path.join(top_dir, file))

@deco
def opener(target, pattern=None):
    while True:
        file_path = yield
        with open(file_path, encoding='utf-8') as f:
            target.send((file_path, f))


@deco
def cat(target):
    while True:
        filepath, f = yield
        for line in f:
            tag = target.send((filepath, line))

            if tag:
                break


@deco
def grep(target, pattern):
    tag = False
    while True:
        filepath, line = yield tag
        tag = False
        if pattern in line:
            target.send(filepath)
            tag = True


@deco
def printer():
    while True:
        filename = yield
        if filename:
            print(filename)


path1 = r'D:\OneDrive\python\上课笔记'
search(opener(cat(grep(printer(), 'python')))).send(path1)
