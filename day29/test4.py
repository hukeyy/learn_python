#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey


class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __hash__(self):
        return hash('%s%s' % (self.name, self.sex))

    def __eq__(self, other):
        if self.name == other.name and self.sex == other.sex:
            return True


p_lst = []
for i in range(100):
    p_lst.append(Person('hkey', i, 'male'))
    p_lst.append(Person('alex', i, 'male'))
    p_lst.append(Person('yuan', i, 'male'))

print(set(p_lst))



