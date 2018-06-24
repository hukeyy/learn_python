# -*- coding: utf-8 -*-
# Author: hkey


# test = 'hkey'
# v = test.capitalize()
# print(v)

# test = 'HkEy'
# v1 = test.casefold()
# v2 = test.lower()
# print(v1, v2)

# name = 'hkey'
#
# v3 = name.center(20,'#')
# print(v3)

# 在字符串中寻找子序列出现的个数
# name = 'hkeyxiaoxiao'
#
# v = name.count('x')
# print(v)
#
# # 执行结果：
# 2
# # 可设置起始位置和结束位置
#
# name = 'hkeyxiaoxiao'
# v1 = name.count('x', 0, 8)
# print(v1)
#
# # 直接结果：
# 1

# name = 'hkey'
#
# v = name.startswith('h')
# print(v)
#
# # 执行结果：
# True
#
#
# v1 = name.endswith('y')
# print(v1)
#
# # 执行结果：
# True

# name = 'hkeykey'
#
# # 从开始找第一个匹配的序列，并打印序列起始的索引位置
# v1 = name.find('key')
# print(v1)
#
# # 执行结果：
# 1
#
# # (sub, start=None, end=None) start：起始位置 end: 结束位置
# v2 = name.find('key', 0, 3)
# print(v2)
#
# # 执行结果：
# -1

# # 格式化，将一个字符串中指定的占位符替换为值
# test = 'i am {name}, age {a}'
# print(test)
# # 执行结果：
# i am {name}, age {a}
#
# v = test.format(name='hkey', a=20)
# print(v)
# # 执行结果：
# i am hkey, age 20


# test = 'i am {0}, age {1}'
# print(test)
#
# # 执行结果：
# i am {0}, age {1}
#
# v = test.format('hkey', 20)
# print(v)
#
# # 执行结果：
# i am hkey, age 20

# 格式化，将一个字符串中指定的占位符替换为值
# test = 'i am {0}, age {1}'
# print(test)
# # 执行结果：
# i am {name}
#
# v = test.format('hkey', 20)
# print(v)
# # 执行结果：
# i am hkey

# format_map 通过字典的形式将值传给对应 key 的占位符
# test = 'i am {name}, age {a}'
#
# v1 = test.format_map({'name': 'hkey', 'a': 20})
#
# print(v1)
#
# # 执行结果：
# # i am hkey, age 20


# name = 'hkey'
# v = name.index('y')
# print(v)
# # 执行结果：
# # 3
#
# v1 = name.index('z')
# print(v1)

# 执行结果：
# Traceback (most recent call last):
#   File "E:/learn_python/day11/s2.py", line 119, in <module>
#     v1 = name.index('z')
# ValueError: substring not found

# test = 'abcd+_'
# v = test.isalnum()
# print(v)
#
# # 执行结果：
# # False
#
# test = 'abcd'
# v = test.isalnum()
# print(v)
#
# # 执行结果：
# # True

# s = 'username\temail\tpassword\nhkey\thkey@qq.com\thkeyy'
# v = s.expandtabs(20)
# print(v)
#
# # 执行结果：
# # username            email               password
# # hkey                hkey@qq.com         hkeyy

# s = 'superman'
# v = s.isalpha()
# print(v)
#
# # 执行结果：
# # True

# test1 = '二'
# v1 = test1.isdecimal()
# v2 = test1.isdigit()
# # 能够判断中文数字的写法
# v3 = test1.isnumeric()
# print(v1, v2, v3)
#
# # 执行结果：
# # False False True

# test = 'hkey'
# v = test.islower()
# print(v)
#
# # 执行结果：
# # True

# test = 'abcdefg\t'
# v = test.isprintable()
# print(v)
#
# # 执行结果：
# # False

# test = ' '
# v = test.isspace()
# print(v)
#
# # 执行结果：
# # True

# test = 'my heart will go on'
#
# v = test.istitle()
# v1 = test.title()
# print(v)
# print(v1)
#
# # 执行结果：
# # False
# # My Heart Will Go On

# test = '看不见你的笑我怎么睡得着'
# v = '#'.join(test)
# print(v)
#
# # 执行结果：
# # 看#不#见#你#的#笑#我#怎#么#睡#得#着

# name = 'hkey'
#
# v1 = name.ljust(20,'*')
# v2 = name.rjust(20, '*')
# print(v1)
# print(v2)
#
# # 执行结果：
# # hkey****************
# # ****************hkey

# name = 'hkey'
# v1 = name.zfill(20)
# print(v1)
#
# # 执行结果：
# # 0000000000000000hkey

# test = 'my heart will go on'
#
# v1 = test.isupper()
# v2 = test.upper()
# print(v1)
# print(v2)
#
# # 执行结果：
# # False
# # MY HEART WILL GO ON

# name = '\nhkey\n'
#
# v1 = name.lstrip()
# v2 = name.rstrip()
# v3 = name.strip()
# print(v1)
# print(v2)
# print(v3)
#
# # 执行结果：
# # v1:
# # hkey
# #
# # v2:
# #
# # hkey
# # v3:
# # hkey

# test1 = 'abcdefg'
# test2 = '1234567'
#
# v = 'adfasdfzcvdrfhkljwerto'
# m = str.maketrans(test1, test2)
# new_m = v.translate(m)
# print(new_m)
#
# # 执行结果：
# # 1461s46z3v4r6hkljw5rto

# test = 'asdfadfsdfxzscv'
#
# # 将字符串分割为三分，并将分隔符作为独立的元素进行分割
# v = test.partition('s')
# print(v)
#
# # 从右边开始，将字符串分割为三分，并将分隔符作为独立的元素进行分割
# v1 = test.rpartition('s')
# print(v1)
#
# # 用指定的字符分割字符串，分割后的列表中不包含分割的字符，可执行分割次数
# v2 = test.split('s', 1)
# print(v2)
# # 从右边开始，用指定的字符分割字符串，分割后的列表中不包含分割的字符，可执行分割次数
# v3 = test.rsplit('s', 1)
# print(v3)
#
# # 执行结果：
# #
# # v:
# # ('a', 's', 'dfadfsdfxzscv')
# # v1:
# # ('asdfadfsdfxz', 's', 'cv')
# # v2:
# # ['a', 'dfadfsdfxzscv']
# # v3:
# # ['asdfadfsdfxz', 'cv']

# test = 'adfaf\nadfadf\nadfaf\n'
# v = test.splitlines(True)
# v1 = test.splitlines(False)
# print(v)
# print(v1)
#
# # 执行结果：
# # v:
# # ['adfaf\n', 'adfadf\n', 'adfaf\n']
# # v1:
# # ['adfaf', 'adfadf', 'adfaf']

# test = 'hkey'
#
# # 以什么开头
# v1 = test.startswith('h')
# # 以什么结尾
# v2 = test.endswith('e')
# print(v1)
# print(v2)
#
# # 执行结果：
# # True
# # False

# name = 'HkEy'
# v = name.swapcase()
#
# print(v)
#
# # 执行结果：
# # hKeY

# name = 'hkey'
# print(name[2])
#
# # 执行结果：
# # e

# name = 'hkey'
# print(name[0:2])
#
# # 执行结果：
# # hk

name = 'hkey'
print(len(name))

# 执行结果：
# 4

str