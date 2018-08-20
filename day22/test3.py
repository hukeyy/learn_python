# -*- coding: utf-8 -*-
# Author: hkey

class Teacher(object):
    def __init__(self, name, course, birthday, role='讲师'):
        self.name = name
        self.course = course
        self.birthday = birthday
        self.role = role


class Birthday(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


b = Birthday(2000, 12, 12)
t = Teacher('jay', 'music', b)

print(t.birthday.year)
print(t.birthday.month)
print(t.birthday.day)
