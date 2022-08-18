from jifenNew.common.readMysql import database_query
from jifenNew.common.gettoken import Token
import random
import time


# 随机取值
def random_sampling(datas,Str):
    datas = random.sample(datas, 1)
    if Str in str(datas[0][Str]):
        return random_sampling(datas[0][Str],Str)
    else:
        return datas
#通用接口
def Interface(users,name,jsondata):
    token = Token().token_way(users['data'], users['url'])
    web_address = Token().web_address()
    datas = database_query().invocation_interface(name, web_address, token,jsondata)
    return datas

'''获取登录账号的可填报积分项目树'''
def projectTree(users,type):
    data=Interface(users,'积分项目树二', {'keyWord':''})
    type_id={
        '产值积分':2,
        '公共积分':3,
        '部门积分':4,
        '固定积分':1
    }
    if data != -1:
        all_data = data['data']
        for i in all_data:
            if i['name'] == type:
                if len(i) > 1:
                    datas = random_sampling(i['childProjectTree'],'childProjectTree')
                    datas = datas[0]
                    datas['dimensionId'] = type_id[type]
                    return datas
        print('未找到填报项')
        return -1
'''填报积分'''
def addIntegral(users, Integraldata):
    test_user = Token().get_user(users['data'], users['url'])
    fg = time.strftime('%Y%m%d%H%M%S', time.localtime())
    remark = '接口测试' + fg
    jsondata = [{
        "applyIntegral": int(Integraldata['points']),
        "applyNum": 1,
        "applyUnit": Integraldata['unit'],
        "approvalId": "",
        "deptId": test_user['deptid'],
        "dimensionId": Integraldata['dimensionId'],
        "informantId": test_user['empno'],
        "remark": remark,
        "standardId": Integraldata['projectId']
    }]
    result = Interface(users, '积分填报', jsondata)

    return result
'''审批人信息'''
def audit_users(users,auditor):
    certifiCateNo=database_query().Execution('查询身份证号',*[auditor])
    users['data']['empno']=auditor
    users['data']['pwd']=str(certifiCateNo[0][0])[-6:]
    return users
'''审核积分提报'''
def integral_audit(users,approvalNo):
    # users['data'][]
    # token=Token().token_way()
    # empno_auditor=
    return



if __name__ == "__main__":
    # datas = projectTree({'url': 'http://oauth.jtyjy.com/api/oneLogin/sso',
    #                      'data': {'serverId': 29, 'empno': '20192', 'pwd': '067540'}, 'validate': 'None'},'公共积分')
    # # users=yamlFile().read_yaml("../otherdata/test.yaml")
    # test_addIntegral({'url': 'http://oauth.jtyjy.com/api/oneLogin/sso',
    #                   'data': {'serverId': 29, 'empno': '11881', 'pwd': '067540'},
    #                   'validate': 'None'}, datas)
    users={'url': 'http://oauth.jtyjy.com/api/oneLogin/sso',
                         'data': {'serverId': 29, 'empno': '11881', 'pwd': '067540'}, 'validate': 'None'}
    # Integraldata=projectTree(users,'公共积分')
    # addIntegral(users,Integraldata)
    # IntegralDeta=getIntegralDetailById(users,47316)
    # print(IntegralDeta)
    # audit_users(users,'11881')
    # IntegralDeta=Interface(users,'积分详情',{'id': 47316})
    # print(IntegralDeta)