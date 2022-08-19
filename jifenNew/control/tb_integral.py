from jifenNew.common import general
import time

'''获取登录账号的可填报积分项目树'''
def projectTree(users, type):
    data = general.Interface(users, '积分项目树二', {'keyWord': ''})
    if data != -1:
        all_data = data['data']
        for i in all_data:
            if i['name'] == type:
                if len(i) > 1:
                    datas = general.random_sampling(i['childProjectTree'], 'childProjectTree')
                    datas = datas[0]
                    datas['dimensionId'] = general.data.type_id[type]
                    return datas
        print('未找到填报项')
        return -1
'''填报积分'''
def addIntegral(users, Integraldata,approvalId=None):
    test_user = general.Token().get_user(users, general.data.token_url, general.data.users_url)
    fg = time.strftime('%Y%m%d%H%M%S', time.localtime())
    remark = '接口测试' + fg
    jsondata = [{
        "applyIntegral": int(Integraldata['points']),
        "applyNum": 1,
        "applyUnit": Integraldata['unit'],
        "approvalId": approvalId,
        "deptId": test_user['deptid'],
        "dimensionId": Integraldata['dimensionId'],
        "informantId": test_user['empno'],
        "remark": remark,
        "standardId": str(Integraldata['projectId'])
    }]
    result = general.Interface(users, '积分填报', jsondata)
    # print(result)
    if result != -1:
        return test_user['empno'], remark,jsondata
    else:
        return -1
'''查询审批信息'''
def integral_approval(empno, remark, approval_id=None):
    if approval_id == None:
        intergral_data = general.database_query().Execution('根据工号查询填报的积分', *[remark, empno])
        datas = {
            'approval_id': intergral_data[0][2],
            'status': intergral_data[0][-8],
            'reviewer': general.Users_Data(intergral_data[0][-6]),
            'id':intergral_data[0][0]
        }
    else:
        reviewer = general.database_query().Execution('查询积分审批人工号', *[approval_id])
        datas = {
            'approval_id': approval_id,
            'status': reviewer[0][1],
            'reviewer': general.Users_Data(reviewer[0][0]),
            'id': reviewer[0][0]
        }
    return datas
'''审批 status:1:通过 2:拒绝 3:驳回'''
def integral_audit(datas, status):
    while datas['status'] == 1 or datas['status'] == 2:
        jsondata = {
            'integralIds': str(datas['approval_id']),
            'remark': '测试接口',
            'status': status}
        result = general.Interface(datas['reviewer'], '审核积分提报', jsondata)
        if result == -1: return -1
        datas = integral_approval(1, 1, datas['approval_id'])
    return
# 清除积分提报数据
def intergral_dalete(empno, remak):
    result = general.database_query().ExecutionDel('根据工号清除积分提报数据', *[remak, empno])
    if result != -1:
        return result
    else:
        return -1
'''驳回详情'''
def integral_detail(users,empno, remak):
    datas=integral_approval(empno, remak)
    result=general.Interface(users,'积分驳回详情',{'id':datas['id']})
    if result!=-1:
        return result['data']
    else:
        return -1
# if __name__ == "__main__":
#     users=general.Users_Data(11881)
#     detail=integral_detail(users,11881,'1188120220818100546869669')
#     print(detail)
# #     approval=integral_approval(11881,'接口测试20220818150259')
# #     print(approval)
# #     result=intergral_dalete(11881,'接口测试20220818150259')
# #     print(result)

