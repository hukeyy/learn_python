#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# li = '[1,2,3,4]'
#
# print(eval(li))
# print(type(eval(li)))
#
# # 执行结果：
# # [1, 2, 3, 4]
# # <class 'list'>

# dic = "{'a':1, 'b':2, 'c':3}"
#
# print(eval(dic))
# print(type(eval(dic)))
#
# # 执行结果：
# # {'c': 3, 'a': 1, 'b': 2}
# # <class 'dict'>

# tu = '(1, 2, 3, 4, 5)'
#
# print(eval(tu))
# print(type(eval(tu)))
#
# # 执行结果：
# # (1, 2, 3, 4, 5)
# # <class 'tuple'>

# s1 = 'print("hello world")'
# eval(s1)
#
# # 执行结果：
# # hello world

# s1 = '1+2+3+4'
#
# n = eval(s1)
# print(n)
#
# # 执行结果：
# # 10

# x = 10
# def func():
#     y = 20
#     a = exec("x+y")
#     print("a:",a)
#     b = exec("x+y",{"x":1,"y":2})
#     print("b:",b)
#     c = exec("x+y",{"x":1,"y":2},{"y":3,"z":4})
#     print("c:",c)
#     d = exec("print(x,y)")
#     print("d:",d)
# func()
#
# # exec 不会有任何返回值
#
# # 执行结果：
# # a: None
# # b: None
# # c: None
# # 10 20
# # d: None


# x = 10
# expr = """
# z = 30
# sum = x + y + z   #一大包代码
# print(sum)
# """
# def func():
#     y = 20
#     exec(expr)   #10+20+30
#     exec(expr,{'x':1,'y':2}) #30+1+2
#     exec(expr,{'x':1,'y':2},{'y':3,'z':4}) #30+1+3，x是定义全局变量1，y是局部变量
#
# func()
#
# # 执行结果：
# # 60  # 10+20+30
# # 33  # 30+1+2
# # 34  # 30+1+3

# s = """              #一大段代码
# for x in range(10):
#     print(x, end='')
# print()
# """
# code_exec = compile(s, '<string>', 'exec')   #必须要指定mode，指定错了和不指定就会报错。
# code_eval = compile('10 + 20', '<string>', 'eval')   #单个表达式
# code_single = compile('name = input("Input Your Name: ")', '<string>', 'single')   #交互式
#
# a = exec(code_exec)   #使用的exec，因此没有返回值
# b = eval(code_eval)
#
# c = exec(code_single)  #交互
# d = eval(code_single)
#
# print('a: ', a)
# print('b: ', b)
# print('c: ', c)
# print('name: ', name)
# print('d: ', d)
# print('name; ', name)

# name = input('your name:')  # 接收一个str的返回值
#
# print(name)
#
# # 执行结果：
#
# # your name:hkey
# # hkey


# print('hello world')
# print(123456)
#
# # 执行结果：
# # hello world
# # 123456

# print('name: %s, age: %d' %('hkey', 20))
#
# # 执行结果：
# # name: hkey, age: 20

# s = 120.123123
#
# print('%.2f' %s)    # 小数点后面保留2位
# print('%.4f' %s)    # 小数点后面保留4位
#
# # 执行结果：
# # 120.12
# # 120.1231

# for i in range(10):
#     print(i, end='')
#
# # 执行结果：
# # 0123456789

# func = lambda x: x*x
#
# f = func(2)
# print(f)
#
# # 执行结果：
# # 4

# func = lambda x, y: x+y
#
# f = func(1, 2)
# print(f)
#
# # 执行结果：
# # 3
# from functools import reduce
#
# r = reduce(lambda x, y: x + y, [1,2,3,4,5])
# print(r)
#
# # 执行结果：
# # 15

# l = [1,2,3,4,5,6,7, 8, 9]
# def is_odd(n):
#     return n % 2 == 1
#
#
# f = filter(is_odd, l)
# print(list(f))
#
# # 执行结果：
# # [1, 3, 5, 7, 9]







# def is_palindrome(n):
#     hx = str(n)
#     if hx == hx[::-1]:
#         return hx
#
# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# L=[('b',2),('a',1),('c',3),('d',4)]
#
# print(sorted(L, key=lambda x:x[1])) # 利用 key  进行比较

# 执行结果：
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

a = [1, 2, 3]
b = [4, 5, 6]

z = zip(a, b)

print(list(z))




















