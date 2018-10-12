#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

import re


# s1 = 'runnicegoodrunbetterrun'
# # rr = re.match('run', 'nicegoodrun better.run')
# r1 = re.match('run', 'runnicegoodrunbetterrun').group()
# r2 = re.match('run', 'Runnicegoodrunbetterrun', re.I).group()   # re.I 忽视大小写
#
# print('r1:', r1)
# print('r2:', r2)
#
# # 执行结果：
# # r1: run
# # r2: Run

# s1 = 'run nice good run better rungood'
# rr = re.search("good", s1).group()
# print(rr)
#
# # 执行结果：
# # good


# import re
# a = "123abc456"
# rr = re.compile("([0-9]*)([a-z]*)([0-9]*)")
# print('group(0):', rr.search(a).group(0))
# print('group(1):', rr.search(a).group(1))
# print('group(2):', rr.search(a).group(2))
# print('group(3):', rr.search(a).group(3))
# print('groups():', rr.search(a).groups())
#
# # 执行结果：
# # group(0): 123abc456
# # group(1): 123
# # group(2): abc
# # group(3): 456
# # groups(): ('123', 'abc', '456')

# import re
#
# p = re.findall("(\d+)", 'asdf12sdf123ad')   # 当匹配到多个值，以列表的形式返回
# print(p)
#
# # 执行结果：
# # ['12', '123']

# import re
#
# tt = 'ggood booyy nice day'
# print(re.findall("\w*oo\w*", tt))
# print(re.findall("(\w)*oo(\w)", tt))    # 通过小括号分组，得到列表中的元组
#
# # 执行结果：
# # ['ggood', 'booyy']
# # [('g', 'd'), ('b', 'y')]


# import re
#
# iter = re.finditer('\d+', 'adfasdfq2313sdasf2qe4123')
# for i in iter:
#     print(i)    # finditer返回的是一个迭代器
#     print(i.group())    # 返回一组匹配到的部分
#     print(i.span())     # 返回一个元组包含匹配（开始，结束）的位置
#
# # 执行结果：
# # <_sre.SRE_Match object; span=(8, 12), match='2313'>
# # 2313
# # (8, 12)
# # <_sre.SRE_Match object; span=(17, 18), match='2'>
# # 2
# # (17, 18)
# # <_sre.SRE_Match object; span=(20, 24), match='4123'>
# # 4123
# # (20, 24)

# import re
# print(re.split('[a-z]','111a222'))
# print(re.split('([a-z])','111a222a333'))
#
# # 执行结果：
# # ['111', '222']        # 未使用分组
# # ['111', 'a', '222']   # 使用分组


# import re
# s1 = '1 + 2 + (4 / 5  + 2)'
#
# print(re.subn(' ', '', s1))  # 直接去除计算表达式中的空格
#
# # 执行结果：
# # ('1+2+(4/5+2)', 9)    # 替换了9次空格

# import re
# s1 = 'abc123'
# print(re.match("[\d]", s1))     # 从头开始搜索数字，如果开始没有匹配到返回None
# print(re.search("[\d]", s1).group())    # 从头开始搜索数字，匹配到第一个直接返回一个迭代器
# print(re.findall("[\d]", s1))   # 遍历查找字符串中的数字部分，查找到每个数字都以元素的形式展现
#
# # 执行结果：
# # None
# # 1
# # ['1', '2', '3']

# import re
# a = re.findall(r"a(\d+?)",'a23b')   # 在正则后面加'?'，表示惰性匹配，匹配到一个就直接返回
# print(a)
# b = re.findall(r"a(\d+)",'a23b')    # 贪婪匹配
# print(b)
#
# # 执行结果：
# # ['2']
# # ['23']
#
#
# a = re.match('<(.*)>','<H1>title<H1>').group()
# print(a)
# b = re.match('<(.*?)>','<H1>title<H1>').group()
# print(b)
#
# # 执行结果：
# # <H1>title<H1>
# # <H1>
#
# a = re.findall(r"a(\d+)b",'a3333b')
# print(a)
# b = re.findall(r"a(\d+?)b",'a3333b')
# print(b)
#
# # 执行结果：
# # ['3333']
# # ['3333']


























