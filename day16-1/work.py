#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
# 1. 用map来处理字符串列表，把列表中所有人都变成sb，比如alex_sb

name = ['alex', 'wupeiqi', 'yuanhao', 'nezha']

# print(list(map(lambda x: x+'_sb', name)))

# 2. 用filter函数处理数字列表，将列表中所有的偶数筛选出来

num = [1,3,5,6,7,8]

# print(list(filter(lambda x: x%2==0, num)))

# 3. 随意写一个20行以上的文件，运行程序，先将内容读到内存中，用列表存储。接收用户输入页码，每页5条，仅输出当页的内容

# with open('test.txt', 'r', encoding='utf-8') as f:
#     data = f.readlines()
#     page = int(input('请输入页码:').strip())
#     line = page * 5 - 5
#     if line > len(data):
#         print('\033[31;1m没有该页.\033[0m')
#     else:
#         for i in data[line:line+5]:
#             print(i.strip())


# 4. 如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'APPLE', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 20.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]


# 计算购买每支股票的总价

# lambda返回一个字典类型，更加友善
print(list(map(lambda x: {x['name']: x['shares'] * x['price']}, portfolio)))


# 用filter过滤出，单价大于100的股票有哪些
print(list(filter(lambda x: x['price']> 100, portfolio)))




