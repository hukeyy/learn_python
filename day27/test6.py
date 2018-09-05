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


with open('rainbow.txt', 'rb') as f1, open('caihong1.txt', 'ab') as f2:
    while True:
        data = f1.read(1024)
        print(f1.tell())
        if not data:
            break
        f2.write(data)


with open('rainbow.txt', 'rb') as f1, open('caihong1.txt', 'rb') as f2:
    file1_md5 = get_file_md5(f1)
    file2_md5 = get_file_md5(f2)
    print('file1_md5:', file1_md5)
    print('file2_md5:', file2_md5)





