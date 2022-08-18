import random
from jifenNew.common.readMysql import database_query
import time

#填报积分
def Jsondata(empno):
    Data=[]
    data={}
    Database = database_query()
    standard='韬奋杯全国决赛获奖'
    result=Database.Execution('根据工作标准查询填报项', *[standard])
    # 查询部门id
    deptId = Database.Execution('查询部门ID', *[str(empno)])
    Time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    random_value = random.randint(10000, 1000000)
    remark = str(empno) + str(Time) + str(random_value)
    Database.Close_mysql()

    data['applyIntegral']=str(result[0][0])
    data['applyNum']=1
    data['applyUnit'] = result[0][1]
    data['approvalId']=''
    data['deptId'] = deptId[0][0]
    data['dimensionId']=result[0][2]
    data['informantId'] = empno
    data['remark'] = remark
    data['standardId']=result[0][3]
    Data.append(data)

    return Data
# if __name__ == '__main__':
#     print(Jsondata(11881))