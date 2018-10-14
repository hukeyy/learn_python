#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
# import json
#
# dic = {'k1':1, 'k2': 2, 'k3': 3}
#
# # 序列化
# str_dic = json.dumps(dic)   # dumps 就是将字典类型转换为字符串类型
# print(type(str_dic), str_dic)
#
# # 执行结果：
# # <class 'str'> {"k1": 1, "k2": 2, "k3": 3}
#
#
# # 反序列化
# dic2 = json.loads(str_dic)  # loads 将字符串类型转换为字典类型
# print(type(dic2), dic2)
#
# # 执行结果：
# # <class 'dict'> {'k2': 2, 'k3': 3, 'k1': 1}

# import json
#
# dic = {'k1':1, 'k2': 2, 'k3': 3}
# with open('test.json', 'w', encoding='utf-8') as f:
#     json.dump(dic, f)   # dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
#
# with open('test.json', 'r', encoding='utf-8') as f:
#     dic = json.load(f)  # load 方法接收一个文件句柄，直接将文件中的json字符串转换成数据结构返回
#
# print(type(dic), dic)
#
# # 执行结果：
# # <class 'dict'> {'k2': 2, 'k3': 3, 'k1': 1}

# import json
# dic = {'k1': '中国', 'k2': '美国', 'k3': 3}
# with open('file.json', 'w', encoding='utf-8') as f:
#     json.dump(dic, f, ensure_ascii=False)


# import json
# data = {'username':['小明','baby'],'sex':'male','age':16}
# json_dic2 = json.dumps(data,sort_keys=True,indent=2,separators=(',',':'),ensure_ascii=False)
# print(json_dic2)




























