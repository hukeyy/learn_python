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
lis = [2,3,"k",["qwe",20,["k1",["tt",3,"1"]],89],"ab","adv"]

lis[1] = 100
lis[3][2][1][1] = 100
print(lis)




















