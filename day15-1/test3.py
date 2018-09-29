#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import pickle


def modify_money(user_file, money):
    with open(user_file, 'rb') as read_f:
        user_db = pickle.load(read_f)
        user_db['money'] = money
        print(user_db)
    with open(user_file, 'wb') as write_f:
        pickle.dump(user_db, write_f)

modify_money('jay.db', 2000)

# with open('hkey.db', 'rb') as f:
#     data = pickle.load(f)
# data['money'] = 10000
# print(data)