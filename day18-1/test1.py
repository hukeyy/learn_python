#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import re
def wipe(s): #定义去除重复+-号函数
    res=s.replace("+-","-").replace("++","+").replace("--","+").replace("-+","-")
    return res

def get(s):#定义取括号内运算式函数
    res=re.sub(" ","",s)#去除字符之间的空格
    res1 = re.split("\(([^()]+)\)", res,1)#取最里面的括号的运算式
    return res1

def add_num(s):#定义加减运算函数
    s=wipe(s)#进行加减法运算前执行去重+-号
    num = re.findall("([+\-]?\d+\.?\d*)", s)#取到所有数字的列表num
    k=0
    for i in num:
        k+=float(i)
    return k    #进行循环相加减并返回最后值

def mul(s):#定义乘除法运算
    while True:
        res=re.split("(\d+\.?\d*[\*/][\+-]?\d+\.?\d*)", s,1) #将整个运算式以最里面的运算式为中间部分分成三个元素的列表
        if len(res)==3 and "*"in res[1]:#判断列表元素是否为三个以及*号是否在最中间运算式里
            a,b,c=res#分别取到列表里的元素的值
            d,e=b.split("*")#将最里面的运算式以*进行分割取到两边的值
            res_s=float(d)*float(e)#将两边的值进行运算
            s = a+str(res_s)+c#将结果替换原来的运算式
        elif len(res)==3 and "/"in res[1]:#判断列表元素是否为三个以及/号是否在最中间运算式里
            a,b,c=res
            d,e= b.split("/")#将最里面的运算式以/进行分割取到两边的值
            res_s=float(d)/float(e)
            s=a+str(res_s)+c
        else:#如果列表元素小于三直接进行加减法运算
            return add_num(s)

def counter(s):  #定义计算器函数
    while True:
        res=get(s)#进行取值并判断
        if len(res)==3:#如果取到的值的列表元素是三进行乘除运算
            a,b,c=res
            result=mul(b)
            s = a + str(result) + c#将最后的乘除运算结果替换原来的运算式
        else:
            return mul(s) #如果列表元素小于三直接进行加减法运算

a="1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
print(counter(a))