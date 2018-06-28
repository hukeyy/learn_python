# -*- coding: utf-8 -*-
# Author: hkey

test = 'hkey'

def func1():
    print(test)

def func2():
    test = 'zhangsan'
    print(test)

def func3():
    global test
    print(test)
    test = 'xiaofei'
    print(test)


print(func1())
print('===========')
print(func2())
print('===========')
print(func3())
print('===========')
print(test)



