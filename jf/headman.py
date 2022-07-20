#-*- coding : utf-8 -*-
# coding: utf-8
import pymysql
from itertools import chain
import requests
import random
from dateutil.relativedelta import relativedelta
import datetime


#数据库查询
class database_query:
    def __init__(self):
        self.conn = pymysql.connect(host='192.168.2.31',
                               user='mysql',
                               passwd='123456',
                               database='jtyjy_integral_test',
                               charset='utf8')
        self.cursor = self.conn.cursor()
        self.conn1= pymysql.connect(host='192.168.2.31',
                               user='mysql',
                               passwd='123456',
                               database='hr2020',
                               charset='utf8')
        self.cursor1 = self.conn1.cursor()
    #sql语句执行
    #积分数据库
    def sql_cursor(self, sql):
        self.cursor.execute(sql)
        line_list = self.cursor.fetchall()
        return line_list
    #hr数据库
    def sql_cursor1(self, sql):
        self.cursor1.execute(sql)
        line_list = self.cursor1.fetchall()
        return line_list
    #转换为一维数组
    def list_info(self,line_list):
        return list(chain.from_iterable(line_list))
    #所有组长查询
    def headman(self):
        sql = "select n.empNo from (sys_title su left join sys_duty m on su.titleId=m.titleId)" \
              "left join sys_user n on m.dutyId=n.dutyId where su.titleName in ('员工-组长') and n.useStatus=0"
        empNo_list=self.sql_cursor(sql)
        empNo_list=self.list_info(empNo_list)
        return empNo_list
    #总积分查询 id维度ID（2 产值积分 3 公共积分 4 部门积分 1 固定积分）
    def person_integral(self,empNo,id,dutyid=None):
        if int(id)==4:
            sql="select created_time,apply_item_id,apply_integral*apply_num,dept_id from tb_integral where informant_id in ("+str(empNo)+") and dimension_id in ("+str(id)+")order by created_time desc"
            sum_list = self.sql_cursor(sql)
            sum=0
            for i in list(sum_list):
                if i[1]!=1232:
                    if i[-1]==int(dutyid):
                        sum=sum+round(i[-2],2)
                else:
                    return sum
        else:
            sql="select sum(apply_integral*apply_num) from tb_integral where informant_id in ("+str(empNo)+") and dimension_id in ("+str(id)+")"
            sum=self.sql_cursor(sql)
            sum=self.list_info(sum)[0]
            return sum
    #通过名字查询异动数据
    def transaction_intergral(self,name):
        sql="select dept_id,apply_integral from tb_integral where apply_item_id=1232 and informant in ('"+name+"')"
        result=self.sql_cursor(sql)
        result=self.list_info(result)
        if len(result)==2:
            return result
        else:
            return 0
    #二级部门查询
    #通过工号
    def Inquire_department(self,empNo):
        sql="select fullDeptName from sys_department where deptId in (select su.deptId from sys_user su where su.empNo in ("+str(empNo)+"))"
        departmentName=self.sql_cursor1(sql)
        departmentName=self.list_info(departmentName)[0]
        return departmentName
    #通过岗位
    def Inquire_fullDeptName(self,name):
        sql="select fullDeptName from sys_department where deptId in (select su.deptId from sys_duty su where su.dutyName in ('"+name+"'))"
        fulldeptname=self.sql_cursor(sql)
        if len(fulldeptname)>0:
            fulldeptname=self.list_info(fulldeptname)[0]
            return fulldeptname
        else:
            print("未查询到%s相关信息！\n"%name)
            return 0
    #通过岗位ID
    def Inquire_deptid(self,deptid):
        sql="select fullDeptName from sys_department where deptid="+str(deptid)
        fulldeptname=self.sql_cursor(sql)
        if len(fulldeptname)>0:
            fulldeptname=self.list_info(fulldeptname)[0]
            return fulldeptname
        else:
            print("未查询到岗位id为%s的部门！\n"%deptid)
            return 0
    #当前部门总人数
    def department_number(self,departmentName):
        sql="select count(*) " \
            "from sys_user su left join sys_department m on m.deptId=su.deptId where m.fullDeptName LIKE ('%"+departmentName+"%') and su.useStatus=0"
        department=self.sql_cursor(sql)
        return self.list_info(department)[0]
    # 用户列表部门id
    def deptId_info(self, empno):
        sql = "select deptId from sys_user where empNo=" + str(empno)
        result = self.sql_cursor(sql)
        if len(result) != 0:
            result = self.list_info(result)

            return result[0]
        else:
            return 0
    #部门总积分输入,计算平均分及总人数
    def transaction_sum(self,departmentName):
        if "-" in departmentName:
            departmentName=departmentName.split("-")[0:2]
            department_data = input("输入[%s-%s]的部门总积分：\n" % (departmentName[0], departmentName[1]))
            name=departmentName[1]
        else:
            department_data=input("输入[%s]的部门总积分：\n"%departmentName)
            name = departmentName[1]
        number=self.department_number(name)
        av=int(department_data)/int(number)
        return av,number
    #通过工号查询名字
    def empno_name(self,empno):
        sql="select empName from sys_user where empNo="+str(empno)
        result = self.sql_cursor(sql)
        if len(result)!=0:
            return (self.list_info(result))[0]
        else:
            return 0
    #通过岗位名称查询级别
    def DutyLevel(self,dutyName):
        sql="select title.dutyLevel from sys_duty duty  left join sys_title title on title.titleId=duty.titleId where duty.dutyName in ('"+dutyName+"')"
        dutylevel=self.sql_cursor(sql)
        if len(dutylevel)!=0:
            return (self.list_info(dutylevel))[0]
        else:
            return 0
    #入职年限查询，不满一年计算为0
    def HireDate(self,empNo):
        sql="select emp.hireDate from emp_employeefile emp left join sys_user us on emp.empId=us.empId where us.empNo="+str(empNo)
        hireDate=self.sql_cursor1(sql)
        if len(hireDate)!=0:
            hireDate=hireDate[0][0]
            hir=datetime.datetime.strptime(hireDate,'%Y-%m-%d')
            now_time=datetime.datetime.now()
            long_time=relativedelta(dt1=now_time,dt2=hir).years
            return long_time
        else:
            return 0
    #上级领导查询
    def superior_leaders(self,empNo):
        sql="select m.empNo from sys_duty su left join sys_user m on m.dutyId=su.dutyid where su.dutyId in" \
            "(select parentId from sys_duty where dutyId in (select dutyid from sys_user u where u.empno="+str(empNo)+"))"
        leaders_empNo=self.cursor1(sql)
        if len(leaders_empNo)!=0:
            leaders_empNo=self.list_info(leaders_empNo)[0]
            return leaders_empNo
        else:
            return 0
    #填报积分项的id查询
    def points_project(self,category,points=None):
        if points!=None:
          sql="select id from tb_points_project where category in ('"+category+"') and points in ("+str(points)+") and is_delete=0"
        else:
            sql = "select id from tb_points_project where category in ('" + category + "') and is_delete=0"
        id=self.sql_cursor(sql)
        if len(id)!=0:
            id=self.list_info(id)[0]
            return id
        else:
            return 0
    #数据库关闭
    def Close_mysql(self):
        self.cursor.close()
        self.conn.close()
        self.cursor1.close()
        self.conn1.close()
