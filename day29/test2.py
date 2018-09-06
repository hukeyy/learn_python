#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
# def jishu(num):
#     for i in range(num):
#         if i % 2:
#             print(i)


# print([x for x in range(100) if x % 2])
# print(list(range(1, 100, 2)))

# s = 'hskakhlkshfkskjakf'
# # print(''.join(set(s)))
# l = []
# for i in s:
#     if i not in l:
#         l.append(i)
#
# print(l)


import re
s = '123.2sdhf123.4fdg1312.123adf'
ret1 = re.findall('\d+\.\d|\d+', s)
print(ret1)


# print(ret1)
# s = 0
# for i in ret1:
#     s += float(i)
# print(s)
# res = '+'.join(ret1)
# print(res)

# print(eval(res))
# 执行结果：
l1 = ['123.2', '123.4', '1312.12', '3']
res = [float(x) for x in l1]
print('{:.2f}'.format(sum(res)))

# 执行结果：
# 1561.72

print('{:.2f}'.format(eval('123.2+123.4+1312.12+3')) )
# 执行结果：
# 1561.72



