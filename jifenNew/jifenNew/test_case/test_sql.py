# -*- coding: utf-8 -*-
# @Time : 2022/7/11 13:59 
# @Author : daixilin
# @File : test_sql.py 
# @Project: jifenNew
import pymysql
import time
import pytest
emp='20192'
class TestSql():
    # def __init__(self):
    #     cn=pymysql.connect(host='192.168.2.31',
    #                            user='mysql',
    #                            passwd='123456',
    #                            database='hr2020',
    #                            charset='utf8')
    #     self.cursor=cn.cursor()

    def test_selct(self):
        cn = pymysql.connect(host='192.168.2.31',
                             user='mysql',
                             passwd='123456',
                             database='jtyjy_integral_test',
                             charset='utf8')
        self.cursor = cn.cursor()
        nowtime = time.strftime('%Y-%m-%d %H:%M', time.localtime())
        a=nowtime+'%'

        sql = "select * from tb_integral where (remark='接口测试' and informant_id ="+emp+")and created_time like '2022-07-11 13:58'"
        self.cursor.execute(sql)
        all = self.cursor.fetchall()
        for a in all:
            print(a)
if __name__ == "__main__":
    pytest.main(['-vs', 'test_sql.py'])