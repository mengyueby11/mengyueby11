#-*- coding : utf-8 -*-
# coding: utf-8
import pymysql
from itertools import chain

class Officer_info:
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.2.31',
                               user='mysql',
                               passwd='123456',
                               database='hr2020',
                               charset='utf8')
        self.cursor = self.conn.cursor()
    #查询所有主管及经理用户的工号
    def Query_officer(self):
        sql = "select su.dutyid,u.empNo,u.empName,su.dutyName,m.titleName,a.fullDeptName " \
              "from ((" \
              "sys_duty su left join sys_title m on su.titleId=m.titleId)" \
              "left join sys_user u on su.dutyId=u.dutyId)" \
              "left join sys_department a on u.deptId=a.deptId where m.dutyLevel between 200 and 301 and u.useStatus=0"

        self.cursor.execute(sql)
        parentId_list = self.cursor.fetchall()
        list_line=[]
        fullDeptName_list=["智慧教育事业部","分销部","名校研究院","公共事务中心","运营中心","供应中心","财务管理中心","	教育研究院"]
        for i in list(parentId_list):
            line=list(i)
            if "-" in line[5]:
                if line[5].split("-")[0] in fullDeptName_list:
                    list_line.append(line[1:])
            elif line[5] in fullDeptName_list:
                list_line.append(line[1:])
        return list_line
    #查询下属人数
    def Personal_Data(self,empNo):
        sql="select count(*) " \
            "from sys_user m left join sys_duty su on m.dutyid=su.dutyId where su.parentId in " \
            "(select u.dutyId from sys_user u where u.empno in ("+empNo+")) and m.useStatus=0 "
        self.cursor.execute(sql)
        n = self.cursor.fetchall()
        n = list(chain.from_iterable(n))
        print(n)
        return n[0]
    # 数据库关闭
    def Close_mysql(self):
        self.cursor.close()
        self.conn.close()


if __name__=='__main__':
    officer=Officer_info()
    line_list=officer.Query_officer()
    for i in line_list:
        n=officer.Personal_Data(i[0])
        if n==1 and i[0]!='10001':
            print(i)
    officer.Close_mysql()