# -*- coding: utf-8 -*-
# Author: hkey

# class Fib(object):
#     def __getitem__(self, item):
#         if item == 0 or item == 1:
#             return 1
#         else:
#             a, b = 1, 1
#             for i in range(item - 1):
#                 a, b = b, a + b
#             return b
#
#
# fib = Fib()
# for i in range(10):
#     print(fib[i])

# class Foo:
#     def __init__(self, name):
#         self.name = name
#
#     def __getitem__(self, item):
#         print(self.__dict__[item])
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         print('del obj[key]时,我执行')
#         self.__dict__.pop(key)
#
#     def __delattr__(self, item):
#         print('del obj.key时,我执行')
#         self.__dict__.pop(item)
#
#
# f = Foo('hkey')
# # print(f.__dict__)
# print(f['name'])
# f['age'] = 20
# print(f['age'])
#
# del f['age']
# del f.name

# class Teacher(object):
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def __str__(self):
#         return 'Teacher is object: %s' % self.name
#
#     def __repr__(self):
#         return str(self.__dict__)
#
#     def func(self):
#         return 'wahaha'
#
#
# t = Teacher('hkey', 200)
# print(t.name, t.salary)
# print(repr(t))


# class Demo(object):
#     def __init__(self):
#         print('__init__() called...')
#
#     def __new__(cls, *args, **kwargs):
#         print('__new__() - {cls}'.format(cls=cls))
#         return object.__new__(cls, *args, **kwargs)
#
#
# if __name__ == '__main__':
#     de = Demo()

# class A(object):
#     def __init__(self):
#         print('init')
#
#     def __new__(cls, *args, **kwargs):
#         print('new %s' % cls)
#         return object.__new__(cls, *args, **kwargs)
#
# A()

# import os
#
# class Manage_cmd(object):
#     def options(self):
#         while True:
#             cmd = input('>>>').strip()
#             if not cmd: continue
#             if hasattr(self, cmd):
#                 cmd_func = getattr(self, cmd)
#                 cmd_func()
#             else:
#                 print('-bash: %s not found!' % cmd)
#
#     def ls(self):
#         print(os.listdir('.'))
#
#
# m = Manage_cmd()
# m.options()

# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __getitem__(self, item):
#         print(self.__dict__[item])
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         print('del obj[key]时，我执行')
#         self.__dict__.pop(key)
#
#     def __delattr__(self, item):
#         print('del obj.key时，我执行')
#         self.__dict__.pop(item)
#
#
# f1 = Foo('sb')
# print(f1['name'])
#
# f1['age'] = 20
# print(f1['age'])
# del f1['age']
# del f1.name

# class Singleton(object):
#     _instance = 'abc'
#     def __new__(cls, *args, **kwargs):
#         print('__new__')
#         if not hasattr(cls, '_instance'):
#             cls._instance = object.__new__(cls, *args, **kwargs)
#         return cls._instance
#
# # one = Singleton()
# # two = Singleton()
# # two.a = 3
#
# sing = Singleton()
# print(sing)





















