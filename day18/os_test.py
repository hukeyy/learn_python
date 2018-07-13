# -*- coding: utf-8 -*-
# Author: hkey
import time
# print(time.time())
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %X', time.localtime()))


# print(time.time())
# print(time.localtime(1531433179.1281905))
# print(time.strftime('%Y-%m-%d %X' ,time.localtime(1531433179.1281905)))

# print(time.strptime('2018-07-13 06:06:19', '%Y-%m-%d %X'))
# print(time.mktime(time.strptime('2018-07-13 06:06:19', '%Y-%m-%d %X')))


# print(time.localtime())
# print(time.asctime(time.localtime()))
# print(time.ctime(time.time()))

# print(time.asctime())

# 执行结果：
# Fri Jul 13 06:30:34 2018

# print(time.ctime(time.time()))


import random

def v_code():
    '''随机生成 4 位的验证码'''
    ran_code = ''
    for i in range(4):
        ran_int = random.randint(0, 9)  # 随机获取 0-9 之间任意一个整数
        ran_alf = chr(random.randint(65, 90))   # 随机获取 65-90之间一个随机数，通过 chr 返回整数对应的 ASCII字符
        s = str(random.choice([ran_int, ran_alf]))  # 通过随机 choice 选取其中一个
        ran_code += s   # 叠加字符串
    return ran_code

print(v_code())



