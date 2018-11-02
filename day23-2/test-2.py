#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

class Aniaml:
    def __init__(self, name, aggr, hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp
    def eat(self):
        self.hp += 100

class Person(Aniaml):
    def __init__(self, name, aggr, hp, sex):
        Aniaml.__init__(self, name, aggr, hp)
        self.sex = sex
        self.tooth = 0
    def eat(self):
        Aniaml.eat(self)
        self.tooth += 2


p = Person('hkey', 10, 100, 'male')
p.eat()
print(p.name)
print(p.hp)
print(p.tooth)

