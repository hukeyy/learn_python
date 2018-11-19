#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


# class Foo:
#     def __init__(self, name):
#         self.name = name
#
#     def __getitem__(self, item):
#         if hasattr(self, item):
#             return self.__dict__[item]
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         print('执行删除.')
#         if hasattr(self, key):
#             self.__dict__.pop(key)
#
#
# f = Foo('hkey')
# f['age'] = 20
# print(f.__dict__)
# print(f.age)
# print(f['name'])
# print(f['age'])

# class Fib(object):
#     def __getitem__(self, item):
#         if isinstance(item, int):
#             a, b = 1, 1
#             for x in range(item):
#                 a, b = b, a+b
#             return a
#         if isinstance(item, slice):
#             start = item.start
#             stop = item.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a+b
#             return L
#
#
# f = Fib()
# print(f[:10])


# class Func:
#     def __repr__(self):
#         return 'repr: class func.'
#
#     def __str__(self):
#         return 'str: class str.'
#
#
# f = Func()
# print('%s'%f)
# print('%r'%f)


# class A:
#     def __init__(self):
#         self.x = 1
#         print('in init function.')
#
#     def __new__(cls, *args, **kwargs):
#         print('in new function')
#         return object.__new__(A, *args, **kwargs)
#
#
# a = A()
# print(a.x)


# class Foo:
#     def __del__(self):
#         print('类完结')
#
#     def __call__(self, *args, **kwargs):
#         print('hello Foo.')
#     def __len__(self):
#         return 10
#
#
#
# f = Foo()
# f()
# print(len(f))

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __hash__(self):
#         return hash(str(self.name)+str(self.age))
#
#     def __eq__(self, other):
#         if self.name == other.name:
#             return True
#         return False
#
#
# p = Person('hkey', 20)
# k = Person('hkey', 23)
#
# print(p == k)

# Car = namedtuple('Car', ['rank', 'suit'])
#
#
# class FranchDeck:
#     ranks = [str(n) for n in range(2, 11)] + list('JKQA')
#     suits = ['红桃', '方块', '梅花', '黑桃']
#
#     def __init__(self):
#         self._cards = [Car(rank, suit) for rank in FranchDeck.ranks for suit in FranchDeck.suits]
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, item):
#         return self._cards[item]
#
#     def __setitem__(self, key, value):
#         self._cards[key] = value
#
#
# deck = FranchDeck()
# print(deck[10])
#
# from random import choice
# print(choice(deck))
#
# from random import shuffle
# shuffle(deck)
# print(deck[:10:2])

# 重点：namedtuple的使用、random shuffle 洗牌的使用  getitem、setitem连用可以实现切片

# from collections import namedtuple
#
# MytunpleClass = namedtuple('MytunpleClass', ['name', 'age', 'gender'])
# obj = MytunpleClass('hkey', 20, 'male')
# print('name:', obj.name)
# print('age:', obj.age)
# print('gender:', obj.gender)


# class Fib:
#     def __getitem__(self, item):
#         a, b = 1, 1
#         if isinstance(item, int):
#             for i in range(item):
#                 a, b = b, a+b
#             return a
#         if isinstance(item, slice):
#             start = item.start
#             stop = item.stop
#             if item.start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a+b
#             return L
#     # def __setitem__(self, key, value):
#     #     self[key] = value
#
# f = Fib()
# print(f[:10])

# from collections import namedtuple
# Car_Namedtuple = namedtuple('Car_Namedtuple', ['num', 'color'])
#
# class Cards:
#     nums = list(range(2, 11)) + list('JQKA')
#     colors = ['红桃', '黑桃', '方块', '梅花']
#
#     def __init__(self):
#         self._cards = [Car_Namedtuple(num, color) for num in Cards.nums for color in Cards.colors]
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, item):
#         return self._cards[item]
#     def __setitem__(self, key, value):
#         self._cards[key] = value
#
#
# card = Cards()
# print(len(card))
# print(card[:4])
# from random import shuffle
# shuffle(card)
# print(card[:4])


# class Func:
#     def __getitem__(self, item):
#         # object[item] 触发
#         return self.__dict__[item]
#
#     def __setitem__(self, key, value):
#         # object[key] = value 触发
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         # del object[key] 触发
#         print('delitem: 删除key')
#         del self.__dict__[key]
#
#     def __delattr__(self, item):
#         # del object.item 触发
#         print('delattr: 删除key')
#         del self.__dict__[item]
#
#
# f = Func()
# f['name'] = 'hkey'  # __setitem__
# f['age'] = 20   # __setitem__
# print(f.name)   # 对象属性原本的调用方式
# print(f['name'])    # __getitem__
# del f['name']   # __delitem__
# print('------')
# del f.age   # __delattr__

class Fib:
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            print('item:', item)
            start = item.start
            stop = item.stop
            print('stop:', stop)
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib()
print(f[:5])



