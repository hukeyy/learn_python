#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

import pickle

db_file = 'user.db'
goods = [
    {'name':'apple', 'price': 10},
    {'name':'pear', 'price': 20},
    {'name':'banana', 'price': 30}
]

shopping_car = {}


def file_oper(file, mode, *args):
    if mode == 'wb':
        data = args[0]
        with open(file, mode) as f:
            pickle.dump(data, f)
    elif mode == 'rb':
        with open(file, mode) as f:
            data = pickle.load(f)
        return data


Flag = False

while not Flag:
    print('\033[32;1m欢迎登录超时系统\033[0m')
    username = input('username:').strip()
    passwd = input('passwd:').strip()
    user_info = file_oper(db_file, 'rb')
    if username == user_info['name'] and passwd == user_info['passwd']:
        if user_info['stat'] == 0:
            while True:
                salary = input('\033[32;1m首次登录，请输入个人金额：\033[0m').strip()
                if isinstance(salary, (int, float)):
                    print('\033[32;1m金额设置成功.\033[0m')
                    user_info['stat'] = 1
                    break
                else:
                    print('\033[31;1m错误，请设置金额.\033[0m')
        else:
            salary = user_info['salary']
        while not Flag:
            for i, k in enumerate(goods):
                print('\033[32;1m序号: %s 商品名：%s 价格：%s' %(i, goods[i]['name'], goods[i]['price']))

            choice = input('\033[32;1m请选择商品序号：\033[0m').strip()
            if choice.isdigit() and 0 <= int(choice) < len(goods):
                num = input('\033[32;1m请输入要购买的数量：\033[0m').strip()
                if num.isdigit():
                    pass
                else:
                    print('\033[31;1m错误：输入的数量错误。\033[0m')
            else:
                print('\033[31;1m错误：商品序号不存在.\033[0m')


    else:
        print('\033[31;1m错误：用户名密码错误！\033[0m')
















