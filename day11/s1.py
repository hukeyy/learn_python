# -*- coding: utf-8 -*-
# Author: hkey

# 将字节为数字的字符串转换为 int 类型
# a = '123'
# b = int(a)
# print(type(a), a)
# print(type(b), b)
# # 用 十六进制的方式将 num 转换为十进制
# num = '0011'
# v = int(num, base=16)
# print(v)

age = 5
# 当前数字的二进制， 至少用 r 位来表示
r = age.bit_length()
print(r)