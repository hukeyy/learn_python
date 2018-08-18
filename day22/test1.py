# -*- coding: utf-8 -*-
# Author: hkey
def Person(name, hp, aggr, sex):
    person = {
        'name': name,
        'hp': hp,
        'aggr': aggr,
        'sex': sex
    }
    def attack(dog):
        dog['hp'] -= person['aggr']
        print('\033[31;1m【%s】被打，掉了【%s】血.\033[0m' % (dog['name'], person['aggr']))
    person['attack'] = attack
    return person

def Dog(name, hp, aggr, kind):
    dog = {
        'name': name,
        'hp': hp,
        'aggr': aggr,
        'kind': kind
    }
    def bite(person):
        person['hp'] -= dog['aggr']
        print('\033[31;1m【%s】被咬，掉了【%s】血.\033[0m' % (person['name'], dog['aggr']))
    dog['bite'] = bite
    return dog

xiaofei = Person('xiaofei', 1000, 1, '女')
jin = Dog('jin', 100, 2, 'teddy')
# xiaofei['attack'](jin)
jin['bite'](xiaofei)