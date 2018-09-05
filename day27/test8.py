#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import hashlib, os


def copy_file(s_file, d_file):
    '''
    文件拷贝
    :param s_file: 拷贝源文件
    :param d_file: 拷贝后的目标文件
    '''
    with open(s_file, 'rb') as f1, open(d_file, 'ab') as f2:
        while True:
            # 读取大文件的时，不能一次全部读取到内存中，每次读取1024个字节
            data = f1.read(1024)
            if not data:
                break
            f2.write(data)


def get_file_md5(f):
    '''
    传入文件句柄，返回文件内容的md5值
    :param f: 文件打开的句柄
    :return: 文件内容的md5值
    '''
    md5 = hashlib.md5()
    while True:
        # 读取大文件的时，不能一次全部读取到内存中，每次读取1024个字节
        data = f.read(1024)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()


if __name__ == '__main__':
    # 判断是否存在备份文件
    if 'rainbow_bak.txt' not in os.listdir('.'):
        copy_file('rainbow.txt', 'rainbow_bak.txt')
        with open('rainbow.txt', 'rb') as f1, open('rainbow_bak.txt', 'rb') as f2:
            file1_md5 = get_file_md5(f1)
            file2_md5 = get_file_md5(f2)
            # print(file1_md5)
            # print(file2_md5)
            # 当源文件和目标文件md5值不匹配，则备份异常；
            if file1_md5 != file2_md5:
                print('\033[31;1m文件备份异常!\033[0m')
            else:
                print('\033[32;1m文件备份完成.\033[0m')
    else:
        print('\033[33;1m文件备份已存在.\033[0m')