#接口调用
class Interface_call:
    # token查询
    def Token(self, empNo):
        token = "http://oauth.jtyjy.com/api/oneLogin/sso?serverId=29&empno=" + str(empNo) + "&pwd=123456"
        respon = requests.get(token).json()  # 请求接口
        token = respon['data'].split("=")[1]
        token = 'token' + '=' + token
        return token
    # 结果判断
    def result_info(self, test_01, empNo):
        if test_01['code'] == 0:
            print("工号为%s接口调用成功!" % empNo)
        else:
            print("工号为%s接口调用失败，失败原因：%s" % (empNo, test_01['msg']))
        return
     # 创建积分任务
    def integralTask_addTask(self, empNo, test_name,taskObjId):
        token = self.Token(empNo)
        test_url = "http://testjf.jtyjy.com"
        all_url = test_url + '/api/integralTask/addTask?' + token
        # print(all_url)
        jsondata = {
            "deductionIntegral": 1000,
            "endDate": "2022-07-25",
            "integralDimension": 4,  # 2 产值积分 3 公共积分 4 部门积分 1 固定积分
            "remark": "111",
            "rewardIntegral": 1000,
            "startDate": "2022-07-18",
            "taskName": test_name,
            "taskObjList": [
                {
                    "taskObjId": taskObjId,
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
    # 填报积分
    def intergral_save(self, empNo):
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
    #异动

class numerical_calculation:
    def __init__(self):
        self.database=database_query()
    # 异动公式计算
    def transaction_data(self, empNo):
        deptid = self.database.deptId_info(empNo)
        if deptid != 0:
            person_transaction = self.database.person_integral(empNo, 4, deptid)
            departmentName = self.database.Inquire_department(empNo)
            (before_av, num_before) = self.database.transaction_sum(departmentName)
            dutyname = input("输入异动后的岗位：\n")
            fulldeptname = self.database.Inquire_fullDeptName(dutyname)
            if fulldeptname != 0:
                (after_av, num_after) = self.database.transaction_sum(fulldeptname)
                transaction = int(person_transaction) / before_av * after_av
                print("-------------------------------异动数据打印---------------------------------------\n")
                print(after_av, before_av)
                print(
                        "异动前个人部门积分为:%s\n异动前的部门为:%s\n异动前的部门人数为:%s\n" % (person_transaction, departmentName, num_before))
                print("异动后个人部门积分为:%s\n异动后的部门为:%s\n异动后的部门人数为:%s\n" % (transaction, fulldeptname, num_after))
            print("----------------开始核算后台数据库--------------\n")
            print("--------------个人异动积分核算----------------\n")
            name=self.database.empno_name(empNo)
            self.transaction_joggle(name,fulldeptname,transaction)
        else:
            print("未到工号为%s的员工\n!")
    def transaction_superior_leaders(self,dutyname,empNo):
        dutylevel=self.database.DutyLevel(dutyname)
        if 300<=dutylevel<301:
            Bonus=200
        elif 200<=dutylevel<300:
            Bonus = 150
        elif dutylevel<200:
            term=self.database.HireDate(empNo)
            if term<1:
                print("工号%s员工未满一年且异动岗位为普通员工，上级无积分奖励\n"%empNo)
            else:
                Bonus=100
        leaders_empNo=self.database.superior_leaders(empNo)
        id = self.database.points_project("人才输送", Bonus)
        print("------------------未完成部分---------------------------------------------------------------------")
        print(id)
        return
    # 异动数据核算
    def transaction_joggle(self,name,deptname,transaction):
        reauls=self.database.transaction_intergral(name)
        print(reauls)
        if reauls!=0:
            deptid=reauls[0]
            num=round(reauls[1],2)
        else:
            print("未查询到%s异动的数据！"%name)
            return
        fulldeptname=self.database.Inquire_deptid(deptid)
        if fulldeptname==deptname and round(transaction,2)==num:
            print("后台异动数据核算正确！\n")
        else:
            print("后台异动数据核算错误！后台查询到数据为：\n异动积分：%s\t"%num)
        return
    #获取二级部门名字
    def Split_name(self,fulldeptname):
        if "-" in fulldeptname:
            return fulldeptname.split("-")[1]
        else:
            return fulldeptname
if __name__=='__main__':
    numerical_calculation=numerical_calculation()
    Interface_call=Interface_call()
    # empNo_list=[14860,15371,16532]
    # for i in empNo_list:
        # Interface_call.intergral_save(str(i))
        # Interface_call.integralTask_addTask(str(i),str(i)+"2207141557")
    # database.connect_sql()
    # numerical_calculation.transaction_data("21579")
    # numerical_calculation.transaction_superior_leaders("智慧编辑组长",21579)
    # numerical_calculation.transaction_superior_leaders("智慧编辑组长",21579)
    # # numerical_calculation.database.HireDate("16517")
    # numerical_calculation.database.Close_mysql()
    # empNo={20822,18365,17266,16459}
    # for i in empNo:
    #     Interface_call.integralTask_addTask(i,str(i)+"20220718测试任务",472)
    Interface_call.integralTask_addTask(20859, str(20859) + "20220718测试任务", 472)
    # # Joggle.integralTask_addTask('14097','14097测试任务11')
    # # for i in empNo_list:
    # #     # 填报积分
    # #     Joggle.intergral_save(i)
    # #     ##创建积分任务
    # #     Joggle.integralTask_addTask(i)
    # # for i in range(0,10):
    # #     Joggle.intergral_save("20739")
    # Joggle.Close_mysql()
