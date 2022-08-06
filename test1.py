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
        self.Connect_mysql()
        self.testjf_url=r"http://testjf.jtyjy.com"
        self.token_url=r"http://oauth.jtyjy.com"
    #数据查询
    def Data_Query(self,sql,name):
        sql=sql%name
        # print(sql)
        try:
            self.testjf_cur.execute(sql)
        except Exception as e:
            print('数据库查询失败: %s\n失败原因：%s' % (name, e))
        else:
            sql=self.testjf_cur.fetchall()
            # print(sql)
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
        # print(sql)
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
        # print(api)
        if api!=-1:
            if api[1]==0 and jsondata==None:
                api=api[0]%arg
                if name=="token":
                    if self.token_url not in api:
                        api=self.token_url+api
                else:
                    if self.testjf_url in api:
                        api=self.testjf_url+api
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
                if self.testjf_url not in api:
                    api=self.testjf_url+api
                try:
                    test_01 = requests.post(url=api, json=jsondata, timeout=5).json()
                except requests.exceptions.ReadTimeout as a:
                    print("%s接口调用失败，失败原因：%s" % (api, a))
                    return -1
                else:
                    return self.result_info(test_01,api)
            elif api[1]==1 and jsondata!=None and api[2]==0:
                api=api[0]%(arg)
                if self.testjf_url not in api:
                    api=self.testjf_url+api
                # print(api)
                try:
                    test_01 = requests.post(url=api, json=jsondata, timeout=5).json()
                except requests.exceptions.ReadTimeout as a:
                    print("%s接口调用失败，失败原因：%s" % (api, a))
                    return -1
                else:
                    return self.result_info(test_01,api)
            elif api[1]==0:
                api = api[0] % (arg)
                if self.testjf_url not in api:
                    api=self.testjf_url+api
                s_api=''
                for key, value in jsondata.items():
                    s_api = str(s_api) + "&%s=%s" % (key, value)
                api=api+s_api
                try:
                    test_01 = requests.get(url=api,timeout=5).json()
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
        self.Connect_mysql()
    #连接数据库
    def Connect_mysql(self):
        self.jtyjy_integral_test = pymysql.connect(host="192.168.2.31", user="mysql", password="123456",
                                                   db='jtyjy_integral_test')
        self.hr2020 = pymysql.connect(host="192.168.2.31", user="mysql", password="123456", db='hr2020')
        self.testjf_sql = pymysql.connect(host="192.168.2.31", user="mysql", password="123456", db='auto_test')
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

    # 查询Token
    def Token(self, empno):
        respon = self.database.invocation_interface('token', empno)
        if respon != -1:
            token = respon['data'].split("=")[1]
            token = 'token' + '=' + str(token)
            return token
    # 单次提报积分流程
    def Point_Management(self, applyNum, empno, standard):
        remark = self.Jsondata(applyNum, empno, standard)
        print("------------重新连接数据库----------------------------")
        self.database.Updata_mysql()
        if remark != None:
            approval_Id = self.Approval_Id(empno, remark)
            reviewer=self.Reviewer(str(approval_Id[0]))
            if reviewer!=None:
                print("-----------------开始审批积分------------------------------\n")
                if reviewer[1]==1 or reviewer[1]==2:
                    self.Audit(reviewer[0],approval_Id)
                return
    #批量提报积分流程
    def bulk_operation(self, applyNum, empno, standard,n):
        remark_list = []
        approval_Id_list = []
        print("------------------开始批量提报积分--------------------------")
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

        reviewer = self.Reviewer(str(approval_Id_list[0]))
        if reviewer != None:
            print("-------------------开始批量审核------------------------")
            if reviewer[1] == 1 or reviewer[1] == 2:
                self.Audit(reviewer[0], approval_Id_list)
            return
    # 填报项目
    def Jsondata(self, applyNum, empno, standard):
        print("------------------提报积分--------------------------")
        result = self.database.Execution('根据工作标准查询填报项', *[standard])
        Time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        random_value = random.randint(10000, 1000000)
        remark = str(empno) + str(Time) + str(random_value)
        applyIntegral = list(result[0])[0]
        applyUnit = list(result[0])[1]
        dimensionId = list(result[0])[2]
        standardId = list(result[0])[3]
        # 查询部门id
        deptId = self.database.Execution('查询部门ID', *[str(empno)])
        if deptId != -1:
            deptId = list(chain.from_iterable(deptId))[0]
            jsondata = [
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
            token = self.Token(empno)
            self.database.invocation_interface('填报积分', token, jsondata)
            # print(remark)
            return remark
        else:
            print("%s未查询到该用户的岗位ID\n" % empno)
            return
    # 查询审批编号
    def Approval_Id(self, empno, remark):
        print("------------------------查询审批编号---------------------")
        approval_id = self.database.Execution('查询审批编号', *[str(empno), remark])
        if approval_id != -1:
            approval_id = list(chain.from_iterable(approval_id))
            print(approval_id)
            return approval_id
    #查询审批人
    def Reviewer(self,approval_id):
        # print(approval_id)
        reviewer=self.database.Execution('查询积分审批人工号',*[approval_id])
        # print(reviewer)
        if reviewer!=None:
            return reviewer[0]
    #审核积分提报
    def Audit(self,empno,approval_id):
        print("----------------------%s审批---------------------------------\n"%empno)
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
        self.database.Updata_mysql()
        reviewer=self.Reviewer(approval_id[0])
        if reviewer[1]==1 or reviewer[1]==2:
            return self.Audit(reviewer[0],approval_id)
        else:
            return
#新建任务
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
    #单次新建积分任务流程检查
    def integralTask_addTask(self,empno,integralDimension):
        # 调用接口
        token = self.Token(empno)
        taskName=self.Create_integralTask(empno,integralDimension,token)
        print("积分任务名称为：%s"%taskName)
        self.database.Updata_mysql()
        cur_auditor=self.database.Execution('查询任务审批人',*[taskName])
        print(cur_auditor)
        if cur_auditor[0][1]==1:
            self.integralTask_verifyTask(cur_auditor[0][2],cur_auditor[0][0])
        return
    #批量单次新建积分任务流程检查
    def list_integralTask_addTask(self,empno,integralDimension,n):
        taskName_list=[]
        token = self.Token(empno)
        for i in range(0,n):
            taskName=self.Create_integralTask(empno,integralDimension,token)
            taskName_list.append(taskName)
        self.database.Updata_mysql()
        for i in taskName_list:
            cur_auditor = self.database.Execution('查询任务审批人', *[i])
            print(cur_auditor)
            if cur_auditor[0][1] == 1:
                self.integralTask_verifyTask(cur_auditor[0][2], cur_auditor[0][0])
        return
    #创建任务
    def Create_integralTask(self,empno,integralDimension,token):
        # token = self.Token(empno)
        print("--------------------开始新建任务----------------")
        nowtime = datetime.datetime.now()
        endDate = nowtime + datetime.timedelta(days=7)
        startDate = nowtime.strftime("%Y-%m-%d")
        endDate = endDate.strftime("%Y-%m-%d")
        random_value = random.randint(10000, 1000000)
        taskName = str(empno) + "测试任务" + nowtime.strftime("%Y%m%d") + str(random_value)
        taskObjId = self.database.Execution('查询部门ID', *[empno])[0][0]
        jsondata = {
            "deductionIntegral": 100,
            "endDate": endDate,
            "integralDimension": integralDimension,
            "remark": "",
            "rewardIntegral": 100,
            "startDate": startDate,
            "taskName": taskName,
            "taskObjList": [
                {
                    "taskObjId": taskObjId,
                    "taskObjType": 1
                }
            ]
        }

        reluse=self.database.invocation_interface('新建积分任务', token, jsondata)
        if reluse!=-1:
            return taskName
    #审批任务
    def integralTask_verifyTask(self,empno,id):
        # 调用接口
        token = self.Token(empno)
        print("----------------开始审批流程----------------------")
        print("--------------------%s审批任务----------------"%empno)
        jsondata={
            "id":id,
            "isAgree":1,
            "remark":""
        }
        self.database.invocation_interface('审核任务', token, jsondata)
        self.database.Updata_mysql()
        staus=self.database.Execution('通过任务ID任务状态', *[str(id)])
        if staus!=-1:
            if staus[0][0]==1:
                self.integralTask_verifyTask(staus[0][1],id)
        return

#异动
class numerical_calculation:
    def __init__(self):
        self.database = database_query()
    # 查询Token
    def Token(self, empno):
        respon = self.database.invocation_interface('token', empno)
        if respon != -1:
            token = respon['data'].split("=")[1]
            token = 'token' + '=' + token
            return token
    #异动
    def deptChange(self,empNo,newDutyId,originDutyId):
        token=self.Token(empNo)
        jsondata={
            "empNo": empNo,
            "newDutyId": newDutyId,
            "originDutyId": originDutyId
        }
        fag=self.database.invocation_interface('部门异动',token,jsondata)
        return fag
    #异动执行
    def transaction(self,empno):
        #异动前的岗位ID
        originDutyId=self.database.Execution('查询岗位ID',*[empno])
        #异动后的岗位ID
        # dutyname = input("输入异动后的岗位：\n")
        dutyname='智慧编辑组长'
        newDutyID=self.database.Execution('岗位名称查询岗位ID',*[dutyname])
        #判断该岗位是否存在，不存在不执行异动
        if originDutyId!=-1 and newDutyID!=-1:
            timedata = time.strftime('%Y-%m-%d %H:%M')
            print(timedata)
            #执行异动
            # fag=self.deptChange(empno,newDutyID,originDutyId)
            fag=1
            if fag!=-1:
                self.transaction_joggle(empno,timedata)
    #异动数据查询
    def transaction_joggle(self,empNo,timedata):
        #更新数据库
        self.database.Updata_mysql()
        data_joggle=self.database.Execution('通过工号查询指定积分数据',*[1232,empNo])
        if data_joggle!=-1:
            for i in data_joggle:
                time_data=i[2].strftime('%Y-%m-%d %H:%M')
                if time_data == timedata:
                    result = [i[0], i[1]]
            transaction_reauls = [str(round(result[1],2)), result[0]]
            print(transaction_reauls)
            # return transaction_reauls

if __name__ == '__main__':
    # numerical=numerical_calculation()
    # # numerical.transaction(17310)
    # numerical.transaction_joggle(21579,'2022-06-27 16:43')
    # numerical.database.Close_mysql()
    # Integral=Integral_fill()
    # Integral.bulk_operation(1,20048,'韬奋杯全国决赛获奖',3)
    # Integral.database.Close_mysql()
    integralTask=IntegralTask()
    # integralTask.list_integralTask_addTask(11881,4,2)
    integralTask.integralTask_addTask(11881,4)
    integralTask.database.Close_mysql()