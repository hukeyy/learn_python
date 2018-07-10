# -*- coding: utf-8 -*-
# Author: hkey
import time

# 时间戳
# print(time.time())

# 结构化时间
# print(time.localtime())
# print(time.gmtime())

# 字符串时间
# print(time.strftime('%Y-%m-%d %X', time.localtime()))
# print(time.strptime('2016-12-05', '%Y-%m-%d'))

import random

# 0, 1 之间的随机数
# print(random.random())

# 1, 2, 3 之间一个随机数
# print(random.randint(1, 3))

# 1, 2 之间一个随机数
# print(random.randrange(1, 3))

# 参数为一个列表，随机列表中的一个元素
# print(random.choice([[1,2], 'abc', ('superman')]))

# 接收2个参数，第一个为list， 第二个为随机取list中多少个元素
# print(random.sample([[1,2], 'abc', ('superman')], 3))

# 取1，3 之间一个实数
# print(random.uniform(1, 3))

# 将序列的所有元素随机排序
# item = [1, 3, 5, 7, 9]
# random.shuffle(item)
# print(item)

