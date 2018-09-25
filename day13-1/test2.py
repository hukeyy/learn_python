#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

# l1 = [1,2,3,4,5,6,7,8,9]
#
# # 使用列表生成式将列表中的各个元素加1
# list_num = [x+1 for x in l1]
# print(list_num)

# s1 = 'hello world'
# print('__iter__' in dir(s1))
# print('__next__' in dir(s1))
#
# # 字符串s1包含 __iter__ 方法且不包含__next__方法，所以字符串 s1 只是一个可迭代的类型，并不是一个迭代器
#
# # 执行结果：
# # True
# # False

# s1 = 'hello world'
# s2 = s1.__iter__()  # 将可迭代类型转换为 迭代器 使用 __iter__()
# print('__iter__' in dir(s2))
# print('__next__' in dir(s2))
#
# # 使用 __iter__()方法将 s1 字符串转换为迭代器，迭代器既有__iter__方法，又有 __next__方法
# # 执行结果：
# # True
# # True

# 自定义一个迭代器：

class My_iterator(object):
    def __init__(self, x, max):
        self.mul, self.x = x, x
        self.xmax = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.x and self.x !=1:
            self.mul = self.mul + self.x
            if self.mul < self.xmax:
                return self.mul
            else:
                raise StopIteration

if __name__ == '__main__':
    myite1 = My_iterator(2, 100)
    for i in myite1:
        print(i)