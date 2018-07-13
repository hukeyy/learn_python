# -*- coding: utf-8 -*-
# Author: hkey
# import json

# # 序列化 -------------------------------
# dic = {'name': 'hkey', 'age': 22}
#
# j = json.dumps(dic)
# print(j, type(j))
#
# # 执行结果：
# # {"age": 22, "name": "hkey"} <class 'str'>
#
# # 反序列化 --------------------------------
#
# i = json.loads(j)
# print(i, type(i))
#
# # 执行结果：
# # {'age': 22, 'name': 'hkey'} <class 'dict'>

# dic = {'name': 'hkey', 'age': 22}
#
# # ----------- 序列化 -----------
# with open('json.txt', 'w', encoding='utf-8') as f:
#     # 序列化后，直接存储 json.txt 文件
#     json.dump(dic, f)
#
# # ----------- 反序列化 -----------
#
# with open('json.txt', 'r') as f:
#     # 读取文件中json类型数据并做反序列化
#     data = json.load(f)
# print(data, type(data))
#
# # 执行结果：
# # {'age': 22, 'name': 'hkey'} <class 'dict'>

import pickle
dic = {'name': 'hkey', 'age': 22}

# #------------序列化------------
# j = pickle.dumps(dic)
# print(j)
#
# # 执行结果：
# # b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x16X\x04\x00\x00\x00nameq\x02X\x04\x00\x00\x00hkeyq\x03u.'
#
# #------------反序列化------------
# data = pickle.loads(j)
# print(data, type(data))
#
# # 执行结果：
# # {'name': 'hkey', 'age': 22} <class 'dict'>

# import pickle
# dic = {'name': 'hkey', 'age': 22}
# #------------序列化------------
# with open('pickel.txt', 'wb') as f:
#     # 序列化后，以字节格式存入 pickel.txt 文件
#     pickle.dump(dic, f)
# #------------反序列化------------
# with open('pickel.txt', 'rb') as f:
#     # 读取文件中字节，并做反序列化
#     data = pickle.load(f)
#
# print(data)
#
# # 执行结果：
# # {'name': 'hkey', 'age': 22}

import shelve

# f = shelve.open('shelve.txt')
# f['key1'] = {'name': 'xiaofei', 'age': 20}
# f.close()
# import shelve
#
# with shelve.open('shelve.txt') as f:
#     name = f['key1']['name']
# print(name)
#
# # 执行结果：
# # xiaofei