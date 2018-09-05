#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

import hashlib


def get_file_md5(f):
    md5 = hashlib.md5()
    while True:
        data = f.read(1024)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()


def copy_file(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'ab') as f2:
        while True:
            data = f1.read(1024)
            if not data:
                break
            f2.write(data)


copy_file('rainbow.txt', 'caihong1.txt')

with open('rainbow.txt', 'rb') as f1, open('caihong1.txt', 'rb') as f2:
    f1_md5 = get_file_md5(f1)
    f2_md5 = get_file_md5(f2)
    # print('f1_md5:', f1_md5)
    # print('f2_md5:', f2_md5)
    if f1_md5 != f2_md5:
        print('\033[31;1m文件已改变.\033[0m')
    else:
        print('\033[32;1m文件一致.\033[0m')
