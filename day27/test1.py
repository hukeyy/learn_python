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
#     day9 = 0
#     month = 0
#     year = 0
#
#     def __init__(self, year=0, month=0, day9=0):
#         self.day9 = day9
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def get_date(cls, string_date):
#         year, month, day9 = map(int, string_date.split('-'))
#         date1 = cls(year, month, day9)
#         return date1
#
#
#     def out_data(self):
#         print('year:')
#         print(self.year)
#         print('month:')
#         print(self.month)
#         print('day9:')
#         print(self.day9)
#
# r = Data_test2.get_date(' 2018-02-04')
# r.out_data()


# 上面的实例等于先调用了 get_date()对字符串进行处理， 然后才使用 Data_test对构造函数初始化；
# 这样的好处就是你以后重构类的时候不必要修改构造函数，只需要额外添加你要处理的函数， 然后使用装饰器 @classmethod 就可以了

# import sys
#
# year = 2018
# age = 29
#
#
# var = input('>>>').strip()
#
# print(getattr(sys.modules[__name__], var))

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
#         self.__dict__.pop(item)
#
#
# f = Foo('hkey')
# print(f['name'])
# print(f.name)

# class Foo(object):
#     f = '类对静态变量'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hi(self):
#         print('hi, %s' % self.name)
#
# obj = Foo('hkey', 20)
#
# print(hasattr(obj, 'name'))
# print(hasattr(obj, 'say_hi'))
#
# n = getattr(obj, 'name')
# print(n)
# func = getattr(obj, 'say_hi')
# func()
# print(getattr(obj, 'aaaaa', '不存在啊!'))
#
# setattr(obj, 'show_name', lambda self: self.name+'king')
# print(obj.__dict__)
# print(obj.show_name(obj))
#
# delattr(obj, 'name')
# delattr(obj, 'show_name')
# delattr(obj, 'show_name111')
# print(obj.__dict__)

# class Foo:
#     f = '类对静态变量'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hi(self):
#         print('hi, %s' % self.name)
#
# obj = Foo('xiaofei', 20)
#
# # 检测是否含有某属性
# print(hasattr(obj, 'name'))
# print(hasattr(obj, 'say_hi'))
# # 执行结果：
# # True
# # True
#
# print('--------------------------------------')
#
# # 获取属性：
# print(getattr(obj, 'name'))
# func = getattr(obj, 'say_hi')
# func()
# print(getattr(obj, 'aaaaa', '不存在!'))
#
# # 执行结果：
# # xiaofei
# # hi, xiaofei
# # 不存在!
#
# print('--------------------------------------')
#
# # 设置属性
#
# setattr(obj, 'gender', 'female')
# setattr(obj, 'show_name', lambda self: self.name + 'er')
# print(obj.gender)
# print(obj.show_name(obj))
#
# # 执行结果：
# # female
# # xiaofeier
#
# print('--------------------------------------')
#
# # 删除属性
# delattr(obj, 'age')
# delattr(obj, 'show_name')
# print(obj.__dict__)
# # 执行结果：
# # {'gender': 'female', 'name': 'xiaofei'}
#
# delattr(obj, 'aaaa')    # 删除不存在的属性会报错

# import os
#
#
# class Manage_cmd(object):
#     def run(self):
#         while True:
#             cmd = input('>>>').strip()
#             if not cmd: continue
#             if hasattr(self, cmd):
#                 func = getattr(self, cmd)
#                 func()
#             else:
#                 print('-bash: %s: command not found' % cmd)
#
#     def ls(self):
#         print(os.listdir('.'))
#
#
# cmd = Manage_cmd()
# cmd.run()
#
# # 执行结果：
# # >>>ls
# # ['logger.py']
# # >>>asdfadf
# # -bash: asdfadf: command not found

# class Foo(object):
#     staticField = 'hello world.'
#
#     def __init__(self):
#         self.name = 'hkey'
#
#     def test(self):
#         return 'test'
#
#     @staticmethod
#     def bar():
#         return 'bar'
#
# print(getattr(Foo, 'staticField'))
# print(getattr(Foo, 'test'))
# func = getattr(Foo, 'bar')
# print(func())
#
# # 执行结果：
# # hello world.
# # <function Foo.test at 0x00000141FE18D158>
# # bar

# import sys
#
# def s1():
#     print('s1')
#
# def s2():
#     print('s2')
#
# this_module = sys.modules[__name__]
# print(hasattr(this_module, 's1'))
# func = getattr(this_module, 's2')
# func()
#
# # 执行结果：
# # True
# # s2

# '''
# 程序目录：
#     module_test.py
#     logger.py
#
# 当前文件:
#     logger.py
# '''
#
# import module_test as obj
#
# if hasattr(obj, 'test'):
#     func = getattr(obj, 'test')
#     func()
#
# # 执行结果：
# # form the test.


# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __getitem__(self, item):
#         print(self.__dict__[item])
#
#
# s = Student('hkey')
# s.age = 20
# s['name']
# s['age']
# # 执行结果：
# # hkey
# # 20


# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
#     def __getitem__(self, item):
#         print(self.__dict__[item])
#
# s = Student('hkey')
# # 调用类的__setitem__方法，通过dict的形式进行添加对象的属性
# s['age'] = 20
# s['hobby'] = 'coding'
#
# # 调用类的__getitem__方法，通过dict的形式获取对象的属性
# s['age']
# s['hobby']
#
# # 执行结果：
# # 20
# # coding

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __getitem__(self, item):
#         return self.__dict__[item]
#
#     def __delitem__(self, key):
#         self.__dict__.pop(key)
#         print('执行我了。')
#
#
# s = Student('hkey')
# s.age = 20
# print(s['name'])
# print(s['age'])
# del s['age']
#
# # 执行结果：
# # hkey
# # 20
# # 执行我了。






















