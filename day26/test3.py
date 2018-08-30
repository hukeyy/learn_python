# -*- coding: utf-8 -*-
# Author: hkey
# class Student(object):
#
#     def get_score(self):
#          return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
# s = Student()
# s.set_score(10)
# print(s.get_score())

# class Student(object):
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 and value > 100:
#             raise  ValueError('score must between 0~100!')
#         self._score = value
#
# s = Student()
# s.score = 100
# print(s.score)

# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2018 - self._birth
#
# s = Student()
# s.birth = 1992
# print(s.age)

# class Screen(object):
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, width):
#         self._width = width
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height):
#         self._height = height
#
#     @property
#     def resolution(self):
#         return self._width * self._height
#
#
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#     __repr__ = __str__
#
# print(Student('Michael'))

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a+b
        return a

f = Fib()
print(f[100])


# for n in Fib():
#     print(n)

































