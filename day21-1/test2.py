#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
#
#
# def func(dic):
#     for k, v in dic.items():
#         if len(v) > 2:
#             dic[k] = v[:2]
#     return dic


# l1 = [0, 1, 2, 3, 4, 5, 6, 7]
#
# f = l1[1::2]
# print(f)
#
#
# def func(*args):
#     li = args[0]
#     return li[1::2]
#
#
# print(func(l1))

# a = '1234'
#
# l = list(map(int, a))
# print(l)

# obj = [25, 9, -23, 9, -11]
#
# print(sorted(obj, key=abs))


# 2017-11-1 2017-11-30

# import time
#
# start_time = time.mktime(time.strptime('2017-11-1', '%Y-%m-%d'))
# end_time = time.mktime(time.strptime('2017-11-30', '%Y-%m-%d'))
#
# while end_time >= start_time:
#     w_dic = {0: '星期一', 1: '星期二', 2: '星期三', 3: '星期四', 4: '星期五', 5: '星期六', 6: '星期日'}
#     print(time.strftime('%Y-%m-%d', time.localtime(start_time)), w_dic[time.localtime(start_time).tm_wday])
#     start_time += 86400.00

# def foo(n):
#     a, b = 0, 1
#     while b < n:
#         yield b
#         a, b = b, a+b
#
#
# f = foo(21)
# import re
# with open('ip.txt') as f:
#     i_list = []
#     for line in f:
#         ip_list = re.findall(r'((([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5]))',
#                              line)
#         for ip in ip_list:
#             i_list.append(ip[0])
#
# print(i_list)
# import re
#
# s = '123.33sdhf3424.34fdg323.324'
#
# r = re.findall("\d*\.\d*", s)
#
# n = 0
# for num in r:
#     n += float(num)
#
# print(n)


# import re
# result='aakk123ddd55kk66'
# r = re.sub("\d", 'A', result, 4)  # re.sub(匹配到的正则，'替换的内容', '需要被替换的内容')
# print(r)

# import random
#
# code = ''
# for i in range(4):
#     ran_int = random.randint(1, 9)
#     ran_str = chr(random.randint(65, 90))
#     n = random.choice([str(ran_int), ran_str])
#     code = ''.join([code, n])
#
# print(code)


# portfolio = [
# {'name': 'IBM', 'shares': 100, 'price': 91.1},
# {'name': 'AAPL', 'shares': 50, 'price': 543.22},
# {'name': 'FB', 'shares': 200, 'price': 21.09},
# {'name': 'HPQ', 'shares': 35, 'price': 31.75},
# {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
#
# f = filter(lambda x: x['price']> 100, portfolio)
# print(list(f))


# def foo(a1, args = []): # 设置参数时，默认参数不能为可变数据类型
#     print("args before = %s" % (args))
#     args.insert(0, 10)
#     args.insert(0, 99999)
#     print("args = %s " % (args))
#
# def main():
#     foo('a')
#     foo('b')
#
# if __name__ == "__main__":
#     main()
# m = ''
# for i in range(1, 10):
#     for n in range(1, 10):
#         cf = str(i)+'*'+str(n)+'='+str(i*n)
#         print(cf)


# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()


# li = ["alex", "wusir", "eric", "rain", "alex"]
# print(li.count('alex'))

# li = [1, 3, 2, "a", 4, "b", 5, "c"]
# l6 = reversed(li[1:6:2])
# print(list(l6))
# lis = [2,3,"k",["qwe",20,["k1",["tt",3,"1"]],89],"ab","adv"]
# lis.insert(1, 100)
# lis.pop(2)
# lis[3][2][1].insert(1, 100)
# lis[3][2][1].pop(2)
# print(lis)

# lis = [2,3,"k",["qwe",20,["k1",["tt",3,"1"]],89],"ab","adv"]
# lis[3][2][1].insert(3, 101)
# print(lis)
# lis[3][2][1].pop(-2)
# print(lis)

# li = ["alex","eric","rain"]
# print("_".join(li))

# li = ["taibai ","alexC","AbC ","egon","Ritian"," Wusir"," agc"]
# l2 = []
# for k in li:
#     k = k.strip()
#     if k.capitalize().startswith('A') and k.endswith('c'):
#         l2.append(k)
#
# print(l2)


# li = ["苍老师","东京热","武藤兰","波多野结衣"]
# while True:
#     str1 = input('>>>').strip()
#     if str1 in li:
#         str1 = str1.replace(str1, '***')
#     print(str1)

# li = [1,3,4, 'xiaom', [3,7,8, [5,6,7,8], 'taibai'],5,'hotdog']
#
# def func(lis):
#     for i in lis:
#         if isinstance(i, list):
#             return func(i)
#         print(i)
#
# func(li)

# lic = [0, 1, 2, 3, 4, 5]
# def func(l):
#     return l[1::2]
# print(func(lic))

# def func(s):
#     if len(s) > 5:
#         print('%s > 5' % s)
#     elif len(s) <= 5:
#         print('%s <= 5' % s)


# def func(n):
#     return n[:2]


# context = input('>>>')
#
# def func(arg):
#     dic = {'数字':0, '字母':0, '空格':0, '其他':0}
#     for i in arg:
#         if i.isdigit():
#             dic['数字'] += 1
#         elif i.isalpha():
#             dic['字母'] += 1
#         elif i.isspace():
#             dic['空格'] += 1
#         else:
#             dic['其他'] += 1
#     return dic
#
# print(func(context))

# l = ['a', ' b', 'c ', 'hel   lo', 1, 2, 3]
# def func(arg):
#     for i in arg:
#         i = str(i)
#         if ' ' in i:
#             print('%s 内有空格' % i)
#
#         else:
#             print(i)
# func(l)
# dic = {1: 123, 'a': 'hello', 'b':['world', 'nice', 'bigbang']}
#
# def func(dic):
#     for k, v in dic.items():
#         if not isinstance(v, (int, float, bool)):
#             dic[k] = v[:2]
#     return dic
#
# print(func(dic))

# print(max(1, 10))

# import os
#
# file_name = input('文件名：')
# be_modify = input('要修改的内容：')
# af_modify = input('要替换的内容：')
#
# def func(file, be_f, af_f):
#     with open(file, 'r', encoding='utf-8') as read_f, open(file+'_new', 'w', encoding='utf-8') as write_f:
#         for line in read_f:
#             if be_f in line:
#                 new_line = line.replace(be_f, af_f)
#                 write_f.write(new_line)
#             else:
#                 write_f.write(line)
#     os.remove(file_name)
#     os.rename(file_name + '_new', file_name)
#
#
# func(file_name, be_modify, af_modify)

def regist():
    while True:
        user = input('user:').strip()
        if not user: continue
        else:
            break
    pwd = input('pwd:').strip()
    dic = ('注册账号：{}, 密码：{}'.format(user, pwd))
    return dic

# print(regist())


def login():
    count = 1
    while count < 4:
        username = input('username:')
        password = input('password:')
        if username == 'hkey' and password == '123':
            print('登录成功.')
            return
        else:
            print('登录失败.')
        count += 1

login()
















