#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
# 1. 写函数，接收N个数字，求这些参数数字的和。

# def func1(*args):
#     n = 0
#     for i in args:
#         n +=i
#     return n
#
# m = func1(1,2,3,4,5)
# print(m)


# 2. 写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者

# def func2(*args):
#     return args[0][1::2]
# m = func2((1,2,3,4,5,6,7,8,9))
# print(m)


# 3. 写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5

# def func(li):
#     return len(li) > 5




# 4. 写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者

# def func(li):
#     return li[:2]
#
# print(func([1,2,3,4]))


# 5. 写函数，计算传入字符串中【数字】、【字母】、【空格】以及【其他】的个数并返回结果
# def func(st):
#     dic = {'digit':0, 'alpha':0, 'space':0, 'other': 0}
#     for i in st:
#         if i.isdigit():
#             dic['digit'] += 1
#         elif i.isalpha():
#             dic['alpha'] += 1
#         elif i.isspace():
#             dic['space'] += 1
#         else:
#             dic['other'] += 1
#
#     return dic


# 6. 写函数，检查用户传入字典的每一个values的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
# dic = {'k1':'v1v1', 'k2':[11,22,33,44]}

# def func(dic):
#     for k, v in dic.items():
#         dic[k] = v[:2]
#     return dic
#
# print(func(dic))

# 7. 写函数接收两个数字参数，返回比较大的那个数字。

# def func(x, y):
#     return max(x, y)
#
# print(func(10, 2))


# 8. 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作
import os
def file_oper(file, old, new):
    with open(file, 'r', encoding='utf-8') as read_file, open(file+'.bak', 'w', encoding='utf-8') as write_file:
        for line in read_file:
            print(line)
            new_line = line.replace(old, new)
            write_file.write(new_line)

    os.remove(file)
    os.rename(file+'.bak', file)


file_oper('test.txt', '哈哈', '嘿嘿')



