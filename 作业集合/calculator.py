# -*- coding: utf-8 -*-
# Author: hkey

import re


def check_exp(cal_str):
    '''
    检查用户输入的表达式是否正确
    :param cal_str: 用户输入的表达式
    :return: 返回bool值，True 表达式正确，False 表达式错误，重新输入
    '''
    char_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '+', '-', '*', '/', '%', '//', '.', '**', '(', ')'}
    # 判断用户输入的表达式是否是 char_set 子集
    if set(cal_str) <= char_set:
        # 用户输入的表达式如果以 '*' '/' '%' ')' 开始，则返回 False
        if cal_str.startswith('*') or cal_str.startswith('/') or cal_str.startswith('%') \
                or cal_str.startswith(')'):
            print('\33[31;1m输入的表达式不正确，请重新输入!\33[0m')
            return False
        # 用户输入的表达式如果以 '+ - * / (' 结尾，则返回 False
        elif cal_str.endswith('+') or cal_str.endswith('-') or cal_str.endswith('*') \
                or cal_str.endswith('/') or cal_str.endswith('('):
            print('\33[31;1m输入的表达式不正确，请重新输入!\33[0m')
            return False
        # 用户输入的表达式如果包含 '.. +* +/ +% -* -/ -%' 结尾，则返回 False
        elif '..' in cal_str or '+*' in cal_str or '+/' in cal_str or '+%' in cal_str \
                or '-*' in cal_str or '-/' in cal_str or '-%' in cal_str:
            print('\33[31;1m输入的表达式不正确，请重新输入!\33[0m')
            return False
        else:
            return True


def simple_exp(cal_str):
    '''
    简化用户输入的表达式
    :param cal_str: 用户输入的表达式
    :return: 简化后的表达式
    '''
    # 初始化一个替换字符列表
    replace_char_list = [('+-', '-'), ('-+', '-'), ('++', '+'), ('--', '+'), ('*+', '*'),
                         ('/+', '/'), ('%+', '%'), ('//+', '//'), ('**+', '**')]
    flag = False  # 初始化标识符
    count = 0  # 初始化不匹配次数

    while not flag:
        for i in replace_char_list:
            # 如果要简化的字符串在用户输入的表达式中
            if i[0] in cal_str:
                # 把需要替换的字符串，替换为最简模式
                cal_str = cal_str.replace(i[0], i[1])
                # 这边 break是为了计算 count的结果等于 len(replace_char_list)
                break
            else:
                count += 1
            # 当 count 等于 len(replace_char_list)时，即没有需要替换的字符了，退出循环
            if count == len(replace_char_list):
                flag = True
        # 如果用户输入的表达式以 '+' 开头，就去掉 '+'
        if cal_str.startswith('+'):
            cal_str = cal_str[1:]
    # 返回检查后最简表达式
    return cal_str


def power(exp):
    '''
    匹配幂运算并计算结果
    :param exp: 去掉括号后的表达式
    :return: 返回计算后的幂运算值并替换幂运算表达式
    '''
    # print('power:', exp)
    match = re.search('\d+\.?\d*[\*]{2}[\+\-]*\d+\.?\d*', exp)  # 匹配幂运算表达式
    if match:  # 匹配到幂运算
        content = match.group()  # 获取匹配到的幂运算表达式
        if len(content.split('**')) > 1:
            n1, n2 = content.split('**')  # 获取幂运算数字
            value = float(n1) ** float(n2)
            exp = exp.replace(content, str(value))  # 替换幂运算表达式为计算后的值
            exp = simple_exp(exp)  # 检查替换括号后，是否存在类似'+-'等字符，如果存在，先检查替换
            return power(exp)  # 递归计算幂运算表达式
        else:
            pass
    else:
        return exp  # 没有匹配到幂运算直接返回表达式


def mul_div(exp):
    # print('mul_div:', exp)
    # match = re.search('\d+\.?\d*[\*\/\/\/%]+[\+\-]?\d+\.?\d*', exp)
    match = re.search('\d+\.?\d*[\*\/%\/\/]+[\+\-]?\d+\.?\d*', exp)
    if match:
        content = match.group()  # 获取匹配到的表达式
        if len(content.split('*')) > 1:
            n1, n2 = content.split('*')
            value = float(n1) * float(n2)  # 乘法运算
            exp = exp.replace(content, str(value))  # 用计算的结果替换计算的表达式
            exp = simple_exp(exp)  # 检查计算后的结果是否存在 '+-' 等字符，存在的话先替换，在执行
            return mul_div(exp)  # 递归检查处理
        elif len(content.split('/')) > 1:
            n1, n2 = content.split('/')
            value = float(n1) / float(n2)  # 除法运算
            exp = exp.replace(content, str(value))  # 用计算的结果替换计算的表达式
            exp = simple_exp(exp)  # 检查计算后的结果是否存在 '+-' 等字符，存在的话先替换，在执行
            return mul_div(exp)  # 递归检查处理
        elif len(content.split('//')) > 1:
            n1, n2 = content.split('//')
            value = float(n1) // float(n2)  # 取整运算
            exp = exp.replace(content, str(value))  # 用计算的结果替换计算的表达式
            exp = simple_exp(exp)  # 检查计算后的结果是否存在 '+-' 等字符，存在的话先替换，在执行
            return mul_div(exp)  # 递归检查处理
        elif len(content.split('%')) > 1:
            n1, n2 = content.split('%')
            value = float(n1) % float(n2)  # 取余运算
            exp = exp.replace(content, str(value))  # 用计算的结果替换计算的表达式
            exp = simple_exp(exp)  # 检查计算后的结果是否存在 '+-' 等字符，存在的话先替换，在执行
            return mul_div(exp)  # 递归检查处理
    else:
        return exp  # 不匹配返回表达式


