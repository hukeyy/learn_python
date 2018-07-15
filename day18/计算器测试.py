# -*- coding: utf-8 -*-
# Author: hkey
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Version:Python3.5.0
import re

def check_exp(get_input):
    '''
    输入一个表达式，判断是否正确，返回一个去空格的表达式
    :param get_input: 获取的表达式
    :return: 返回一个去空格的表达式
    '''
    char_set = set(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                    '+', '-', '*', '/', '%', '//', '**', '.', '(', ')'))     # 有效表达式的字符集合
    # 判断输入的字符合法,输入的表达式字符属于全集char_set为真
    if set(get_input).issubset(char_set):
        # 输入的表达式是乘号'*'、除号'/'，百分号'%' 开头的，不合法
        if get_input.startswith('*') or get_input.startswith('/') or get_input.startswith('%'):
            print('\033[31;1m输入的表达式不正确，请重新输入！\033[0m')
            return False
        # 输入的表达式是乘号'*'、除号'/'，百分号'%'、加号'+'、减号'-' 结尾的，不合法
        elif (get_input.endswith('*') or get_input.endswith('/') or get_input.endswith('%')
                or get_input.endswith('+') or get_input.endswith('-')):
            print('\033[31;1m输入的表达式不正确，请重新输入！\033[0m')
            return False
        # 输入的表达式中，有两个点号或者加减号后面跟着乘除百分号的，不合法
        elif ('..' in get_input or '+*' in get_input or '+/' in get_input or '+%' in get_input
                or '-*' in get_input or '-/' in get_input or '-%' in get_input):
            print('\033[31;1m输入的表达式不正确，请重新输入！\033[0m')
            return False
        else:
            return True
    else:
        print('\033[31;1m输入的表达式包涵其他字符，无法进行计算，请重新输入！\033[0m')
        return False

def replace_symbol(exp):
    '''
    化简表达式，比如“++-”转换成“-"，返回最简表达式
    :param exp: 需要化简的表达式
    :return:    化简后的表达式
    '''
    # 初始化一个替换字符的列表
    replace_char_list = [('+-', '-'), ('-+', '-'), ('++', '+'), ('--', '+'), ('*+', '*'),
                        ('/+', '/'), ('%+', '%'), ('//+', '//'), ('**+', '**')]
    flag = False    # 初始化标识符
    count = 0       # 初始化不匹配次数
    while not flag:
        for i in replace_char_list:
            if i[0] in exp:    # 要化简的字符在表达式中，则直接替换
                exp = exp.replace(i[0], i[1])   # 把需要替换的键字符串修改为其值的字符串
                break     # 中断for循环，进行下一次while循环
            else:
                count += 1
            # 当count等于 len(replace_char_list)时，即 没有需要替换的字符了，退出循环
            if count == len(replace_char_list):
                flag = True

        if exp.startswith('+'):
            exp = exp[1:]   # 除去表达式中开头的加号
    return exp

def parenthesis(exp):
    '''
    运算括号里面的表达式，运算结果替代括号的内容，返回运算结果
    :param exp: 计算的表达式
    :return: None
    '''
    match = re.search('\(([\+\-\*\/%\/\/\*\*]*\d+\.*\d*){2,}\)', exp)  # 匹配括号内的表达式
    if match:   # 找到匹配的字符
        content = match.group()[1:-1]     # 获取匹配到的表达式,并过滤括号
        result = calculate(content)     # 调用计算函数，返回结束结果
        print('计算前的表达式：\033[32;1m%s\033[0m' % exp)
        print('括号中运算结果：\033[33;1m%s=%s\033[0m' % (content, result))
        replace_content = '(' + content + ')'
        exp = exp.replace(replace_content, result)      # 把运算结果替换表达式
        exp = replace_symbol(exp)   # 检查计算后的表达式是否存在类似 '+- '等字符，存在的话先替换，后执行
        print('计算后的表达式：\033[34;1m%s\033[0m\n' % exp)
        parenthesis(exp)     # 递归执行括号处理
    else:
        result = calculate(exp)  # 当表达式没有括号时，直接计算表达式结果
        print('表达式运算结果：\033[35;1m%s\033[0m' % result)

def power(exp):
    '''
    幂运算，返回运算结果
    :param exp: 幂运算的表达式
    :return: 计算后的表达式
    '''
    match = re.search('\d+\.?\d*[\*]{2}[\+\-]*\d+\.?\d*', exp)  # 匹配幂运算
    if match:   # 找到匹配的字符
        content = match.group()     # 获取匹配到的表达式
        if len(content.split('**')) > 1:
            n1, n2 = content.split('**')
            value = float(n1) ** float(n2)
            exp = exp.replace(content, str(value))   # 用计算的结果替换计算的表达式
            exp = replace_symbol(exp)   # 检查计算后的表达式是否存在类似 '+- '等字符，存在的话先替换，后执行
            return power(exp)      # 递归重复匹配
        else:
            pass
    else:
        return exp  # 不匹配到，返回exp

