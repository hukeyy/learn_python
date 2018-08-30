# -*- coding: utf-8 -*-
# Author: hkey
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
#
#
# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)
# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())

# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     def set_score(self, score):
#         if 0 <= score <= 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score.')
#
#     def print_score(self):
#         print('%s: %s' %(self.__name, self.__score))
#
#
# hkey = Student('hkey', 100)
# print(hkey.__dict__)
# print(hkey.get_name())
# hkey.set_score(80)
# print(hkey.get_score())

# class Student(object):
#     def __init__(self, name, gender):
#         self.__name = name
#         self.__gender = gender
#
#     def get_name(self):
#         return self.__name
#
#     def get_gender(self):
#         return self.__gender
#
#     def set_gender(self, sex):
#         if sex in ('female', 'male'):
#             self.__gender = sex
#         else:
#             raise ValueError('参数不合法')
#
#
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')

# class Animal(object):
#     def run(self):
#         print('Animal is running...')
#
# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')
#     def eat(self):
#         print('Eating meat...')
#
#
# class Cat(Animal):
#     pass
#
# # dog = Dog()
# # dog.run()
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
# # run_twice(Animal())
#
# # run_twice(Dog())
#
# class Tortoise(Animal):
#     def run(self):
#         print('Tortoise is running slowly...')
#
# class Timer(object):
#     def run(self):
#         print('Start...')
#
# run_twice(Tortoise())
# run_twice(Timer())

# class Student(object):
#     name = 'Student'
#
# s = Student()
# print(s.name)
# print(Student.name)
# s.name = 'hkey'
# print(s.name)
# print(Student.name)
# del s.name
# print(Student.name)
# print(s.name)


# class Student(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Student.count += 1
#
# if Student.count != 0:
#     print('测试失败!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('测试失败!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('测试失败!')
#         else:
#             print('Students:', Student.count)
#             print('测试通过!')

# class Student(object):
#     pass
#
# def set_age(self, age):
#     self.age = age
#
# from types import MethodType
# # s = Student()
# # s.set_age = MethodType(set_age, s)
# # s.set_age(25)
# # print(s.age)
#
# s2 = Student()
# # s2.set_age(24)
# # s.name = 'hkey'
# # print(s.name)
#
# def set_score(self, score):
#     self.score = score
# s = Student()
# Student.set_score = set_score
#
# s.set_score(100)
# print(s.score)
#
# s2.set_score(99)
# print(s2.score)

class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'hkey'
s.age = 20

s.score = 100






















































