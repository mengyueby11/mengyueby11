# -*- coding : utf-8 -*-
# coding: utf-8
import pymysql
from itertools import chain
import requests
import random
from dateutil.relativedelta import relativedelta
import datetime
import time

#数据库查询
class database_query:
    #连接数据库
    def __init__(self):
        self.jtyjy_integral_test = pymysql.connect(host="192.168.2.31", user="mysql", password="123456",
                                                   db='jtyjy_integral_test')
        self.hr2020 = pymysql.connect(host="192.168.2.31", user="mysql", password="123456", db='hr2020')
        self.testjf_sql = pymysql.connect(host="10.96.15.89", user="root", password="123456", db='testjf')
        self.jtyjy_cur=self.jtyjy_integral_test.cursor()
        self.hr2020_cur=self.hr2020.cursor()
        self.testjf_cur=self.testjf_sql.cursor()
    #数据查询
    def Data_Query(self,sql,name):
        sql=sql%name
        try:
            self.testjf_cur.execute(sql)
        except Exception as e:
            print('数据库查询失败: %s\n失败原因：%s' % (name, e))
        else:
            sql=self.testjf_cur.fetchall()
            if len(sql)>0:
                sql=list(chain.from_iterable(sql))
                return sql

            else:
                print("未查询到该数据: %s\n"%name)
                return -1
    #执行sql语句
    def Execution(self,type,*args):
        sql="select sentence,hr from inquire where type in ('%s')"
        sql=self.Data_Query(sql,type)
        if sql!=-1:
            if sql[1]==0:
                try:
                    self.jtyjy_cur.execute(sql[0],args)
                except Exception as e:
                    print('数据库查询失败: %s\n失败原因：%s' % (sql[0],e))
                else:
                    print("数据库查询成功\n")
                    result=self.jtyjy_cur.fetchall()
                    if len(result)>0:
                        return result
                    else:
                        print("%s查询结果为空\n",type)
                        return -1
            elif sql[1]==1:
                try:
                    self.hr2020_cur.execute(sql[0],args)
                except Exception as e:
                    print('数据库查询失败: %s\n失败原因：%s' % (sql[0],e))
                else:
                    print("数据库查询成功\n")
                    result=self.hr2020_cur.fetchall()
                    if len(result)>0:
                        return result
                    else:
                        print("%s查询结果为空\n",sql[0])
                        return -1
    #调用接口
    def invocation_interface(self,name,arg,jsondata=None):
        sql="select api,Post,code from interface where name in ('%s')"
        api=self.Data_Query(sql,name)
        # print(jsondata)
        if api!=-1:
            if api[1]==0 and jsondata==None:
                api=api[0]%arg
                try:
                    respon = requests.get(api).json()
                except requests.exceptions.ReadTimeout as a:
                    print("%s接口调用失败，失败原因：%s" % (api, a))
                    return -1
                else:
                    return self.result_info(respon,api)
            elif api[1]==1 and jsondata!=None and api[2]==1:
                random_value = random.randint(10000, 1000000)
                api=api[0]%(str(random_value),arg)
                try:
                    test_01 = requests.post(url=api, json=jsondata, timeout=5).json()
                except requests.exceptions.ReadTimeout as a:
                    print("%s接口调用失败，失败原因：%s" % (api, a))
                    return -1
                else:
                    return self.result_info(test_01,api)
    # 结果判断
    def result_info(self, test_01, api):
        if test_01['code'] == 0:
            print("接口调用成功!" )
            return test_01
        else:
            print("%s接口调用失败，失败原因：%s" % (api, test_01['msg']))
            return 0
    #关闭重新连接
    def Updata_mysql(self):
        self.Close_mysql()
        self.jtyjy_integral_test = pymysql.connect(host="192.168.2.31", user="mysql", password="123456",
                                                   db='jtyjy_integral_test')
        self.hr2020 = pymysql.connect(host="192.168.2.31", user="mysql", password="123456", db='hr2020')
        self.testjf_sql = pymysql.connect(host="10.96.15.89", user="root", password="123456", db='testjf')
        self.jtyjy_cur = self.jtyjy_integral_test.cursor()
        self.hr2020_cur = self.hr2020.cursor()
        self.testjf_cur = self.testjf_sql.cursor()
    # 数据库关闭
    def Close_mysql(self):
        self.jtyjy_cur.close()
        self.jtyjy_integral_test.close()
        self.hr2020_cur.close()
        self.hr2020.close()
        self.testjf_cur.close()
        self.testjf_sql.close()
