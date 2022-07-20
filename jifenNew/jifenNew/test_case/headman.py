#-*- coding : utf-8 -*-
# coding: utf-8
import pymysql
from itertools import chain
import requests
import random


class Joggle_Info:
    def __init__(self):
        conn = pymysql.connect(host='192.168.2.31',
                               user='mysql',
                               passwd='123456',
                               database='hr2020',
                               charset='utf8')
        self.cursor = conn.cursor()
    #所有组长查询
    def headman(self):
        sql = "select n.empNo from (sys_title su left join sys_duty m on su.titleId=m.titleId)" \
              "left join sys_user n on m.dutyId=n.dutyId where su.titleName in ('员工-组长') and n.useStatus=0"
        self.cursor.execute(sql)
        empNo_list=self.cursor.fetchall()
        empNo_list=list(chain.from_iterable(empNo_list))
        return empNo_list
    #token查询
    def Token(self,empNo):
        token = "http://oauth.jtyjy.com/api/oneLogin/sso?serverId=29&empno="+str(empNo)+"&pwd=123456"
        respon=requests.get(token).json() # 请求接口
        token=respon['data'].split("=")[1]
        token='token'+'='+token
        return token
    #结果判断
    def result_info(self,test_01,empNo):
        if test_01['code'] == 0:
            print("工号为%s接口调用成功!" % empNo)
        else:
            print("工号为%s接口调用失败，失败原因：%s" % (empNo, test_01['msg']))
        return
    #创建积分任务
    def integralTask_addTask(self,empNo,test_name):
        token=self.Token(empNo)
        test_url = "http://testjf.jtyjy.com"
        all_url = test_url + '/api/integralTask/addTask?' + token
        # print(all_url)
        jsondata = {
            "deductionIntegral": 1000,
            "endDate": "2022-07-15",
            "integralDimension": 4,  # 2 产值积分 3 公共积分 4 部门积分 1 固定积分
            "remark": "111",
            "rewardIntegral": 1000,
            "startDate": "2022-07-12",
            "taskName": test_name,
            "taskObjList": [
                {
                    "taskObjId": 478,
                    "taskObjType": 1  # 1 部门 2人员
                }
            ]
        }
        try:
            test_01 = requests.post(url=all_url, json=jsondata, timeout=5).json()
        except requests.exceptions.ReadTimeout as a:
            print("工号%s接口调用失败，失败原因：%s" % (empNo, a))
        else:
            self.result_info(test_01, empNo)
        return
    #填报积分
    def intergral_save(self,empNo):
        random_value = random.randint(10000, 1000000)
        token = self.Token(empNo)
        test_url = "http://testjf.jtyjy.com"
        all_url = test_url + '/api/integral/save/' + str(random_value) + '?' + token
        jsondata = [{
            "applyIntegral": 300,
            "applyNum": 1,
            "applyUnit": "次",
            "approvalId": "",
            "deptId": 531,
            "dimensionId": 3,
            "informantId": str(empNo),
            "remark": "11111",
            "standardId": 1592
        }]
        try:
            test_01 = requests.post(url=all_url, json=jsondata, timeout=5).json()
        except requests.exceptions.ReadTimeout as a:
            print("工号%s接口调用失败，失败原因：%s" % (empNo, a))
        else:
            self.result_info(test_01, empNo)
        return


# empNo_list=headman()
# for i in empNo_list:
#     # print(i)
#     joggle(i,str(i)+"测试任务5")
if __name__=='__main__':
    Joggle=Joggle_Info()
    empNo_list=Joggle.headman()
    print(empNo_list)
    # Joggle.integralTask_addTask('14097','14097测试任务11')
    for i in empNo_list:
        Joggle.intergral_save(i)
