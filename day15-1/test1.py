#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

import os, pickle


def file_oper(file, mode, *args):
    '''
    通过pickle序列化持久存储数据信息
    :param file: 不同的用户生成不同的数据文件，文件名+'.db'
    :param mode: 对数据文件的操作，读取还是写入
    :param args: 需要写入的数据信息
    :return: 返回读取数据文件的信息
    '''
    if mode == 'wb':
        data = args[0]
        with open(file, mode) as f:
            pickle.dump(data, f)
    elif mode == 'rb':
        with open(file, mode) as f:
            data = pickle.load(f)
            return data


def user(user, pwd, mode):
    '''
    用户注册及登录
    :param user: 用户输入的用户名
    :param pwd:  用户输入的密码
    :param mode: 注册还是登录
    :return: 登录成功，返回用户信息；登录失败，返回 None
    '''
    db_file = user + '.db'
    # 用户注册
    if mode == 'regist':
        if not os.path.isfile(db_file):
            user_info = {'name': user, 'passwd': pwd, 'stat': 0}
            file_oper(db_file, 'wb', user_info)
            print('\033[32;1m注册成功.\033[0m')
        else:
            print('\033[31;1m错误：该用户已存在.\033[0m')
    # 用户登录
    elif mode == 'login':
        if os.path.isfile(db_file):
            dict_user = file_oper(db_file, 'rb')
            if dict_user['name'] == user and dict_user['passwd'] == pwd:
                print('\033[32;1m登录成功.\033[0m')
                return dict_user
            else:
                print('\033[31;1m错误：用户名密码错误。\033[0m')
        else:
            print('\033[31;1m错误：该用户不存在.\033[0m')


def shopping(user_dict, list_goods):
    '''
    用户购物信息
    :param user_dict: 用户信息
    :param list_goods: 商品列表
    '''

    # 判断购物车内是否有商品
    if user_dict['shopping_car']:
        list_shopping = user_dict['shopping_car']
    else:
        list_shopping = []
    while True:
        print('\033[32;1m商品列表\033[0m'.center(50, '#'))
        for i, k in enumerate(list_goods):
            print('序号：%s\t商品名：%s\t\t价格：%s' % (i, k['name'], k['price']))
        choice = input('\033[34;1m购买请输入商品序号[t 查看购物清单 q 退出]：\033[0m').strip()
        if not choice: continue
        # 用户输入大小写 'q' 都是退出
        if choice.upper() == 'Q':
            break
        # 购买商品必须输入商品范围类的数字
        if choice.isdigit() and 0 <= int(choice) < len(list_goods):
            num = input('\033[34;1m输入购买的数量：\033[0m').strip()
            if num.isdigit():
                num = int(num)
            else:
                print('\033[31;1m错误：数量必须是正整数.\033[0m')

            # 获取用户输入的商品信息，并生成商品字典
            good = {'name': list_goods[int(choice)]['name'], 'num': num,
                    'total_prices': list_goods[int(choice)]['price'] * num}
            # 获取用户的余额
            money = user_dict['money']
            # 用户的余额 - 商品的总价
            res_money = money - good['total_prices']
            if res_money >= 0:
                # 这里目前没有想到好的处理办法，只能使用标记来做判断
                # 默认 flag 为 True，因为用户一次只能购买一件商品，如果用户购买的是重复的商品，就将购买过的商品信息合并，
                # 然后将 flag 设置为 False
                flag = True
                for i in list_shopping:
                    if good['name'] == i['name']:
                        i['num'] += good['num']
                        i['total_prices'] += good['total_prices']
                        flag = False
                # 当flag = True 说明用户没有购买重复的商品，添加新商品到购物清单；反之则购买了重复的商品 flag = False
                if flag:
                    list_shopping.append(good)
                print('\033[32;1m购买成功！\033[0m\n')
                print('\033[32;1m购物清单\033[0m'.center(50, '#'))
                for i in list_shopping:
                    print('商品名：%s\t数量：%s\t总价：%d元' % (i['name'], i['num'], i['total_prices']))
                print('\033[33;1m您的余额为：%d元\033[0m' % res_money)
                print('##########################################\n')
                # 修改购物后的用户余额信息
                user_dict['money'] = res_money
                # 修改购物清单信息
                user_dict['shopping_car'] = list_shopping
                # 将修改后的数据写入数据文件
                file_oper(user_dict['name'] + '.db', 'wb', user_dict)
            else:
                print('\033[31;1m错误：商品总价为：%d元，您的余额为：%d元，购物失败.\033[0m' % (good['total_prices'], money))

        elif choice.upper() == 'T':
            print('\033[32;1m购物清单\033[0m'.center(50, '#'))
            for i in list_shopping:
                print('商品名：%s\t数量：%s\t总价：%d元' % (i['name'], i['num'], i['total_prices']))
            print('\033[33;1m您的余额为：%d元\033[0m' % user_dict['money'])
            print('##########################################\n')
            any = input('\033[34;1m任意键返回商品列表\033[0m').strip()
            continue
        else:
            print('\033[31;1m错误：输入商品序号错误。\033[0m')


def start(list_goods):
    while True:
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
                # 当 user(username, password, 'login') 返回 None表示登录失败
                if user_dict is None:
                    continue
                # user_dict['stat'] = 0 表示用户第一次登录，user_dict['stat'] 非零则表示用户多次登录
                if user_dict['stat'] == 0:
                    money = input('\033[34;1m首次登录，请输入充值金额：\033[0m').strip()
                    if money.isdigit():  # 这里无法判断小数类型
                        user_dict['money'] = int(money)
                        # 第一次登录设置成功金额后，将 stat 设置为非零
                        user_dict['stat'] = 1
                        user_dict['shopping_car'] = []
                        print('\033[32;1m恭喜：充值成功!\033[0m')
                        shopping(user_dict, list_goods)

                    else:
                        print('\033[31;1m错误：金额只能是正整数！\033[0m')
                # user_dict['stat'] = 0 表示用户第一次登录，user_dict['stat'] 非零则表示用户多次登录
                else:
                    shopping(user_dict, list_goods)
            elif choice == '3':
                break
        else:
            print('\033[31;1m错误：序号输入错误.\033[0m')


if __name__ == '__main__':
    # 商品列表
    list_goods = [
        {'name': '苹果', 'price': 10},
        {'name': '鸭梨', 'price': 20},
        {'name': '芒果', 'price': 30},
    ]

    start(list_goods)









