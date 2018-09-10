#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

s1 = 'asdfa123adfa2adfa4adfa232'
# count = 0
# for i in s1:
#     if i.isdigit():
#         count += 1
#
# print(count)
s2 = ''
for i in s1:
    if i.isalpha():
        s1 = s1.replace(i, ' ')
l = s1.split()
print(len(l))
