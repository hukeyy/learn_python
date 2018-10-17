#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

def treeML(dic):
    while True:
        for i in dic:
            print(i)
        key = input('>>>').strip()
        if key == 'b' or key == 'q':
            return key
        elif key in dic:
            res = treeML(dic[key])
            if res == 'q':
                return 'q'

treeML(menu)






