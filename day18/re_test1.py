# -*- coding: utf-8 -*-
# Author: hkey

import re

#
str1 = '1 - 2 * ( ( 6 0 -3 0  +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
#
# print(re.findall('[\d+]|\+|-|\*|/', str1))

ret = re.split('\s+', str1)
print(''.join(ret))









