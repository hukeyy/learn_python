#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# dic = {'name':'jay', 'age':18, 'sex': 'male'}

# dic.popitem()   # 随机删除并返回删除元组，元组里面是删除的键值对
# print(dic)
# dic1 = {"name": "hkey", "age": 18, "sex": "male"}
# dic1["heigh"] = 185
# dic1['name'] = 'jay'
# print(dic1)
# # 执行结果：
# # {'age': 18, 'sex': 'male', 'name': 'jay', 'heigh': 185}
# dic = {'name':'jay', 'age':18, 'sex': 'male'}
#
# dic.setdefault('age', 20)       # 存在不修改，不报错
# dic.setdefault('heigh', 180)    # 不存在修改。
# print(dic)
#
# # 执行结果:
# # {'sex': 'male', 'heigh': 180, 'age': 18, 'name': 'jay'}

# dic = {'name':'jay', 'age':18, 'sex': 'male'}
# t1 = dic.pop('name1111', None)    # 当 key 不存在时，则返回定义的第二个参数给 t1
# print(t1)
# # 执行结果：
# # None

# dic = {'name':'jay', 'age':18, 'sex': 'male'}
#
# t1 = dic.popitem()  # 随机删除key-value 并作为元组返回给 t1
# print(t1, type(t1))
# print(dic)
#
# # 执行结果：
# # ('name', 'jay') <class 'tuple'>
# # {'sex': 'male', 'age': 18}

# dic = {'name':'jay', 'age':18, 'sex': 'male'}
# del dic['name'] # 删除字典中的键值对
# del dic # 直接删除整个字典

# dic = {'name':'jay', 'age':18, 'sex': 'male'}
# dic2 = {'name1':'hkey', 'age1': 20}
#
# dic.update(dic2)    # 将dic2作为参数合并到dic中，dic变，dic2不变
#
# print('dic:', dic)
# print('dic2:', dic2)
#
# # 执行结果：
# # dic: {'age': 18, 'name': 'jay', 'sex': 'male', 'name1': 'hkey', 'age1': 20}
# # dic2: {'age1': 20, 'name1': 'hkey'}

# dic = {'name':'jay', 'age':18, 'sex': 'male'}

# print(dic.keys())
# print(dic.values())
# print(dic.items())

# 执行结果：
# dict_keys(['age', 'sex', 'name'])
# dict_values([18, 'male', 'jay'])
# dict_items([('age', 18), ('sex', 'male'), ('name', 'jay')])

# dic = {'name':'jay', 'age':18, 'sex': 'male'}

# # keys()、values()、items() 一般用for来遍历
#
# for k in dic:   # 循环 key 值
#     print(k)
#
# for v in dic.values():  # 循环 value 值
#     print(v)
#
# for k, v in dic.items():    # 循环key, value 值
#     print(k, v)

# dic = {'name':'jay', 'age':18, 'sex': 'male'}
# print(dic.get('name'))
# print(dic.get('name111', None))
#
# # 执行结果：
# # jay
# # None

s1 = 'asdf123sdfer45sdf3'

for i in s1:    # 循环整个 s1 字符串
    if i.isalpha(): # 当单个字符串是字母的时候，就将字母替换成空格
        s1 = s1.replace(i, ' ')
li = s1.split() # 通过空格将字符串 s1 分隔成列表
print(len(li))  # 直接统计列表元素的个数

# 执行结果：
# 3









