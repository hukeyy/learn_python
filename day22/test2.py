# -*- coding: utf-8 -*-
# Author: hkey

class Person(object):
    def __init__(self, name, hp, aggr, sex):
        self.name = name
        self.hp = hp
        self.aggr = aggr
        self.sex = sex

    def attack(self, dog):
        dog.hp -= self.hp
        print('\033[31;1m【%s】被打，掉了【%s】血量.\033[0m' %(dog.name, self.aggr))



class Dog(object):
    def __init__(self, name, hp, aggr, kind):
        self.name = name
        self.hp = hp
        self.aggr = aggr
        self.kind = kind

    def bite(self, person):
        person.hp -= self.aggr
        print('\033[31;1m【%s】被咬，掉了【%s】血量.\033[0m' %(person.name, self.aggr))

p = Person('小k', 200, 12, '男')
d = Dog('狗儿', 500, 20, 'teddy')

d.bite(p)
print('------------')
p.attack(d)



