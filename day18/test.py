# -*- coding: utf-8 -*-
# Author: hkey

# char_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
#             '+', '-', '*', '/', '%', '//', '**', '.', '(', ')'}

# print(char_set, type(char_set))

# str1 = 'hello world'
#
# str2 = str1.replace('l', 'A')
# print(str2)


# a = {'a', 'b', 'c', 'd'}
#
# b = {'d', 'a', 'c'}
#
# print( b <= a)
# from collections import Iterable
# import re
# str1 = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
# str2 = re.search('\([^()]+\)', str1)

# import re
# # str1 = '123.1-123.12'
# # print(str1.split('-'))
# exp = '3.0'
# match = re.search('\d+\.?\d*[\+\-]+\d+\.?\d*', exp)
# print(match)

# print(eval('3*( -4+ 50 )-(( 100 + 40 )*5/2- 3*2* 2/4+9)*((( 3 + 4)-4)-4)'))
# import re
# exp = '3*( 4+ 50 )-(( 100 + 40 )*5/2- 3*2* 2/4+9)*((( 3 + 4)-4)-4)'
# exp = ''.join(re.split('\s+', exp))
# print(re.search('\([^()]+\)', exp).group()[1:-1])

import re

# exp = '-1+20'
# match = re.search('\-?\d+\.?\d*(\+|\-)\d+\.?\d*', exp)
# print(match.group())
# content = match.group()
# n1, n2 = content.split('-')[1:]
# print(float('-' + n1) -  float(n2))

str1 = '  1      +     2    '

str2 = str1.replace(' ', '')
print(str2)






























