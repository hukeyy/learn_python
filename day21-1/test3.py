#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# a = 1
# def fun(a):
#     a = 2   # 在函数作用域中定义了 a = 2
#     return a    # 返回a时，首先在函数内作用域中查找，找到则直接返回
# print(fun(a))   # a = 2
# print(a)    # 在全局作用域中查找 a = 1

# a = []  # a 是一个可变类型
# print(id(a))
# def fun(a):
#     a.append(1) # 在函数没有找到变量a,在全局作用域中找到 a = []
#     return a    # 返回 a = [1]
# print(fun(a))   # a = [1]
# print(a)    # 因为a为可变数据类型，在内存中指向是的list体，当list内部发生变化并不会影响变量a的指向
# print(id(a))

# L = [x*x for x in range(10)]    # 列表生成式，返回list所有元素
# print(L)
#
# g = (x*x for x in range(10))    # 生成器, 惰性计算，节省资料开销
# print(g)

# L = [x*x for x in range(10)]
# print(type(L))
# g = (x*x for x in range(10))
# print(type(g))
#
# 执行结果：
# <class 'list'>
# <class 'generator'>

# def func(n):
#     if n == 1:
#         return 1
#     return n * func(n -1)
#
# print(func(5))

# import time
#
# def timer(flag):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if flag == True:
#                 with open('timer.txt', 'a') as f:
#                     f.write(time.asctime())
#             res = func(*args, **kwargs)
#             return res
#         return wrapper
#     return decorator
#
# @timer(True)
# def foo():
#     print('hello foo')
#
# foo()

# def func(dic):
#     for k, v in dic.items():
#         dic[k] = v[:2]
#     return dic
# d1 = {'a': 'abcde', 'b': [1, 2, 3, 4, 5]}
# print(func(d1))

# def func(li):
#     return li[1::2]
# l1 = [0, 1, 2, 3, 4, 5]
# print(func(l1))

# a="1234"
# print(list(map(int, a)))

# obj = [25, 9, -23, 9, -11]
# print(sorted(obj, key=abs))

# import time
#
# start_time = time.mktime(time.strptime('2017-11-1', '%Y-%m-%d'))
# end_time = time.mktime(time.strptime('2017-11-30', '%Y-%m-%d'))
# w_day = {0:'星期一', 1:'星期二', 2:'星期三', 3:'星期四',4:'星期五',5:'星期六',6:'星期日',}
# while start_time <= end_time:
#     print(time.strftime('%Y-%m-%d', time.localtime(start_time)),
#           w_day[time.localtime(start_time).tm_wday])
#     start_time += 86400.00

# def foo(n):
#     a, b = 0, 1
#     while b <= n:
#         yield b
#         a, b = b, a+b
#
# for i in foo(21):
#     print(i,end=' ')

# import re
# with open('ip.txt') as f:
#     i_list = []
#     for line in f:
#         ip_list = re.findall(r'((([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5]))',
#                              line)
#         for ip in ip_list:
#             i_list.append(ip[0])
# print(i_list)

# import re
# s = '123.33sdhf3424.34fdg323.324'
# num_list = re.findall(r"\d+\.\d*", s)
# n = 0
# for i in num_list:
#     n += float(i)
#
# print(n)

# import re
# result='aakk123ddd55kk66'
#
# s1 = re.sub(r"\d", 'A', result, 4)
# print(s1)

# import random
# count = 0
# code = ''
# while count < 4:
#     ran_num = random.randint(0, 9)
#     ran_alpha = chr(random.randint(65, 90))
#     ran_str = random.choice([str(ran_num), ran_alpha])
#     code = ''.join([code, ran_str])
#     count+= 1
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
# f = filter(lambda x: x['price'] > 100, portfolio)
# print(list(f))


# def foo(a1, args = []): #
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

for i in range(1,10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i * j), end='')
    print()

















