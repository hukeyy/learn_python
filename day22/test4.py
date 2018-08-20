#! /usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import xlsxwriter

workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 20)
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'Hello')
worksheet.write('A2', 'World', bold)
worksheet.write('B2', u'中文测试', bold)
worksheet.write('A3', 32)
worksheet.write('A4', 35.5)
worksheet.write('A5', '=SUM(A3:A4)')
worksheet.insert_image('B5', r'D:\1.png')
workbook.close()






