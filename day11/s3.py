# -*- coding: utf-8 -*-
# Author: hkey
#
# name = 'hkey'
# print(name.encode())

# test = '1a1dsf123'
# print(test.isidentifier())
#
# # 执行结果；
# # False

# name = 'hkeykey'
# # 将字符串中的 'k' 替换为 'f' 最多替换1次
# print(name.replace('k', 'f', 1))
#
# # 执行结果：
# # hfeykey

# name = 'khkeykey'
# # 从右到左查找字符索引位置
# print(name.rfind('y'))
#
# # 执行结果：
# # 7

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

# test = '看不见你的笑我怎么睡得着'
# v = '#'.join(test)
# print(v)

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
# # ['asdfadfsdfxz', 'cv']
# # v3:
# # ['a', 'dfadfsdfxzscv']
# # v4:
# # ['asdfadfsdfxz', 'cv']
# name = 'hkey'
# v1 = name[0:2]
# v2 = name[0:4:2]
# print(v1)
# print(v2)
#
# # 执行结果：
# # v1:
# # hk
# # v2:
# # he
#
# name = 'hkey'
# gender = '男'
# info = name + gender
# print(info)

# a = "alex"
# b = a.capitalize()
# print(a)
# print(b)

# name = "  aleX"
# name = 'hkey'
# print(name.strip())
# print(name.startswith('al'))
# print(name.endswith('X'))
# print(name.replace('l', 'p'))
# print(type(name.split('l')))
# print(name.upper())
# print(name.lower())
# print(name[0:3])
# print(name[-2:])
# print(name.find('e'))
# print(name[:len(name)-1])
# for i in 'superman':
#     print(i)

# li = "alexericrain"
#
# print('_'.join(li))


# li = ['alex', 'eric', 'rain']
#
# print('_'.join(li))

# content = input('请输入内容：')
#
# str1 = content.split('+')
# n = 0
# for i in str1:
#     m = int(i.strip())
#     n += m
# print(n)


# content = input('请输入内容：')
#
# n = 0
# m = 0
# for i in content:
#     if i.isalpha():
#         n += 1
#     if i.isdigit():
#         m += 1
# print('字母为：', n)
# print('数字为：', m)

# name = input('name:')
# place = input('place:')
# thing = input('do something:')
#
# print('敬爱可亲的%s，最喜欢在 %s 地方干 %s ' % (name, place, thing))

















