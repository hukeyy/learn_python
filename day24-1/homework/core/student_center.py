#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
from conf.settings import main_db_file
from model.tools import option, file_oper
from model.tools import file_oper

class Student_center(object):
    student_list = ['学员注册', '返回']
    def __init__(self):
        self.run()
    def run(self):
        while True:
            self.school_db = file_oper(main_db_file, 'rb')
            choice = option(Student_center.student_list)
            if choice == '1':
                self.regist_student()
            else:
                break
    
    def regist_student(self):
        student_name = input('\033[34;1m输入姓名:\033[0m').strip()
        
        for key in self.school_db:
            print('\033[32;1m学校名【%s】\033[0m' % key)
        
        school_name = input('\033[34;1m选择学校名:\033[0m').strip()
        if school_name in self.school_db:
            self.school_name = school_name
            self.school = self.school_db[school_name]
            for key in self.school.school_grade:
                self.grade_obj = self.school.school_grade[key]
                self.grade_obj.cat_grade()
            grade_name = input('\033[34;1m输入选择的班级名:\033[0m').strip()
            if grade_name in self.school.school_grade:
                self.grade = self.school.school_grade[grade_name]
                print('\033[32;1m课程【%s】的价格为【%s元】\033[0m' % (self.grade.course_obj.course_name, 
                                                           self.grade.course_obj.course_price))
                if_pay = input('\033[33;1m是否支付当前费用[y]:').strip()
                if if_pay == 'y':
                    self.grade.add_student(student_name)
                    self.school_db[self.school_name] = self.school
                    file_oper(main_db_file, 'wb', self.school_db)
                    print('\033[35;1m选课成功.\033[0m')
                    
                
            


        
        
        