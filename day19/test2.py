# -*- coding: utf-8 -*-
# Author: hkey

# class Person:
#     def __init__(self, name, age, sex, do_some_thing):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.do_some_thing = do_some_thing
#
#     def to_do_thing(self):
#         print('%s, %s岁, %s, %s' %(self.name, self.age, self.sex, self.do_some_thing))
#
# person = Person('小明', 10, '男', '上山去砍柴')
# person.to_do_thing()
# import math
# class Circle:
#     def __init__(self, banjing):
#         self.banjing = banjing
#
#     def zhouchang(self):
#         print('周长是%s' %(2 * math.pi * self.banjing))
#
#     def mianji(self):
#         print('面积是%s' %(math.pi * self.banjing **2))
#


# c = Circle(5)
# c.zhouchang()
# c.mianji()

class Session:
    language = 'Chinses'
    def __init__(self, kecheng, price):
        self.kecheng = 'linux'
        self.price = price


s = Session('Linux', 2000)
print(s.__dict__)
print(Session.__dict__)
print(s.language)

















