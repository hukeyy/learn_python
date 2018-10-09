#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


# def auth(auth_type):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             username = input('username:').strip()
#             passwd = input('passwd:').strip()
#             if auth_type == 'filedb':
#                 print('filedb 验证中...')
#                 if username == 'hkey' and passwd == '123':
#                     res = func(*args, **kwargs)
#                     return res
#
#             elif auth_type == 'ldap':
#                 print('ldap 验证中...')
#                 if username == 'admin' and passwd == '123':
#                     res = func(*args, **kwargs)
#                     return res
#
#         return wrapper
#
#     return decorator
#
#
# @auth('ldap')
# def home():
#     print('\033[32;1mwelcome home.\033[0m')
#
#
# @auth('filedb')
# def shopping_cars():
#     print('\033[32;1mshopping cars \033[0m')
#
#
# shopping_cars()
# home()

# import sys
# sys.setrecursionlimit(10000000)
#
# n = 0
#
# def story():
#     global n
#     n +=1
#     print(n)
#     story()
#
# story()


# def my_sum(n):
#     if n > 0:
#         return n + my_sum(n -1)
#     else:
#         return 0
#
# num = my_sum(100)
# print(num)

# for i in range(50):
#     print(i, end=',')

# def age(n):
#     if n == 1:
#         return 40
#     else:
#         return age(n-1) + 2

# print(age(4))

# l[12] = 41


# l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
# l = [2, 3, 5, 7, 9, 11]


# def find(l, aim):
#     mid_index = len(l) // 2
#     if l[mid_index] > aim:
#         find(l[:mid_index], aim)
#     elif l[mid_index] < aim:
#         find(l[mid_index+1:], aim)
#     else:
#         print(mid_index, l[mid_index])
#
#
# find(l, 82)

# def find(l, aim, start=0, end=None):
#     end = len(l) if end is None else end    # start =0 end = 6
#     mid_index = (end - start) // 2 + start  # mid_index = (6 - 0) // 2 + 0 = 3
#     if start <= end:
#         if l[mid_index] > aim:
#             return find(l, aim, start=start, end=mid_index-1)
#         elif l[mid_index] < aim:    # 7 < 100
#             return find(l, aim, start=mid_index+1, end=end) # find(l, aim, start=1, end=6)
#         else:
#             return (mid_index, l[mid_index])
#     else:
#         return ('\033[31;1mError: 未找到.\033[0m')
#
# res = find(l, 8)
# print(res)


# def search(num,l,start=None,end=None):
#     start = start if start else 0
#     # end = end if end is None else len(l) - 1
#     end = len(l) - 1 if end is None else end
#     mid = (end - start)//2 + start  # start = 0 end = 4 mid = (4-0)//2+0 =2
#     if start > end:
#         return None
#     elif l[mid] > num : # 5 > 3
#         return search(num,l,start,mid-1)    # search(3,l,0,1)
#     elif l[mid] < num:
#         return search(num,l,mid+1,end)
#     elif l[mid] == num:
#         return mid
#
# s = search(100, l)
# print(s)




# def find(l, aim, start=None, end=None):
#     start = start if start else 0   # start = 0
#     end = len(l) -1 if end is None else end # end = 2
#     mid_index = (end - start) // 2 + start  # mid_index = (2-0) // 2 + 0 = 1
#     if start > end:
#         return None
#     if l[mid_index] > aim:
#         return find(l, aim, start, mid_index-1)
#     elif l[mid_index] < aim:    # 3 < 100
#         return find(l, aim, mid_index+1, end)   # find(l, 100, 2, 2)
#     else:
#         return mid_index, l[mid_index]
#
# res = find(l, 100)
# print(res)
#
# def find(l, aim, start=None, end=None):     # find(l, 100, 2, 2)
#     start = start if start else 0   # start = 2
#     end = len(l) -1 if end is None else end # end = 2
#     mid_index = (end - start) // 2 + start  # mid_index = (2-2) // 2 + 2 = 2
#     if start > end:
#         return None
#     if l[mid_index] > aim:
#         return find(l, aim, start, mid_index-1)
#     elif l[mid_index] < aim:    # 5 < 100
#         return find(l, aim, mid_index+1, end)   # find(l, 100, 3, 2)
#     else:
#         return mid_index, l[mid_index]


l = [2,3,5]


def find(l, aim, start=0, end=None):
    end = len(l)-1 if end is None else end    # start = 0 end = 3
    mid_index = (end-start) // 2 + start    # mid_index = (3-0) // 2 + 0 = 1
    if start > end:
        return None
    if l[mid_index] > aim:
        return find(l, aim, start, mid_index-1)
    elif l[mid_index] < aim:    # 3 < 6
        return find(l, aim, mid_index+1, end)   # find(l, 6, 2, 3)
    else:
        return mid_index, l[mid_index]


f = find(l, 6)
print(f)
















