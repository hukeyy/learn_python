#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
class Person:
    '''人类'''

    def __init__(self, name, hp, aggr, sex):
        self.name = name
        self.hp = hp
        self.aggr = aggr
        self.sex = sex
        self.price = 0  # 设置人类初始金钱

    def hit(self, dog):
        dog.hp -= self.aggr
        print('\033[31;1m%s被打，掉了%s的血.\033[0m' % (dog.name, self.aggr))

    def get_weapon(self, weapon):
        '穿戴武器'
        if self.price > weapon.price:  # 购买武器
            self.price -= weapon.price
            self.weapon = weapon  # 带上武器


class Dog:
    '''狗类'''

    def __init__(self, name, hp, aggr, kind):
        self.name = name
        self.hp = hp
        self.aggr = aggr
        self.kind = kind

    def bite(self, person):
        person.hp -= self.aggr
        print('\033[31;1m%s被咬，掉了%s的血.\033[0m' % (person.name, self.aggr))


class Weapon:
    def __init__(self, name, aggr, njd, price):
        self.name = name
        self.aggr = aggr
        self.njd = njd
        self.price = price

    def dazhao(self, dog):
        if self.njd > 0:
            dog.hp -= self.aggr * 2
            print('\033[33;1m【%s】使用武器【%s】，发大招伤害【%s】\033[0m' % (dog.name, self.name, self.aggr * 2))


per = Person('kk', 100, 2, 'male')
dog = Dog('teddy', 200, 5, 'teddy')

per.hit(dog)
dog.bite(per)
hit_dog = Weapon('dbg', 20, 3, 998)  # 实例化一个武器对象-打狗棒
per.price += 998  # 冲钱才能变强
per.get_weapon(hit_dog)  # 人物装备上武器
per.weapon.dazhao()  # 人物使用武器发大招
