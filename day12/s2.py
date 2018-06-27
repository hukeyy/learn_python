# -*- coding: utf-8 -*-
# Author: hkey
# dict

# dict1 = {'name': 'hkey', 'age': 20, 'gender': '男'}
# dict1.clear()
# print(dict1)
#
# # 执行结果：
# # {}

# dict1 = {'name': 'hkey', 'age': 20, 'gender': '男'}
# dict2 = dict1.copy()
# print(dict2)
#
# # 执行结果：
# # {'age': 20, 'gender': '男', 'name': 'hkey'}

# dict1 = {'name': 'hkey', 'age': 20, 'gender': '男'}
# dict2 = dict.fromkeys(['a', 'b', 'c'], ['hello', 'world'])
# print(dict2)
#
# # 执行结果：
# # {'a': ['hello', 'world'], 'c': ['hello', 'world'], 'b': ['hello', 'world']}

# dict1 = {'name': 'hkey', 'age': 20, 'gender': '男'}
# print(dict1.get('age'))
# # 如果 get 没有找到对应的 key 则返回 None
# # 执行结果：
# # 20

# dict1 = {'name': 'hkey', 'age': 20, 'gender': '男'}
# for k, v in dict1.items():
#     print(k, v)
#
# # 执行结果：
# # age 20
# # gender 男
# # name hkey

# dict1 = {'name': 'hkey', 'age': 20, 'gender': '男'}
# for k in dict1.keys():
#     print(k)
#
# # 执行结果：
# # gender
# # age
# # name

# dict1 = {'name': 'hkey', 'age': 20, 'gender': '男'}
# for v in dict1.values():
#     print(v)
#
# # 执行结果：
# # 20
# # 男
# # hkey

# dict1 = {'name': 'hkey', 'age': 20, 'gender': '男'}
#
# dict1.pop('name')
# print(dict1)
#
# # 执行结果：
# # {'age': 20, 'gender': '男'}

# dict1 = {'name': 'hkey', 'age': 20, 'gender': '男'}
# dict2 = dict1.popitem()
# print('随机删除后的dict1', dict1)
# print('获取随机删除的键值对:', dict2)
#
# # 执行结果：
# # 随机删除后的dict1 {'gender': '男', 'name': 'hkey'}
# # 获取随机删除的键值对: ('age', 20)

# dict1 = {'name': 'hkey', 'age': 20, 'gender': '男'}
# d1 = dict1.setdefault('name1', 'xiaofei')
# print(d1)
#
# # 执行结果：
# # xiaofei

dict1 = {'name': 'hkey', 'age': 20, 'gender': '男'}
dict1.update({'name': 'xiaofei'})
dict1.update(age=19)
print(dict1)
# 执行结果：
# {'gender': '男', 'age': 19, 'name': 'xiaofei'}
