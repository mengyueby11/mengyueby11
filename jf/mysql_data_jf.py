#-*- coding : utf-8 -*-
# coding: utf-8
import pymysql
from itertools import chain
import pandas as pd
import numpy as np

class Mysql_search:
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.2.31',
                               user='mysql',
                               passwd='123456',
                               database='hr2020',
                               charset='utf8')

        self.cursor = self.conn.cursor()
        self.data_info()
        while True:
            empno = input("\n请输入工号(多个工号用“,”分隔)\n")
            print("\n")
            if "," in empno:
                empno_list=empno.replace("'","").strip("[").strip("]").split(",")
                for i in empno_list:
                    self.personal_info(i)
            elif empno=="T" or empno=='t':
                break
            else:
                empno=empno.strip()
                self.personal_info(empno)
        self.Close_mysql()
    #缓存数据生成（生成常用数据表）
    def data_info(self):
        sql="select su.dutyId,su.empNo,su.empName,m.dutyName,n.titleName,a.fulldeptName from ((sys_duty m left join sys_user su on m.dutyid=su.dutyid)" \
            "left join sys_title n on m.titleId=n.titleId)" \
            "left join sys_department a on m.deptId=a.deptId where a.fullDeptName is not null or trim(a.fullDeptName)!='' " \
            "and m.useStatus=0"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        self.cache_df=self.dataframe_info(result)
        #删除存在空值的行
        self.cache_df=self.cache_df.dropna(axis=0,how='any')
        instr=["dutyId","empNo","empName","dutyName","titleName","fulldeptName"]
        self.cache_df.columns=instr
    #个人数据查询
    def personal_info(self,empno):
        # list_line=[[10,"13982","王文辉","软件开发工程师","专员","IT平台开发部"],[10,"14064","辜迎龙","软件开发工程师","专员","IT平台开发部"],
        #            [1861,"14073","陈欢","软件开发工程师","专员","IT平台开发部"],[1491,"11881","罗秋香","人力资源部副经理","副经理","人力资源部"],
        #            [100,"10346","丁启福","生产部经理兼物流部经理","经理","生产部"]]
        # instr=["dutyId","empNo","empName","dutyName","titleName","fulldeptName"]
        # list_line=pd.DataFrame(list_line,columns=instr)
        # empno="10346"
        empno=empno.replace(" ","")
        dutyid=self.dutyId_info(empno)
        if dutyid!=0:
            (flag,tep)=self.dutylevel_info(dutyid)
            # print(empno)
            if flag!=0:
                lins=self.cache_df.loc[self.cache_df['empNo']==str(empno)]
                if len(lins.values)>0:
                    # lins = list_line.loc[list_line['empNo'] == str(empno)]
                    parentId = lins['dutyId'].values[0]
                    lins = np.array(lins).tolist()[0]
                    list_next,n=self.suoervisor_info(empno,parentId)
                    lins.append(n)
                    lins.append(tep)
                    print("岗位id：%s\n工号：%s\n名字：%s\n企业微信岗位：%s\n实际岗位：%s\n部门：%s\n下属人数：%s\n单次奖惩上限：%s"
                          %(str(lins[0]).replace(".0",""),lins[1],lins[2],lins[3],lins[4],lins[5],lins[6],lins[7]))
                    list_next=self.Screening_employees(list_next)
                    if len(list_next)>0:
                        print("下属为主管级以上的员工为:")
                        print(list_next)
                else:
                    print("工号%s员工未找到！"%empno)

            else:
                print("该用户为普通员工")
            print("\n\n")
            print("-----------------------------------------------------------------------------\n")
        else:
            print("工号%s员工未找到！"%empno)
        return
    #属下员工筛选（仅打印主管级以上员工）
    def Screening_employees(self,list_next):
        line=[]
        if len(list_next)==1:
            for i in list_next[0]:
                dutyid=self.dutyId_info(i)
                fag=self.DutyLevel(dutyid)
                if fag==0:
                    line.append(i)
        else:
            for i in list_next:
                for j in i:
                    dutyid = self.dutyId_info(j)
                    fag = self.DutyLevel(dutyid)
                    if fag == 0:
                        line.append(j)
        return line
    #主管级以上员工
    def suoervisor_info(self,empno,parentId):
        hold = self.hold_info(empno)
        list_next = []
        n = 0
        if hold!=None:
            for i in hold:
                (hold_parentid, hold_n) = self.parentId(i)
                if hold_n != 0:
                    list_next.append(hold_parentid)
                    n = n + hold_n
        (list_parentid, parentid_n) = self.parentId(parentId)
        list_next.append(list_parentid)
        n = n + parentid_n
        return list_next,n
    #仅判断员工级别
    def DutyLevel(self,dutyid):
        sql = "select dutyLevel from sys_title where titleId in (select u.titleId from sys_duty u where u.dutyId in (" + str(
            dutyid) + "))"
        self.cursor.execute(sql)
        dutylevel = self.cursor.fetchall()
        dutylevel = self.list_info(dutylevel)[0]
        if dutylevel<200:
            return -1
        else:
            return 0
    #判断员工级别
    def dutylevel_info(self,dutyid):
        sql="select dutyLevel from sys_title where titleId in (select u.titleId from sys_duty u where u.dutyId in ("+str(dutyid)+"))"
        self.cursor.execute(sql)
        dutylevel=self.cursor.fetchall()
        dutylevel=self.list_info(dutylevel)[0]
        flag=0
        #判断是否执行查询
        if dutylevel>=200:
            flag=1
            if dutylevel>=400:
                toplimit=100
            elif dutylevel==301:
                toplimit = 40
            elif dutylevel==300:
                toplimit = 30
            elif dutylevel==200:
                toplimit=20
            return flag,toplimit
        else:
            return flag,0
    #兼职列表查询dutyId
    def hold_info(self,empno):
        parttimeduty = "select su.dutyId from sys_user m " \
                       "left join emp_parttimeduty su on m.empId=su.empId where su.empId in  (select u.empId from sys_user u where u.empno in ( " + str(
            empno) + ")) and m.useStatus=0 "
        self.cursor.execute(parttimeduty)
        parttimeduty_result = self.cursor.fetchall()
        parttimeduty_result=self.list_info(parttimeduty_result)
        if len(parttimeduty_result) > 0:
            return parttimeduty_result
        else:

            return
    #通过dutyId查询parentId
    def dutyid_parentId(self,dutyid):
        sql="select parentId from sys_duty where dutyId in ("+str(dutyid)+")"
        self.cursor.execute(sql)
        result=self.list_info(self.cursor.fetchall())
        return result
    # 用户列表查询dutyId
    def dutyId_info(self,empno):
        sql="select dutyId from sys_user where empno in ("+str(empno)+")"
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        if len(result)!=0:
            result=self.list_info(result)
            return result[0]
        else:
            return 0
    #查询下级parentId
    def parentId(self,parentid):
        sql="select m.empNo from sys_user m " \
                 "left join sys_duty su on m.dutyid=su.dutyId where su.parentId in ("+str(parentid)+") " \
                                                                                              "and m.useStatus=0"
        self.cursor.execute(sql)
        parentid_result=self.cursor.fetchall()
        result=self.list_info(parentid_result)
        n=len(result)
        return result,n
    #将查询结果转换为list
    def list_info(self,result):
        result=list(chain.from_iterable(result))
        return result
    #将查询结果转换为矩阵
    def dataframe_info(self,result):
        df = pd.DataFrame(list(result))
        return df
    # 关闭链接的数据库
    def Close_mysql(self):
        self.cursor.close()
        self.conn.close()


if __name__=='__main__':
    Mysql_search()



