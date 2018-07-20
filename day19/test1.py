# -*- coding: utf-8 -*-
# Author: hkey
menu = {
    '陕西省': {
        '西安': {
            '未央区': {},
            '莲湖区': {},
            '高新区': {},
        },
        '咸阳': {
            '秦都区': {},
            '渭城区': {}
        }
    },
    '四川省': {
        '成都': {
            '锦江区': {},
            '青羊区': {},
            '金牛区': {},
        },
        '绵阳': {
            '涪城区': {},
            '游仙区': {},
        }
    }
}

def threeTL(dic):
    while True:
        for key in dic:
            print(key)
        choice = input('>>>').strip()
        if choice == 'b' or choice == 'q': return choice
        elif choice in dic and dic[choice]:
            res = threeTL(dic[choice])
        elif choice not in dic or dic[choice]:
            continue

threeTL(menu)