# -*- coding: utf-8 -*-
# @Time : 2022/3/11 11:46 
# @Author : daixilin
# @File : test_goods.py 
# @Project: newMarket
import requests
import time
from common import gettoken
from common.readCSV import readCSV

token='token'+'='+gettoken.get_token()
test_url ="http://testjf.jtyjy.com"
#登录测试用例
class TestIntegralMge:
    def test_integral_management(self):
        ''' 获取积分管理 '''
        all_url = test_url + readCSV().get_csv('testdata.csv','r')[1][2]+token#接口拼接
        test_01 = requests.get(all_url).json()
        assert test_01['code']==0
        assert test_01['msg']=='请求成功'
    def test_projectTree(self):
        all_url = test_url + readCSV().get_csv('testdata.csv', 'r')[2][2] + token  # 接口拼接
        test_01 = requests.get(all_url).json()
        assert test_01['code']==0
    def test_addIntegral(self):
        nowtime=time.strftime('%Y%m%d%H%M%S',time.localtime())

        all_url = test_url + readCSV().get_csv('testdata.csv', 'r')[3][2] +nowtime+'?'+ token  # 接口拼接

        jsondata=[{"applyIntegral":13,"applyNum":1,"applyUnit":"13/小时","approvalId":"","deptId":478,"dimensionId":3,"informantId":"20192","remark":"","standardId":1530}]
        test_01=requests.post(url=all_url,json=jsondata).json()
        assert test_01['code']==0