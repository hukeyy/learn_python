#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


# class Father1:  # 定义父类
#     print('class Father1')
#
#
# class Father2:  # 定义父类
#     print('class Father2')
#
#
# class Son1(Father1):  # 单继承，父类：Father1 子类：Son1
#     pass
#
#
# class Son2(Father1, Father2):  # 多继承： 父类：Father1, Father2 子类：Son2
#     pass


# print(Son1.__bases__)
# print(Son2.__bases__)
#
# # 执行结果：
# # (<class '__main__.Father1'>,)
# # (<class '__main__.Father1'>, <class '__main__.Father2'>)


# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Person(Animal):
#     def __init__(self, name, age, sex):
#         Animal.__init__(self, name, age)
#         self.sex = sex
#
#
# class Bird(Animal):
#     def __init__(self, name, age, kind):
#         Animal.__init__(self, name, age)
#         self.kind = kind
#
#
# p = Person('hkey', 20, 'male')
# b = Bird('maque', 1, 'maque')
# print(p.name)
# print(b.name)

# class A:
#     def haha(self):
#         print('A')
#
# class B(A):
#     def haha(self):
#         super(B, self).haha()
#         print('B')
#
# a = A()
# b = B()
# b.haha()
# print('------')
# super(B, b).haha()

# class A:
#     def test(self):
#         print('A')
#
# class B(A):
#     def test(self):
#         print('B')
#
# b = B()
# b.test()
#
# 执行结果：
# B

# class Animal:
#     '''
#     人和狗都是动物，所以创造一个Animal父类
#     '''
#     def __init__(self, name, aggr, hp):
#         self.name = name
#         self.aggr = aggr
#         self.hp = hp
#
#     def eat(self):
#         print('%s is eating.' % self.name)
#
#
# class Dog(Animal):
#     '''
#     狗类继承 Animal 类
#     '''
#     def __init__(self, name, aggr, hp, tooth):
#         super(Dog, self).__init__(name, aggr, hp)   # 使用 super 调用父类的方法
#         self.tooth = tooth  # 派生属性
#     def bite(self, person):
#         '''派生方法：狗有咬人的技能'''
#         person.hp -= self.aggr
#
#
# class Person(Animal):
#     '''
#     人类，继承 Animal 类
#     '''
#     def __init__(self, name, aggr, hp, money):
#         super(Person, self).__init__(name, aggr, hp)    # 使用 super 调用父类的方法
#         self.money = money  # 派生属性
#     def attack(self, dog):
#         '''派生方法：人有攻击的技能'''
#         dog.hp -= self.aggr
#
# p = Person('kk', 5, 100, 0)
# d = Dog('tt', 10, 50, 1000)
#
# print(p.hp)
# d.bite(p)
# print(p.hp)
#
# # 执行结果：
# # 100
# # 90

# class Teacher:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#     def teach(self):
#         print('teaching.')
#
# class Professor(Teacher):
#     pass
#
# p1 = Professor('kk', 'male')
# p1.teach()
from abc import ABCMeta, abstractclassmethod

# class Alipay:
#     '''
#     支付宝
#     '''
#     def pay(self, money):
#         print('支付宝支付了%s元.' % money)
#
#
# class Applepay:
#     '''
#     apple 支付
#     '''
#     def pay(self, money):
#         print('apple pay支付了%s元.' % money)
#
# class Wechatpay:
#     def fuqian(self, money):
#         print('Wechatpay支付了%s元.' % money)
#
#
# def pay(payment, money):
#     '''
#     支付函数，总体负责支付
#     对应支付的对象和要支付的金额
#     '''
#     payment.pay(money)
#
#
# w = Wechatpay()
# pay(w, 200)

# class A:
#     print('A')
#
# class B:
#     print('B')
#
# class C(A, B):
#     print('C')
#
#
# C()

# class A:
#     print('A')
#
# class B(A):
#     print('B')
#
# class C(A):
#     print('C')
#
# class D(B):
#     print('D')
#
# class E(C):
#     print('E')
#
# class F(D, E):
#     print('F')
#
# F()
# print(F.mro())
#
# # from D
# # [<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# from abc import ABC, abstractclassmethod, ABCMeta
# class Payment(metaclass=ABCMeta):
#     @abstractclassmethod
#     def pay(self, money):
#         raise NotImplemented
#
# class Wechat(Payment):
#     '''
#     微信支付
#     '''
#     def pay(self, money):
#         print('已经用微信支付%s元.' % money)
#
#
# class Alipay(Payment):
#     '''
#     支付宝支付
#     '''
#     def pay(self, money):
#         print('已经用支付宝支付%s元.' % money)
#
# class Applepay(Payment):
#     def fuqian(self, money):
#         print('已经用Applepay支付%s元.' % money)
#
#
#
# def pay(pay_obj, money):
#     '''
#     支付函数，总体负责支付
#     对应支付的对象和要支付的金额
#     '''
#     pay_obj.pay(money)
#
#
# ali = Alipay()
# pay(ali, 200)
#
# apple = Applepay()  # 实例化就能检查出子类是否创建了 pay 方法

class Animal:
    pass

class Dog(Animal):
    pass




































