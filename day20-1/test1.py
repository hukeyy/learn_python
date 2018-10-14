#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# import pickle
#
# dic = {'k1': 1, 'k2': 2, 'k3': 3}
#
# str_dic = pickle.dumps(dic) # 使用dumps进行序列化，序列化后是一串字节类型的数据。
# print(str_dic)

# 执行结果：
# b'\x80\x03}q\x00(X\x02\x00\x00\x00k1q\x01K\x01X\x02\x00\x00\x00k2q\x02K\x02X\x02\x00\x00\x00k3q\x03K\x03u.'

# import pickle
#
# dic2 = pickle.loads(b'\x80\x03}q\x00(X\x02\x00\x00\x00k1q\x01K\x01X\x02\x00\x00\x00k2q\x02K\x02X\x02\x00\x00\x00k3q\x03K\x03u.')
# print(dic2) # loads进行反序列化得到结果
#
# # 执行结果：
# # {'k2': 2, 'k3': 3, 'k1': 1}

# import pickle
# with open('file.json', 'rb') as f:
#     l2 = pickle.load(f)
#
# print(l2)
#
# # 执行结果：
# # [1, 2, 3, 4, 5, 6, 'hehe', 'haha']

# import shelve
# dic = dict(zip(['name', 'age'], ['hkey', 20]))
# print(dic)

# import shelve
# l1 = ['male', 20]
# she = shelve.open('user', writeback=True)
# she['xiaom'] = l1
# she['xiaom'].append('aaa')
# print(she['xiaom'])
# she.close()

# import shelve
# she = shelve.open('user')
# she['xiaom'] = ['male', 20] # 字典的形式，添加一个列表
# she['xiaom'].append('aaa')  # 新增一个元素
# she.close()
#
# import shelve
#
# s = shelve.open('user')
# print(s['xiaom'])
# s.close()
#
# # 执行结果：
# # ['male', 20, 'aaa']


# import shelve
# she = shelve.open('user', writeback=True)   # 开启回写模式
# she['xiaom'] = ['male', 20] # 字典的形式，添加一个列表
# she['xiaom'].append('aaa')  # 新增一个元素
# she.close()




























