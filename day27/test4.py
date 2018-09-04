#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# dict1 = {'hkey': '123'}
# def regist():
#     user = input('user:')
#     pwd = input('pwd:')
#
#     dict2 = {'hkey': '123', 'xiaofei':'123'}
#
#     if user in dict2 and pwd == dict2[user]:
#         print('ok')
#     else:
#         print('bad')

import hashlib

md5 = hashlib.md5()
md5.update(bytes('admin0.123456', encoding='utf-8'))
print(md5.hexdigest())
