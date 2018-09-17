#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, pickle

def file_oper(file, mode, *args):
    if mode == 'wb':
        data = args[0]
        with open(file, mode) as f:
            pickle.dump(data, f)
    elif mode == 'rb':
        with open(file, mode) as f:
            data = pickle.load(f)
            return data


def user(user, pwd, mode):
    db_file = user + '.db'
    if mode == 'regist':
        if not os.path.isfile(db_file):
            user_info = {'name': user, 'passwd': pwd, 'stat': 0}
            file_oper(db_file, 'wb', user_info)
            print('\033[32;1m注册成功.\033[0m')
        else:
            print('\033[31;1m错误：该用户已存在.\033[0m')

    elif mode == 'login':
        if os.path.isfile(db_file):
            dict_user = file_oper(db_file, 'rb')
            if dict_user['name'] == user and dict_user['passwd'] == pwd:
                print('\033[32;1m登录成功.\033[0m')
                return dict_user
        else:
            print('\033[31;1m错误：该用户不存在.\033[0m')


def shopping(user_dict, list_goods):
    list_shopping = []
    while True:
        for i, k in enumerate(list_goods):
            print('序号：%s\r商品名：%s\r价格：%s' %(i, k['name'], k['price']))
        choice = input('\033[34;1m购买请输入商品序号：\033[0m').strip()
        if not choice: continue
        if choice.isdigit() and 0 <= int(choice) < len(list_goods):
            while True:
                num = input('\033[34;1m输入购买的数量：\033[0m').strip()
                if num.isdigit():
                    num = int(num)
                else:
                    print('\033[31;1m错误：数量必须是正整数.\033[0m')
                good = {'name': list_goods[int(choice)]['name'], 'num': num,
                        'total_prices': list_goods[int(choice)]['price'] * num}
                money = user_dict['money']
                for i in list_shopping:
                    money -= i['total_prices']
                if money < 0:
                    print('\033[31;1m错误：余额不足，无法购买.\033[0m')
                    break
                else:
                    list_shopping.append(good)
                    print('\033[32;1m购买成功.\033[0m')

        else:
            print('\033[31;1m错误：输入商品序号错误。\033[0m')




def start(list_goods):
    Flag = False
    while not Flag:
        print('1. 注册\n'
              '2. 登录\n'
              '3. 退出')
        choice = input('>>>').strip()
        if not choice: continue
        if choice.isdigit() and 0 < int(choice) < 4:
            if choice == '1':
                username = input('\033[34;1m输入用户名：\033[0m').strip()
                password = input('\033[34;1m输入密码：\033[0m').strip()
                user(username, password, 'regist')

            elif choice == '2':
                username = input('\033[34;1m输入用户名：\033[0m').strip()
                password = input('\033[34;1m输入密码：\033[0m').strip()
                user_dict = user(username, password, 'login')
                if user_dict['stat'] == 0:
                    money = input('\033[34;1m首次登录，请输入充值金额：\033[0m').strip()
                    if money.isdigit(): # 这里无法判断小数类型
                        user_dict['money'] = money
                        user_dict['stat'] = 1
                        print('\033[32;1m恭喜：充值成功!\033[0m')
                        print('user_dict:', user_dict)
                        shopping(user_dict, list_goods)

                    else:
                        print('\033[31;1m错误：金额只能是正整数！\033[0m')

                else:
                    # 这里应该有一个函数继续处理
                    shopping(user_dict, list_goods)

        else:
            print('\033[31;1m错误：序号输入错误.\033[0m')



if __name__ == '__main__':
    list_goods = [
{'name': 'banana', 'price': 10},
{'name': 'apple', 'price': 20},
{'name': 'pear', 'price': 30},
]
    start(list_goods)








