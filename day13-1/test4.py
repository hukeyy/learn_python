#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os


def read_file(file):
    file_size = os.stat('test.txt').st_size
    with open(file, 'rb') as f:
        while file_size > 0:
            data = f.read(50)
            file_size -= 50
            print('file_size:', file_size)
            yield '****' + data.decode('utf-8')

f = read_file('test.txt')
for line in f:
    print(line)
# print(f.__next__())
# print(f.__next__())