#提报积分流程（提报-审核）
class Integral_fill:
    def __init__(self):
        self.database = database_query()
    #单次提报积分流程
    def Point_Management(self,applyNum,empno,standard):
        print("------------------提报积分--------------------------")
        remark=self.Jsondata(applyNum,empno,standard)
        self.database.Updata_mysql()
        if remark!=None:
            print("------------------------查询审批编号---------------------")
            approval_Id=self.Approval_Id(empno,remark)
            print("----------------------查询职级-----------------------")
            self.Query_Level(empno,approval_Id)
        return
    #批量审核
    def bulk_operation(self, applyNum, empno, standard, n):
        remark_list = []
        approval_Id_list = []
        print("------------------提报积分--------------------------")
        for i in range(0, n):
            remark = self.Jsondata(applyNum, empno, standard)
            remark_list.append(remark)
        print("------------重新连接数据库----------------------------")
        self.database.Updata_mysql()
        print("------------------------查询审批编号---------------------")
        for i in remark_list:
            approval_Id = self.Approval_Id(empno, i)
            approval_Id_list.append(approval_Id[0])
        print(approval_Id_list)
        print("-------------------积分员审核------------------------")
        # Integral.His_supervisor(empno, approval_Id_list)
        self.Query_Level(empno, approval_Id_list)
        return
    #审批流程判断
    def Query_Level(self,empno,approval_Id):
        titleId=self.database.Execution('查询职务id',*[str(empno)])[0][0]
        dutyLevel=self.database.Execution('职务id查询级别',str(titleId))[0][0]
        if 200<=dutyLevel<301:
            print("-----------------审核流程：积分员-部门经理/总裁---------------------------")
            self.Integral_Manager(empno,approval_Id)
            self.His_supervisor(empno,approval_Id)
        elif dutyLevel<200:
            print("-----------------审核流程：主管-积分员-部门经理---------------------------")
            self.His_supervisor(empno,approval_Id)
            self.Integral_Manager(empno,approval_Id)
            leaders_empno=self.His_supervisor(empno,123,dutyLevel)
            self.His_supervisor(leaders_empno,approval_Id)
    #查询Token
    def Token(self,empno):
        respon = self.database.invocation_interface('token', empno)
        if respon!=-1:
            token = respon['data'].split("=")[1]
            token = 'token' + '=' + token
            return token
    #填报项目
    def Jsondata(self,applyNum,empno,standard):
        result=self.database.Execution('根据工作标准查询填报项',*[standard])
        Time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        random_value = random.randint(10000, 1000000)
        remark=str(empno)+str(Time)+str(random_value)
        applyIntegral=list(result[0])[0]
        applyUnit=list(result[0])[1]
        dimensionId=list(result[0])[2]
        standardId=list(result[0])[3]
        # 查询部门id
        deptId=self.database.Execution('查询部门ID',*[str(empno)])
        if deptId!=-1:
            deptId = list(chain.from_iterable(deptId))[0]
            jsondata=[
            {
                    "applyIntegral": int(applyIntegral),
                    "applyNum": applyNum,
                    "applyUnit": applyUnit,
                    "approvalId": "",
                    "deptId": deptId,
                    "dimensionId": dimensionId,
                    "informantId": str(empno),
                    "remark": remark,
                    "standardId": standardId
            }
        ]
            token=self.Token(empno)
            self.database.invocation_interface('填报积分',token,jsondata)
            # print(remark)
            return remark
        else:
            print("%s未查询到该用户的岗位ID\n"%empno)
            return
    #上级审核
    def His_supervisor(self,empno,approval_id,dutyLevel=None):
        print("---------------------开始查询上级领导-------------------------")
        # 上级领导查询
        parentid =self.database.Execution('查询上级领导的岗位ID',*[str(empno)])
        if parentid !=-1:
            parentid =list(chain.from_iterable(parentid))[0]
            leaders_empno=self.database.Execution('岗位ID查询工号',*[str(parentid)])
            if leaders_empno==-1:
                leaders_empno = self.database.Execution('兼职表岗位ID查询工号', *[str(parentid)])
                if leaders_empno==-1:
                    print("工号为%s的用户无领导!\n"%empno)
            leaders_empno=list(chain.from_iterable(leaders_empno))[0]
            print("----------------查询到的上级领导为:%s---------------------------" % leaders_empno)
            if dutyLevel!=None:
                return leaders_empno
            print("-----------------------------------上级领导审核----------------------------------------")
            self.Audit(leaders_empno,approval_id)
            return
    #审核积分提报
    def Audit(self,empno,approval_id):
        # 审批编号处理
        if len(approval_id) > 1:
            integralIds = approval_id[0]
            for i in approval_id[1:]:
                integralIds = integralIds + ',' + i
        else:
            integralIds = approval_id[0]
        jsondata = {
            "integralIds": integralIds,
            "remark": "",
            "status": 1  # 1:通过 2:拒绝 3:驳回
        }
        print(integralIds)
        #调用接口
        token = self.Token(empno)
        self.database.invocation_interface('审核积分提报', token, jsondata)
    #积分员审核
    def Integral_Manager(self,empno,approval_Id):
        print("------------开始查询积分员----------------------")
        deptId=self.database.Execution('查询部门信息',*[str(empno)])
        #判断当前所处部门级别，3级部门往上查询
        if deptId[0][0]>2:
            fullDeptName=deptId[0][1].split("-")[0]+"-"+deptId[0][1].split("-")[1]
            deptId=self.database.Execution('通过部门全称查询部门ID',*[fullDeptName])[0][0]
        elif deptId[0][0]==2:
            deptId=deptId[0][2]
        emp_no=self.database.Execution('查询积分员',*[str(deptId)])[0][0]
        print("----------------查询到的积分员为:%s---------------------------" % emp_no)
        print("-----------------------------------积分员审核----------------------------------------")
        self.Audit(emp_no,approval_Id)
        return
        # 查询审批编号
    #查询审批编号
    def Approval_Id(self,empno,remark):
        approval_id=self.database.Execution('查询审批编号',*[str(empno),remark])
        if approval_id!=-1:
            approval_id =list(chain.from_iterable(approval_id))
            print(approval_id)
            return approval_id
