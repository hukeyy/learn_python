# -*- coding: utf-8 -*-
# Author: hkey
import re


def check_exp(get_input):
    '''
    检查表达式中的字符是否存在不合法性，合法返回真，不合法返回假
    :param get_input: 用户输入的表达式，待检测的表达式
    :return: 返回真或者假
    '''
    char_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '+', '-', '*', '/', '(', ')', '**', '%', '//', '.', }  # 有效表达式的字符集合
    # 判断用户输入的表达式字符是否是char_set的子集，如果是则为真，否则为假
    if set(get_input) <= char_set:
        # 如果表达式以 '*, /, %, )'开头，则为假
        if get_input.startswith('*') or get_input.startswith('/') or get_input.startswith('%') \
                or get_input.startswith(')'):
            print('\33[31;1m输入的表达式有误，请重新输入\33[0m')
            return False
        # 如果表达式以 '+, -, *, /, ('结尾，则为假
        elif get_input.endswith('+') or get_input.endswith('-') or get_input.endswith('*') \
                or get_input.endswith('/') or get_input.endswith('('):
            print('\33[31;1m输入的表达式有误，请重新输入\33[0m')
            return False
        # 如果表达式中含有 '.., +/, +/, -*, -/, -%'，则为假
        elif '..' in get_input or '+*' in get_input or '+/' in get_input or '+%' in get_input \
                or '-*' in get_input or '-/' in get_input or '-%' in get_input:
            print('\33[31;1m输入的表达式有误，请重新输入\33[0m')
            return False
        else:
            return True
    else:
        print('\33[31;1m表达式中包含其他字符，无法进行计算，请重新输入\33[0m')
        return False


def simple_exp(exp):
    # 初始化一个替换字符列表
    replace_char_list = [('+-', '-'), ('-+', '-'), ('++', '+'), ('--', '+'), ('*+', '*'),
                         ('/+', '/'), ('%+', '%'), ('//+', '//'), ('**+', '**')]
    flag = False  # 初始化标识符
    count = 0  # 初始化不匹配次数
    while not flag:  # 使用 flag循环的目的是为了避免出现 '1+++3'这样情况
        for i in replace_char_list:
            if i[0] in exp:  # 要简化的字符在表达式中
                exp = exp.replace(i[0], i[1])  # 替换需要简化的字符
                break  # 中断for循环，进行下一次while循环，
            else:
                count += 1
            if len(replace_char_list) == count:
                flag = True

        if exp.startswith('+'):
            exp = exp[1:]
    return exp

def power(exp):
    match = re.search('[\+\-]*\d*\.?\d*[\*]{2}[\+\-]*\d*\.?\d*', exp)
    if match:
        pass
    else:
        return exp

def mul_div(exp):
    pass

def add_sub(exp):
    pass


def calculate(exp):
    '''
    获取一个表达式，返回计算结果
    :param exp: 表达式
    :return: 运算结果
    '''
    result = power(exp)
    result = mul_div(result)
    result = add_sub(result)
    return result

def parenthesis(exp):
    '''
    匹配括号内的表达式并计算结果，将结果替换括号中的内容，最终返回计算结果
    :param exp: 字符检查替换后最简的表达式
    :return: 表达式最终计算结果
    '''
    match = re.search('\([^()]+\)', exp)  # 匹配括号内的表达式
    # 如果取到括号内的表达式，则去除括号，计算表达式结果并替换括号的内容
    if match:
        content = match.group()[1:-1]  # 通过索引剔除表达式的括号
        result = calculate(content)  # 计算不带括号表达式的结果
        print('计算前的表达式：\33[32;1m%s\33[0m' % exp)
        print('括号中运算结果：\33[32;1m%s=%s\33[0m' % (content, result))
        result_content = '(' + content + ')'
        exp = exp.replace(result_content, str(result))  # 将计算的值替换括号表达式
        exp = simple_exp(exp)  # 检查替换括号后的表达式是否存在 '++'等字符，存在的话先替换掉
        print('计算后的表达式:\33[32;1m%s\33[0m\n' % exp)
        parenthesis(exp)  # 递归计算括号中的内容并替换
    # 如果表达式没有匹配到括号，则直接计算表达式结果
    else:
        result = calculate(exp)  # 计算表达式结果
        print('表达式运算结果：\33[32;1m%s\33[0m' % result)


if __name__ == '__main__':
    print('\33[33;1m欢迎使用计算器\33[0m'.center(30, '#'))
    while True:
        get_input = input('请输入表达式 | 退出(q) ：').strip()
        if not get_input: continue
        if get_input == 'q': break
        get_input = ''.join(re.split('\s+', get_input))
        if check_exp(get_input):
            exp = simple_exp(get_input)
            print('简化后的表达式:\33[32;1m%s\33[0m' % exp)
            parenthesis(exp)

        else:
            pass
