# class Course(object):
#     def __init__(self, name, price, time):
#         self.name = name
#         self.price = price
#         self.time = time
#
#
# class Grade(object):
#     def __init__(self, name, course):
#         self.name = name
#         self.course = course
#
#
# course = Course('python', 20000, 12)
#
# grade = Grade('三年二班', course)
#
# print(grade.course.name)
# print(grade.course.price)

# class gradfa(object):
#     def test(self):
#         print('from gradfa')
#
# class fa(object):
#     def test(self):
#         print('from fa')
#
# class son(fa, gradfa):
#     pass
#
#
# s = son()
# s.test()


# class Test(object):
#
#     @classmethod
#     def get(cls):
#         print('hello')
#
#
# t = Test()
# t.get()
# Test.get()

# class Classmethod_Demo():
#     role = 'dog'
#
#     @classmethod
#     def func(cls):
#         cls.role = 'cat'
#         print(cls.role)
#
# Classmethod_Demo.func()
# c = Classmethod_Demo()
# print(c.role)
#
# # c.func()

# class Data_test2(object):
#     day = 0
#     month = 0
#     year = 0
#
#     def __init__(self, year=0, month=0, day=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def get_date(cls, string_date):
#         year, month, day = map(int, string_date.split('-'))
#         date1 = cls(year, month, day)
#         return date1
#
#
#     def out_data(self):
#         print('year:')
#         print(self.year)
#         print('month:')
#         print(self.month)
#         print('day:')
#         print(self.day)
#
# r = Data_test2.get_date(' 2018-02-04')
# r.out_data()


# 上面的实例等于先调用了 get_date()对字符串进行处理， 然后才使用 Data_test对构造函数初始化；
# 这样的好处就是你以后重构类的时候不必要修改构造函数，只需要额外添加你要处理的函数， 然后使用装饰器 @classmethod 就可以了

import sys

year = 2018
age = 29


var = input('>>>').strip()

print(getattr(sys.modules[__name__], var))













