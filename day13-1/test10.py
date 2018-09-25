#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

def deco(func):
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        next(ret)
        return ret
    return wrapper


@deco
def foo():
    food_list = []
    while True:
        food = yield food_list
        food_list.append(food)
        print('elements in foodlist are:', food)


g = foo()

print(g.send('apple'))
print(g.send('banana'))
print(g.send('pear'))