class IntegralTask:
    def __init__(self):
        self.database = database_query()

    # 查询Token
    def Token(self, empno):
        respon = self.database.invocation_interface('token', empno)
        if respon != -1:
            token = respon['data'].split("=")[1]
            token = 'token' + '=' + token
            return token
    def integralTask_addTask(self,empno,integralDimension,taskObjId,taskObjType):
        nowtime = datetime.datetime.now()
        endDate = nowtime + datetime.timedelta(days=7)
        startDate=nowtime.strftime("%Y-%m-%d")
        endDate=endDate.strftime("%Y-%m-%d")
        random_value = random.randint(10000, 1000000)
        taskName=str(empno)+"测试任务"+nowtime.strftime("%Y%m%d%H%M%S")+str(random_value)
        jsondata = {
            "deductionIntegral": 100,
            "endDate": endDate,
            "integralDimension": integralDimension,
            "remark": "",
            "rewardIntegral": 100,
            "startDate":startDate,
            "taskName": taskName,
            "taskObjList": [
                {
                    "taskObjId": taskObjId,
                    "taskObjType": taskObjType
                }
            ]
        }

        return
if __name__ == '__main__':
    # Integral=Integral_fill()
    # Integral.bulk_operation(1,20048,'韬奋杯全国决赛获奖',3)
    # Integral.database.Close_mysql()
    integralTask=IntegralTask()


    integralTask.database.Close_mysql()