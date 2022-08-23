from jifenNewOne.common.readMysql import database_query
from jifenNewOne.common.gettoken import Token
from jifenNewOne.otherdata import data

import random

# 随机取值
def random_sampling(datas,Str):
    datas = random.sample(datas, 1)
    if Str in str(datas[0][Str]):
        return random_sampling(datas[0][Str],Str)
    else:
        return datas
#通用接口
def Interface(users,name,jsondata):
    token = Token().token_way(users, data.token_url)
    test_01, api = database_query().invocation_interface(name, data.web_address, token, jsondata)
    datas=database_query().result_info(test_01, api)
    return datas,api

'''个人信息生成'''
def Users_Data(auditor):
    certifiCateNo=database_query().Execution('查询身份证号',*[auditor])
    assert certifiCateNo!=-1
    print("个人信息")
    data.users_data['empno']=auditor
    data.users_data['pwd']= str(certifiCateNo[0][0])[-6:]
    return data.users_data