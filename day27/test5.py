#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import hashlib

def get_file_md5(f):
    m = hashlib.md5()
    while True:
        data = f.read(1024)
        if not data:
            break
        m.update(data)
    return m.hexdigest()

txt1 = '你好么?我可以用下面这段代码验证一下：'
txt2 = '你好么?我可以用下面这段代码验证一下：1'
with open('1.txt', 'w', encoding='utf-8') as f1, open('2.txt', 'w', encoding='utf-8') as f2:
    f1.write(txt1)
    f2.write(txt2)

with open('1.txt', 'rb') as f1, open('2.txt', 'rb') as f2:
    file1_md5 = get_file_md5(f1)
    file2_md5 = get_file_md5(f2)
    print('file1_md5:', file1_md5)
    print('file2_md5:', file2_md5)
    if file1_md5 != file2_md5:
        print('file has changed')
    else:
        print('file not changed')