def add_sub(exp):
    # print('add_sub:', exp)
    match = re.search('\d+\.?\d*[\+\-]+\d+\.?\d*', exp)  # 从前往后匹配第一个 '+ -'的表达式
    print(match)
    if match:
        content = match.group()  # 获取匹配到的表达式
        if len(content.split('+')) > 1:
            n1, n2 = content.split('+')
            value = float(n1) + float(n2)  # 计算加法
            exp = exp.replace(content, str(value))  # 计算后的值替换表达式
            print('exp', exp)
            exp = simple_exp(exp)  # 检查表达式是否存在'+-'等字符
            return add_sub(exp)  # 递归计算
        elif len(content.split('-')) > 1:
            if len(content.split('-')) == 3:  # 如果用减法分隔出三个元素，表达式如：'-2-3'
                n1, n2 = content.split('-')[1:]  # 第一个元素为空，从索引为 1 开始取值
                value = float('-' + n1) - float(n2)  # 计算表达式，如 -2-3=-5
                exp = exp.replace(content, str(value))  # 计算后的值替换表达式
                exp = simple_exp(exp)  # 检查表达式是否存在'+-'等字符
                return add_sub(exp)  # 递归计算
            elif len(content.split('-')) == 2:
                n1, n2 = content.split('-')
                value = float(n1) - float(n2)  # 计算表达式，如 4-3=1
                exp = exp.replace(content, str(value))  # 用计算的结果替换计算的表达式
                exp = simple_exp(exp)  # 检查计算后的结果是否存在 '+-' 等字符，存在的话先替换，在执行
                return add_sub(exp)  # 递归检查处理
    else:
        return exp


def calculate(exp):
    '''
    获取一个运算表达式，返回运算结果
    :param exp: 表达式
    :return: 运算结果
    '''
    result = power(exp)         # 执行幂运算，返回运算结果
    result = mul_div(result)    # 执行乘法、除法、取余、取整运算，返回运算结果
    result = add_sub(result)    # 执行加法、减法运算，返回运算结果
    # print('calculate', result)
    return result


def parenthesis(exp):
    '''
    递归函数，递归计算括号中的内容并替换掉括号，直到返回表达式计算结果
    :param exp: 检查后的最简表达式
    :return: 返回表达式最终计算结果
    '''
    # 匹配表达式最里面括号内容
    match = re.search('\([^()]+\)', exp)
    if match:
        # 如果获取到括号里的内容，过去掉括号，获取计算表达式
        content = match.group()[1:-1]
        # 计算括号中的内容并返回计算结果
        result = calculate(content)
        print('计算前的表达式：\33[32;1m%s\33[0m' % exp)
        print('括号中的计算结果：\33[32;1m%s=%s\33[0m' % (content, result))
        replace_content = '(' + content + ')'
        # 替换括号中的内容，将表达式中的括号替换成计算结果
        exp.replace(replace_content, str(result))
        # 检查替换括号后，是否存在类似'+-'等字符，如果存在，先检查替换
        exp = simple_exp(exp)
        print('计算后的表达式：\33[32;1m%s\33[0m' % exp)
        # 递归计算括号中的内容，直到替换所有括号中的内容
        parenthesis(exp)

    else:
        # 当表达式没有括号时，直接计算出结果
        result = calculate(exp)
        print('result', result)
        print('表达式运算结果：\33[32;1m%s\33[0m' % result)


if __name__ == '__main__':
    print('\33[32;1m欢迎使用计算器\33[0m'.center(30, '#'))
    while True:
        cal_str = input('请输入表达式（q退出）:').strip()
        cal_str = ''.join(re.split('\s+', cal_str))
        if not cal_str: continue
        if cal_str == 'q':
            print('\33[35;1m程序退出。\33[0m')
            break
        if check_exp(cal_str):
            # exp = 简化用户输入后的表达式
            exp = simple_exp(cal_str)
            print('------------', exp)
            print('\33[32;1m简化后的表达式：%s\33[0m' % exp)
            parenthesis(exp)

