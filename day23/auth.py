# -*- coding: utf-8 -*-
# Author: hkey
import pickle


def file_oper(file, mode, *args):
    if mode == 'wb':
        with open(file, mode) as f:
            data_dict = args[0]
            pickle.dump(data_dict, f)
    elif mode == 'rb':
        with open(file, mode) as f:
            data = pickle.load(f)
            return data


class UserInfo(object):
    def __init__(self, name, passwd, kind):
        self.name = name
        self.passwd = passwd
        self.kind = kind

    def regist(self):
        user_dict = {'name': self.name, 'passwd': self.passwd, 'kind': self.kind}
        if self.kind == '学生':
            file_dict = file_oper('student_dict', 'rb')
            print(type(file_dict))
            # file_dict.add(user_dict)
            # file_oper('student_dict', 'wb', file_dict)

def init_user():
    set_info = set([])
    dict_data = {'name': 'hkey', 'passwd': '123', 'kind': '学生'}
    set_info.add(dict_data)
    file_oper('student_dict', 'wb', set_info)

if __name__ == '__main__':
    init_user()
    name = input('用户名：')
    passwd = input('密码：')
    kind = input('种类：')
    user = UserInfo(name, passwd, kind)
    user.regist()