def mul_div(exp):
    '''
    做乘法、除法、取余、取整运算，返回运算结果
    :param exp: 乘法、除法、取余、取整运算的表达式
    :return: 计算后的表达式
    '''
    match = re.search('\d+\.?\d*[\*\/%\/\/]+[\+\-]?\d+\.?\d*', exp)  # 匹配乘、除、取余、取整运算
    if match:   # 找到匹配的字符
        content = match.group()     # 获取匹配到的表达式
        if len(content.split('*')) > 1:
            n1, n2 = content.split('*')
            value = float(n1) * float(n2)   # 乘法运算
            exp = exp.replace(content, str(value))   # 用计算的结果替换计算的表达式
            exp = replace_symbol(exp)   # 检查计算后的表达式是否存在类似 '+- '等字符，存在的话先替换，后执行
            return mul_div(exp)

        elif len(content.split('//')) > 1:
            n1, n2 = content.split('//')     # 取余运算
            value = float(n1) // float(n2)
            exp = exp.replace(content, str(value))   # 用计算的结果替换计算的表达式
            exp = replace_symbol(exp)   # 检查计算后的表达式是否存在类似 '+- '等字符，存在的话先替换，后执行
            return mul_div(exp)

        elif len(content.split('%')) > 1:
            n1, n2 = content.split('%')     # 除法运算
            value = float(n1) % float(n2)
            exp = exp.replace(content, str(value))   # 用计算的结果替换计算的表达式
            exp = replace_symbol(exp)   # 检查计算后的表达式是否存在类似 '+- '等字符，存在的话先替换，后执行
            return mul_div(exp)

        elif len(content.split('/')) > 1:
            n1, n2 = content.split('/')    # 取整运算
            value = float(n1) / float(n2)
            exp = exp.replace(content, str(value))   # 用计算的结果替换计算的表达式
            exp = replace_symbol(exp)   # 检查计算后的表达式是否存在类似 '+- '等字符，存在的话先替换，后执行
            return mul_div(exp)

        else:
            pass
    else:
        return exp  # 不匹配到，返回exp

def add_sub(exp):
    '''
    加法、减法运算，返回运算结果
    :param exp: 加法、减法运算的表达式
    :return: 计算后的表达式
    '''
    match = re.search('\-?\d+\.?\d*[\+\-]+\d+\.?\d*', exp)  # 匹配加法、减法
    if match:   # 找到匹配的字符
        content = match.group()     # 获取匹配到的表达式
        if len(content.split('+')) > 1:
            n1, n2 = content.split('+')
            value = float(n1) + float(n2)
            exp = exp.replace(content, str(value))   # 用计算的结果替换计算的表达式
            exp = replace_symbol(exp)   # 检查计算后的表达式是否存在类似 '+- '等字符，存在的话先替换，后执行
            return add_sub(exp)

        elif len(content.split('-')) > 1:
            if len(content.split('-')) == 3:    # 被减数是负数的情况
                n1, n2 = content.split('-')[1:]     #  过滤分割列表开头的空白字符串
                value = float('-' + n1) - float(n2)   # 被减数需要添加一个负号
                exp = exp.replace(content, str(value))   # 用计算的结果替换计算的表达式
                exp = replace_symbol(exp)   # 检查计算后的表达式是否存在类似 '+- '等字符，存在的话先替换，后执行
                return add_sub(exp)
            elif len(content.split('-')) == 2:    # 被减数是正数的情况
                n1, n2 = content.split('-')     #  直接把两个操作数赋值给对应的变量
                value = float(n1) - float(n2)   # 做减法运算
                exp = exp.replace(content, str(value))   # 用计算的结果替换计算的表达式
                exp = replace_symbol(exp)   # 检查计算后的表达式是否存在类似 '+- '等字符，存在的话先替换，后执行
                return add_sub(exp)
            else:
                pass
        else:
            pass
    else:
        return exp  # 不匹配到，返回exp

def calculate(exp):
    '''
    获取一个运算表达式，返回运算结果
    :param exp: 表达式
    :return: 运算结果
    '''
    result = power(exp)         # 执行幂运算，返回运算结果
    result = mul_div(result)    # 执行乘法、除法、取余、取整运算，返回运算结果
    result = add_sub(result)    # 执行加法、减法运算，返回运算结果
    return result

if __name__ == '__main__':
    print('\033[31;1m欢迎使用计算器\033[0m'.center(100,'='))
    while True:
        # 计算 s = '1-2 *(   (60- 30+(-40.0/5)*(9-2*5 / 3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
        get_input = input('\n\033[32;1m请输入一个表达式 | 退出（q）： \033[0m').strip()
        get_input = ''.join(re.split('\s+', get_input))    # 除去输入表达式中多余的空格
        if get_input == '':     # 空字符，重新输入
            continue
        elif get_input == 'q':
            print('\033[31;1m退出程序!\033[0m')
            break
        elif check_exp(get_input):    # 输入的表达式合法
            exp = replace_symbol(get_input)     # 化简输入的表达式
            print('化简后的表达式：\033[33;1m%s\033[0m\n' % exp)
            parenthesis(exp)
        else:
            pass

