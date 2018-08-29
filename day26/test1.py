# -*- coding: utf-8 -*-
# Author: hkey


# class Person(object):
#     __key = '123'
#
#     def __init__(self, name, passwd):
#         self.name = name
#         self.__passwd = passwd
#
#     def __get_pwd(self):
#         return self.__passwd
#
#     def login(self):
#         self.__get_pwd()
#
#
# p = Person('hkey', '123')
# print(p.name)
# print(p._Person__passwd)

# from cmath import pi
#
# class Circle(object):
#     def __init__(self, r):
#         self.r = r
#     @property
#     def perimeter(self):
#         return 2*pi*self.r
#     @property
#     def area(self):
#         return self.r**2*pi
#
# c = Circle(4)
# print(c.perimeter)
# print(c.area)

# class Goods(object):
#     discount = 0.8
#
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#
#     @property
#     def price(self):
#         return self.__price * Goods.discount
#
# goods = Goods('apple', 5)
# print(goods.price)

# class Person(object):
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
# p = Person('hkey')
# print(p.name)
# p.name = 'xiaofei'
# print(p.name)
# del p.name
# print(p.name)

# class Myclass:
#     def instance_method(self, myself):
#         print('excute instance_method(%s, %s)' %(self, myself))
#
#     @classmethod
#     def class_method(cls, mycls):
#         print('excute class_mthod(%s, %s)' % (cls, mycls))
#
#     @staticmethod
#     def static_method():
#         print('excute static method.')
#
# myclass = Myclass()
# myclass.instance_method('hkey')

# class A(object):
#     def kkk(self, x):
#         print(self, x)
#
#     @classmethod
#     def classKkk(cls, x):
#         print(cls, x)
#
#     @staticmethod
#     def staticKkk(x):
#         print(x)
#     def mmm(x):
#         print(x)
#
# A.classKkk(2)
#
# A.kkk(A, 1)
# A.staticKkk(3)

# import time
#
#
# class TimeTest(object):
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     @staticmethod
#     def showTime():
#         return time.strftime('%H:%M:%S', time.localtime())
#
# # 通过类名直接调用静态方法
# print(TimeTest.showTime())
#
# # 执行结果：
# # 17:56:36
#
#
# t = TimeTest(2, 10, 10)
#
# # 通过实例也可以调用静态方法，执行结果和类名调用静态方法结果是一致的
# nowTime = t.showTime()
# print(nowTime)
# # 执行结果：
# # 17:56:36

# class People(object):
#     country = 'china'
#     @classmethod
#     def getCountry(cls):
#         return cls.country
#
# p = People()
# print(p.getCountry())
# print(People.getCountry())
#
# # 执行结果：
# # china
# # china

class People(object):
    country = 'china'

    @classmethod
    def getCountry(cls):
        return cls.country

    @classmethod
    def setCountry(cls, country):
        cls.country = country

p = People()
print(p.getCountry())
p.setCountry('japan')
print(p.getCountry())

print(People.getCountry())

# 执行结果：
# china
# japan
# japan













