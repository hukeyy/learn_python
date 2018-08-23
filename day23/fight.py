#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

class Person(object):
    def __init__(self, name, hp, aggr, sex):
        self.name = name
        self.hp = hp
        self.aggr = aggr
        self.sex = sex

    def hit(self, dog):
        dog.hp -= self.aggr
        print('%s 被打，掉了%s点血' % (dog.name, self.aggr))


class Dog(object):
    def __init__(self, name, hp, aggr, kind):
        self.name = name
        self.hp = hp
        self.aggr = aggr
        self.kind = kind

    def bite(self, person):
        person.hp -= self.aggr
        print('%s 被咬， 掉了 %s 点血.' %(person.name, self.aggr))


per = Person('jay', 100, 5, '男')
dog = Dog('gou', 10, 10, 'teddy')

per.hit(dog)
dog.bite(per)
