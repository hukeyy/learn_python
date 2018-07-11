# -*- coding: utf-8 -*-
# Author: hkey
import random


# def v_code():
#     code = ''
#     for i in range(5):
#         num = random.randint(0, 9)
#         alf = chr(random.randint(65,90))
#         add = random.choice([num, alf])
#         code += str(add)
#     return code
#
# print(v_code())


def v_code():
    '''随机验证码'''
    ret = ''
    for i in range(5):
        ran_int = random.randint(0, 9)
        ran_str1 = chr(random.randint(65, 122))
        # ran_str2 = chr(random.randint(97, 122))
        str1 = str(random.choice([ran_int, ran_str1]))
        ret += str1
    return ret


print(v_code())
