#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

goods = [
    {'name':'apple', 'price':20},
    {'name':'pear', 'price':10},
    {'name':'banana', 'price':30},
]



shopping_car = {}

print('欢迎光临.')
money = int(input('请确认你的钱：').strip())

while True:
    for i, k in enumerate(goods):
        print('序号%s: 商品名%s, 商品价格：%s' %(i, k['name'], k['price']))

    choice = input('\033[34;1m请选择序号：\033[0m').strip()
    if choice.isdigit() and 0 <= int(choice) < len(goods):
        num = input('\033[34;1m请输入购买的数量：\033[0m').strip()
        if num.isdigit():
            if money > goods[int(choice)]['price'] * int(num):
                money -= goods[int(choice)]['price'] * int(num)
                if goods[int(choice)]['name'] in shopping_car:
                    shopping_car[goods[int(choice)]['name']] = shopping_car[goods[int(choice)]['name']] + int(num)
                else:
                    shopping_car[goods[int(choice)]['name']] = int(num)

                print('\033[32;1m购物车中的商品%s,余额：%s\033[0m' %(goods[int(choice)]['name'], money))
            else:
                print('\033[31;1m错误：钱不够.\033[0m')

        else:
            print('\033[31;1m错误：输入的数量错误.\033[0m')
            break
    else:
        print('\033[31;1m错误：输入的序号错误\033[0m')




