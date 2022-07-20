import itertools

import pymysql
from itertools import chain

#-*- coding : utf-8 -*-
# coding: utf-8




conn=pymysql.connect(host='192.168.2.31',
                     user='mysql',
                     passwd='123456',
                     database='jtyjy_integral_test',
                     charset='utf8')

cursor=conn.cursor()
sql="select id from tb_points_project where category in ('人才输送') and points in (150) and is_delete=0"
cursor.execute(sql)
print(cursor.fetchall())
# def om_info(empno):
#     sql="select su.dutyId,su.dutyName,m.empNo,m.empName " \
#         "from sys_duty su left join sys_user m on m.dutyId=su.dutyid where su.dutyId in " \
#         "(select parentId from sys_duty where dutyId in (select dutyid from sys_user u where u.empno in ("+str(empno)+")))"
#
#     cursor.execute(sql)
#     manager_result=cursor.fetchall()
#     manager_result=list(chain.from_iterable(manager_result))
#
#     if manager_result[2]==None:
#         print(empno)
#         print(manager_result)
#     return
#
# f=open(r"C:\Users\Administrator\Desktop\1.txt","r+",encoding='utf-8')
# # print(f.readlines())
# list_line=[]
# for line in f.readlines():
#     list_line.append(line.replace("\t"," ").replace("\n","").split())
#
# list_line=list_line[1:]
# for i in list_line:
#     if i[2]!=i[3]:
#         om_info(i[3])

cursor.close()
conn.close()