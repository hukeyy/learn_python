# -*- coding: utf-8 -*-
# Author: hkey


def person(name, age, job):
    data = {
        'name': name,
        'age': age,
        'job': job
    }

    def walk(p):
        print("person %s is walking..." % p['name'])
    return data

def dog(name, dog_type):
    data = {
        'name': name,
        'dog_type': dog_type
    }

    def bark(d):
        print("dog %s:wang.wang..wang..." % d['name'])
    return data


p1 = person('xiaoA', 18, 'it')
d1 = dog('dog_1', '泰迪')


print(p1.__dict__)