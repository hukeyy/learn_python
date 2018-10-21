#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


# class Person(object):
#     def __init__(self, name, hp, aggr, sex):
#         self.name = name
#         self.hp = hp
#         self.aggr = aggr
#         self.sex = sex
#         self.price = 0
#
#     def attack(self, dog):
#         dog.hp -= self.aggr
#
#     def get_weapon(self, weapon):
#         if self.price > weapon.price:
#             self.price -= weapon.price
#             self.weapon = weapon
#             self.aggr += weapon.aggr
#         else:
#             print('\033[32;1m只要998，打狗棒带回家。\033[0m')
#
#
# class Dog(object):
#     def __init__(self, name, hp, aggr, kind):
#         self.name = name
#         self.hp = hp
#         self.aggr = aggr
#         self.kind = kind
#
#     def bite(self, person):
#         person.hp -= self.aggr
#
#
# class Weapon(object):
#     def __init__(self, name, aggr, ljd, price):
#         self.name = name
#         self.aggr = aggr
#         self.ljd = ljd
#         self.price = price
#
#     def hand18(self, person):
#         if self.ljd > 0:
#             person.hp -= self.aggr * 2
#             self.ljd -= 1
#         else:
#             print('\033[31;1m耐久度不够，请修复装备.\033[0m')
#
#
# # 实例化人类
# xiaom = Person('xiaom', 100, 1, 'male')
# # 实例化狗
# gougou = Dog('gougou', 500, 2, 'teddy')
# # 实例化武器
# w = Weapon('stick', 200, 3, 998)
# # 变强变强变强
# xiaom.price += 1000  # 不够强难道不是因为你冲的钱不到位？
#
# print('xiaom 赤手空拳攻击力：', xiaom.aggr)
# # 带上武器
# xiaom.get_weapon(w)
# print('xiaom 带上打狗棒攻击力：', xiaom.aggr)
# # 使用武器大招
# xiaom.weapon.hand18(gougou)
# print(gougou.hp)
#
# # xiaom.attack(gougou)
# # print(gougou.hp)

class Brithday(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class Teacher(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    def brith(self, brith):
        self.brithday = brith

brith = Brithday(1900, 10, 1)
feifei = Teacher('feifei', 'girl')
feifei.brith(brith)
print(feifei.brithday.year)

























