#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import pymysql

mysql_dict = {
        'host': '172.168.20.188',
        'port': 3306,
        'user': 'dba',
        'passwd': 'dba@wsd.com',
        'db': 'winstar_spree'
    }


class Database(object):
    '''查询数据库并生成Excel文档'''

    def __init__(self, mysql_info):
        self.mysql_info = mysql_info
        self.conn = pymysql.connect(host = self.mysql_info['host'], port = self.mysql_info['port'],
                               user = self.mysql_info['user'], passwd = self.mysql_info['passwd'],
                               db = self.mysql_info['db'], charset='utf8')
        self.cursor = self.conn.cursor()
    def getUserData(self, sql):
        # 查询数据库
        self.cursor.execute(sql)
        # table_desc = self.cursor.description
        result = self.cursor.fetchall()
        if not result:
            print('没数据。')
            # 返回查询数据、表字段
        print('数据库查询完毕'.center(30, '#'))
        return result


table_tuple = ('cbc_white_list', 'cbc_six_white_list', 'cbc_seven_white_list', 'cbc_eight_white_list')
for table_name in table_tuple:
    sql = '''
        SELECT
        	o.account_id,
        	c.phone_number
        FROM
        	
        	cbc_oil_order o,
        	%s c
        WHERE
        	o.account_id = c.account_id
        AND o.pay_time >= "2018-10-08 00:00:00"
        AND pay_time <= "2018-10-08 23:59:59";
        ''' % table_name
    sql_exec = Database(mysql_dict)
    sql_res = sql_exec.getUserData(sql)
    print(sql_res)
    print(len(sql_res))
