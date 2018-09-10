#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# name = 'aleX leNb'
# # 1. 有变量 name = 'aleX leNb' 完成如下操作：
# # 	（1）移除 name 变量对应的值两边的空格，并输出处理结果；
# print(name.strip())
#
# # 	（2）移除 name 变量左边的 'al' 并输出结果；
# print(name[2:])
#
# # 	（3）移除 name 变量右边的 'Nb'，并输出结果；
# print(name[:-3])
#
# # 	（4）移除 name 变量开头的 'a' 与最后的 'b'，并输出处理结果；
# print(name[1:-1])
#
# # 	（5）判断 name 变量是否以 'al' 结尾，并输出结果；
# print(name.endswith('al'))
#
# # 	（6）判断 name 变量是否以 'Nb' 结尾，并输出结果；
# print(name.endswith('Nb'))
#
# # 	（7）将 name 变量对应的值中的第一个'l' 替换成 'p'，并输出结果；
# name1 = name.replace('l', 'p', 1)
# print(name1)
#
# # 	（8）将 name 变量对应的值中的一个'l'替换成'p'，并输出结果；
# name1 = name.replace('i', 'p', 1)
#
# # 	（9）将 name 变量对应的值根据所有的 'l' 分隔，并输出结果；
# print(name.split('l'))
#
# # 	（10）将 name 变量对应的值变大写，并输出结果；
# print(name.upper())
#
# # 	（11）将 name 变量对应的值变小写，并输出结果；
# print(name.lower())
#
# # 	（12）将 name 变量对应的值变小写，并输出结果；
# print(name.lower())
#
# # 	（13）将 name 变量对应的值首字母'a'大写，并输出结果；
# print(name.capitalize())
#
# # 	（14）判断 name 变量对应的值字母'l'出现几次，并输出结果；
# print(name.count('l'))
#
# # 	（15）如果判断 name 变量对应的值前四位'l'出现几次，并输出结果；
# print(name[0:5].count('l'))
#
# # 	（16）从 name 变量对应的值中找到 'N' 对应的索引（如果找不到则报错，并输出结果）
# print(name.index('N'))
#
# # 	（17）从 name 变量对应的值中找到 'N' 对应的索引（如果找不到则返回-1）输出结果；
# print(name.find('N'))
#
# # 	（18）从 name 变量对应的值中找到 'X le'对应的索引，并输出结果；
# print(name.find('X le'))
#
# # 	（19）请输出 name 变量对应的值的第 2 个字符；
# print(name[1])
#
# # 	（20）请输出 name 变量对应的值的前 3 个字符；
# print(name[2])
#
# # 	（21）请输出 name 变量对应值的后 2个字符；
# print(name[-2:])
#
# # 	（22）请输出 name 变量对应的值中 'e'所在索引位置；
# print(name.find('e'))

# 2. 有字符串 s = '132a4b5c
#
# 	（1）通过对li列表的切片形成新的字符串s1, s2 = '123'
# 	（2）通过对li列表的切片形成新的字符串s2, s2 = 'a4b'
# 	（3）通过对li列表的切片形成新的字符串s3, s3 = '1245'
# 	（4）通过对li列表的切片形成字符串s4,s4 = '3ab'
# 	（5）通过对li列表的切片形成字符串s5,s5 = 'c'
# 	（6）通过对li列表的切片形成字符串s6,s6 = 'ba3'

# 2. 使用 while 和 for 循环分别打印字符串 s='asdfer'中的每个元素；

# s='asdfer'
# for i in s:
#     print(i)
#
# ite = iter(s)   # 转换为可迭代对象
#
# while True:
#     try:
#         each = next(ite)    # 使用next循环调用，直到抓到报错退出.
#     except StopIteration:
#         break
#     print(each)

# 4. 实现一个整数加法计算器；
# 如：content = input('输入内容：') # 如用户输入 1+1 2+8 5+

# content = input('输入内容：')
# li = content.split('+')
# count = 0
# if li[-1] == '':
#     li.pop()
#     for i in li:
#         count += int(i)
# print(count)


# content=input('请输入内容：')
# count = 0
# for i in content:
#     if i.isdigit():
#         count += 1
#
# print(count)

# 作业：打印li中所有元素，包括list中的元素，逐个打印出来。
# li = [1,2,3,4, 'hkey',[5,6,7,8,'xiaobai'], 'abc']
#
# for i in li:
#     if isinstance(i, list):
#         for j in i:
#             print(j)
#         continue
#     print(i)

t1 = ('hkey', 'xiaofei', 'kk')

# 把 xiaofei 修改为大写

# t1[3][0] = t1[3][0].upper()
# print(t1)

# 执行结果：
# (1, 2, 3, ['XIAOFEI', 'hkey', 'jay'], 'kk')

# t1 = ('hkey', 'xiaofei', 'kk')

# 把元组 t1 修改为字符串类型
# s1 = ''.join(t1)    # join中的参数必须是可迭代对象，list和tuple都是可迭代对象，并且列表中的元素只能是str类型
# print(s1)

# 执行结果：
# hkeyxiaofeikk




