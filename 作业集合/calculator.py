# -*- coding: utf-8 -*-
# Author: hkey

import re

def check_exp(cal_str):
    '''
    输入一个表达式，判断是否正确，返回一个去空格的表达式
    :param cal_str: 获取用户输入的表达式
    :return: 返回bool值。True通过检查，False 不符合规则
    '''
    char_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '+', '-', '*', '/', '%', '//', '**', '.', '(', ')'}
    if set(cal_str).issubset(char_set):
        if cal_str.startswith('*') or cal_str.startswith('/') or cal_str.startswith('%'):
            print('\33[31;1m输入的表达式不正确，请重新输入！\33[0m')
            return False
        elif cal_str.endswith('*') or cal_str.endswith('/') or cal_str.endswith('%') \
                or cal_str.endswith('+') or cal_str.endswith('-'):
            print('\33[31;1m输入的表达式不正确，请重新输入！\33[0m')

            return False
        elif '..' in cal_str or '+*' in cal_str or '+/' in cal_str or '+%' in cal_str \
            or '-*' in cal_str or '-/' in cal_str or '-%' in cal_str:
            print('\33[31;1m输入的表达式不正确，请重新输入！\33[0m')
            return False
        else:
            return True
    else:
        print('\33[31;1m输入的表达式包含其他字符，无法进行计算，请重新输入！\33[0m')
        return False

def replace_symbol(exp):
    replace_char_list = [('+-', '-'), ('-+', '-'), ('++', '+'), ('--', '+'), ('*+', '*'),
                         ('/+', '/'), ('%+', '%'), ('//+', '//'), ('**+', '**')]

    flag = False
    count = 0
    while not flag:
        for i in replace_char_list:
            if i[0] in exp:
                exp = exp.repalce(i[0], i[1])
                # break
            else:
                count += 1
            if count == len(replace_char_list):
                pass




if __name__ == '__main__':
    print('\33[32;1m欢迎使用计算器\33[0m'.center(30, '#'))
    while True:
        cal_str = input('请输入一个表达式：').strip()
        cal_str = ''.join(re.split('\s+', cal_str))

        if not cal_str: continue
        elif cal_str == 'q':
            print('退出程序！')
        elif check_exp(cal_str):
            pass
        else:
            print('bad')




