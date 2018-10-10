#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# menu = {
#     '北京': {
#         '海淀': {
#             '五道口': {
#                 'soho': {},
#                 '网易': {},
#                 'google': {}
#             },
#             '中关村': {
#                 '爱奇艺': {},
#                 '汽车之家': {},
#                 'youku': {},
#             },
#             '上地': {
#                 '百度': {},
#             },
#         },
#         '昌平': {
#             '沙河': {
#                 '北航': {},
#             },
#             '天通苑': {},
#             '回龙观': {},
#         },
#         '朝阳': {},
#         '东城': {},
#     },
#     '上海': {
#         '闵行': {
#             "人民广场": {
#                 '炸鸡店': {}
#             }
#         },
#         '闸北': {
#             '火车战': {
#                 '携程': {}
#             }
#         },
#         '浦东': {},
#     },
#     '山东': {},
# }


# zone = {
#     '西安':{
#         '碑林区':{
#             '钟楼':{},
#             '鼓楼':{}
#         }
#     },
#     '安康':{
#         '高新区':{
#             '公园1':{},
#             '公园2':{},
#         }
#     }
#
# }


# def threeLM(dic):
#     for i in dic:
#         print(i)
#     choice = input('>>>').strip()
#     if choice in dic:
#
#         city_zone = dic[choice]
#         return threeLM(city_zone)
#     elif choice.upper() == 'Q' and choice.upper() == 'B':
#
#         return choice
#
# threeLM(menu)



# def treeML(dic):
#     while True:
#         for i in dic:
#             print(i)
#
#         key = input('>>>').strip()
#         if key == 'b' or key == 'q':
#             return key
#
#         elif key in dic:
#             res = treeML(dic[key])
#             if res == 'q':
#                 return 'q'
#
# treeML(menu)


# def find(l, aim):
#     mid_index = len(l) // 2    # 这里需要取整数不能是小数
#     if l[mid_index] > aim:  # 当取的值大于要找的值，取左边
#         find(l[:mid_index], aim)    # 通过切片取list左边的值
#     elif l[mid_index] < aim:    # 当取的值大于要找的值，取右边
#         find(l[mid_index+1:], aim)    # 通过切片取list右边的值
#     else:
#         print(mid_index, l[mid_index])  # 数字比较只有三种情况，大于、小于、等于
#
# find(l, 82)

l = [2,3,5]


def find(l, aim, start=None, end=None):
    start = start if start else 0   # start = 0
    end = len(l) if end is None else end # end = 3
    mid_index = (end - start) // 2 + start  # mid_index = (3-0) // 2 + 0 =1
    if start > end:
        return None
    if l[mid_index] > aim:
        return find(l, aim, start, mid_index-1)
    elif l[mid_index] < aim:    # 3 < 100
        return find(l, aim, mid_index+1, end)   # find(l, 6, 2, 3)
    elif l[mid_index] == aim:
        return mid_index, l[mid_index]

res = find(l, 6)
print(res)

# 执行结果：
# (22, 82)


def find(l, aim, start=None, end=None): # find(l, 6, 2, 3)
    start = start if start else 0   # start = 2
    end = len(l) if end is None else end # end = 3
    mid_index = (end - start) // 2 + start  # mid_index = (3-2) // 2 + 2 =2
    if start > end:
        return None
    if l[mid_index] > aim:
        return find(l, aim, start, mid_index-1)
    elif l[mid_index] < aim:    # 5 < 6
        return find(l, aim, mid_index+1, end)   # find(l, 6, 3, 3)
    elif l[mid_index] == aim:
        return mid_index, l[mid_index]


def find(l, aim, start=None, end=None): # find(l, 6, 3, 3)
    start = start if start else 0   # start = 3
    end = len(l)-1 if end is None else end # end = 3
    mid_index = (end - start) // 2 + start  # mid_index = (3-3) // 2 + 3 = 3
    if start > end:
        return None
    if l[mid_index] > aim:  # l 最大的索引为：2 这里：l[3] 报错啦，因此 end = len(l)-1 if end is None else end
        return find(l, aim, start, mid_index-1)
    elif l[mid_index] < aim:
        return find(l, aim, mid_index+1, end)   # find(l, 6, 3, 3)
    elif l[mid_index] == aim:
        return mid_index, l[mid_index]












