#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import re
s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'


def wipe(s):
    '''
    根据数学运算，去除重复的运算符号
    :param s: 只剩下加减运算的表达式
    :return: 去除多余的表达式符号
    '''
    res = s.replace('+-', '-').replace('-+', '-').replace('++', '+').replace('--', '+') # 通过replace进行替换
    return res


def get(s):
    '''
    去除原始表达式中的空格，并通过re.split以最内层括号第一个分隔为三个元素，最内层括号第一个表达式的索引为 1
    :param s: 最原始的运算表达式
    :return: 返回list，其中其中索引为1的元素就是最内层括号第一个首先要计算的表达式
    '''
    no_space_exp = re.sub(' ', '', s)   # re.sub 去除表达式中的空格符
    res = re.split("(\([^()]+\))", no_space_exp, 1) # 分解成列表且索引为1的元素即第一个要计算的表达式
    return res


def add_num(s):
    '''
    加减运算
    :param s: 去括号后的计算表达式
    :return: 加减表达式计算后的结果值
    '''
    s = wipe(s) # 进行加减运算的时候，去除掉多余的符号
    list_num = re.findall("([+-]?\d+\.?\d*)", s)    # 查找表达式中的每个具体的数字
    k = 0
    for i in list_num:
        k += float(i)   # 进行累加操作
    return k


def mul(s):
    '''
    乘除算法，如果表示不存在乘除运算就返回到加减函数中
    :param s: 括号中要计算的表达式
    :return: 加减函数
    '''
    while True:
        res = re.split("(\d+\.?\d*[*/][+-]?\d+\.?\d*)", s, 1)   # 获取括号内的计算表达式
        if len(res) == 3 and '*' in res[1]: # 判断计算表达式是否是乘法计算
            a, b, c = res
            d, e = b.split('*')
            res_b = float(d) * float(e) # 进行乘法计算
            s = a + str(res_b) + c  # 括号内计算的结果替换掉带括号的表达式
        elif len(res) == 3 and '/' in res[1]:   # 判断计算表达式是否是除法计算
            a, b, c = res
            d, e = b.split('/')
            res_b = float(d) / float(e) # 进行除法计算
            s = a + str(res_b) + c  # 括号内计算的结果替换掉带括号的表达式
        else:
            return add_num(s)   # 如果表达式不存在乘法和除法，则进行加减运算


def counter(s):
    '''
    循环计算括号中的表达式，并将计算结果替换原始表达式括号的内容
    :param s: 传入要计算的原始表达式
    :return: 当所有的括号计算完成并替换完毕后，在进行最后的计算并得到最终结果
    '''
    while True:
        res = get(s)
        if len(res) == 3:
            a, b, c = res
            res_b = mul(b)
            s = a + str(res_b) + c
        else:
            return mul(s)


print(counter(s))
















