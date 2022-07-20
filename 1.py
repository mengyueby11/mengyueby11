# import requests
#
# def Token():
#     token="http://oauth.jtyjy.com/api/oneLogin/sso?serverId=29&empno=16907&pwd=123456"
#
#     respon = requests.get(token).json()#请求接口
#     token=respon['data'].split("=")[1]
#     return token
# test_url="http://testjf.jtyjy.com"
# token=Token()
# token='token'+'='+token
#
# all_url=test_url+'/api/integral/save/111121?'+token
# print(all_url)
# jsondata=[{
#     "applyIntegral":300,
#     "applyNum":1,
#     "applyUnit":"次",
#     "approvalId":"",
#     "deptId": 531,
#     "dimensionId": 3,
# 	"informantId": "16907",
# 	"remark": "11111",
# 	"standardId": 1592
#     }]
# try:
#     test_01=requests.post(url=all_url,json=jsondata,timeout=5).json()
# except requests.exceptions.ReadTimeout as a:
#     print(a)
# else:
#     print(test_01)


# def sum(a,b,c=None):
#     print(c)
#
# sum(1,2,3)