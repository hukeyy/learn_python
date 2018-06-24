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

# def check_code():
#     import random
#     checkcode = ''
#     for i in range(4):
#         current = random.randrange(0, 4)
#         if current != i:
#             temp = chr(random.randint(65, 90))
#         else:
#             temp = random.randint(0, 9)
#         checkcode += str(temp)
#     return checkcode
#
# while True:
#     code = check_code()
#     print(code)
#     auth_code = input('输入验证码：')
#     if auth_code != code:
#         print('验证码错误！')
#         continue
#     else:
#         print('验证成功。')
#         break

# str1 = input('>>>')
# if '苍老师' in str1 or '东京热' in str1:
#     str2 = str1.replace('东京热', '***').replace('苍老师', '***')
#     print(str2)
# else:
#     print(str1)

while True:
    username = input('username:')
    pwd = input('pwd:')
    email = input('email:')
    str1 = username + '\t' + pwd + '\t' + email + '\n'
    cmd = input('>>>')
    if cmd == 'Q' or cmd == 'q':
        v = str1.expandtabs(20)
        print(v)
        break















