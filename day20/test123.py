# -*- coding: utf-8 -*-
# Author: hkey

import time
last_login_time = time.time()
print('\033[32;1m该用户已登录，登录时间[%s]' % time.strftime('%Y-%m-%d %X', time.localtime(last_login_time)))