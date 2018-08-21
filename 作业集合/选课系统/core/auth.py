# -*- coding: utf-8 -*-
# Author: hkey
import pickle


class Auth(object):
    def __init__(self, user, passwd, kind):
        self.user = user
        self.passwd = passwd
        self.kind = kind

    def is_auth(self, user_db_file):
        with open(user_db_file, 'rb') as f:
            user_info = pickle.load(f)
        if self.kind == user_info['kind'] and self.user == user_info['username'] and self.passwd == user_info['passwd']:
            return True
        else:
            return False
