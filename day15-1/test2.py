#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# 处理文件，用户指定要查找的文件和内容，将文件中包含要查找内容的每一行都输出到屏幕上


def file_find(file, content):
    with open(file, 'r',encoding='utf-8') as f:
        for line in f:
            if content in line:
                print(line.strip())


# file_find('test.txt', '哈哈')


# 写生成器，从文件中读取内容，在每一次读取到的内容之前加上 '***' 之后再返回给用户

def file_oper(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            yield '***'+line.strip()


f = file_oper('test.txt')
for i in f:
    print(i)
