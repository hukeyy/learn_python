# -*- coding: utf-8 -*-
# Author: hkey
import shelve, time
LOGIN_TIME_OUT = 30
db = shelve.open('user.db', writeback=True)

def regist():
      print('\033[42;1m【注册】\033[0m')
      while True:
            name = input('\033[34;1musername:\033[0m').strip()
            if not name:continue
            if name in db:
                  print('\033[31;1m错误：该用户已存在.\033[0m')
            pwd = input('\033[34;1mpwd:\033[0m').strip()
            db[name] = {'pwd': pwd, 'last_login_time': time.time()}

def login():
      print('\033[42;1m【注册】\033[0m')
      name = input('\033[34;1musername:\033[0m').strip()
      pwd = input('\033[34;1mpwd:\033[0m').strip()
      try:
            password = db.get(name).get('password')
      except AttributeError as e:
            print('\033[32;1m错误：用户名不存在.\033[0m')
            return
      if pwd == password:
            login_time = time.time()
            last_login_time = db[name].get('last_login_time')
            if login_time - last_login_time < LOGIN_TIME_OUT:
                  print('\033[32;1m该用户已登录，上次登录时间【%s】\033[0m'
                        % time.strftime('%Y-%m-%d %X', time.localtime(last_login_time)))
                  db[name]['last_login_time'] = login_time
                  print('\033[32;1mwelcome back.\033[0m')
            else:
                  print('\033[31;1m错误\033[0m')



