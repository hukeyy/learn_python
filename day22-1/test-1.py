#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

class Person(object):
    def __init__(self, name, hp, aggr, job):
        self.name = name
        self.hp = hp
        self.aggr = aggr
        self.job = job

    def hit(self, gg):
        gg.hp -= self.aggr
        print('\033[31;1m%s被打，掉了%s的血。\033[0m' % (gg.name, self.aggr))


class Dog(object):
    def __init__(self, name, hp, aggr, kind):
        self.name = name
        self.hp = hp
        self.aggr = aggr
        self.kind = kind

    def bite(self, p):
        p.hp -= self.aggr
        print('\033[31;1m%s被咬，掉了%s的血。\033[0m' % (p.name, self.aggr))


p = Person('kk', 100, 2, 'it')
teddy = Dog('teddy', 100, 3, 'teddy')

p.hit(teddy)
print(teddy.hp)

teddy.bite(p)
print(p.hp)
