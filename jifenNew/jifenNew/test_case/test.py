# -*- coding: utf-8 -*-
# @Time : 2022/7/8 9:52 
# @Author : daixilin
# @File : test.py 
# @Project: jifenNew
import requests
import pytest
import time
import json
from common import gettoken
from common.readCSV import readCSV
token='token'+'='+gettoken.get_token()
test_url ="http://testjf.jtyjy.com"
@pytest.fixture()
def test_user():
        all_url = readCSV().get_csv('testdata.csv', 'r')[4][2] + token  # 接口拼接
        all_info=requests.get(all_url).json()
        a=all_info['data']
        all_data=[]
        for i,j in a.items():
            # print(j)
            all_data.append(j)
        dept=all_data[7]
        print(dept)
        assert all_info['code'] == 0
        return dept
def test_addIntegral(test_user):
        # a=self.test_user()
        nowtime=time.strftime('%Y%m%d%H%M%S',time.localtime())
        print(nowtime)
        all_url = test_url + readCSV().get_csv('testdata.csv', 'r')[3][2] +nowtime+'?'+ token  # 接口拼接
        print(all_url)
        jsondata=[{"applyIntegral":13,"applyNum":1,"applyUnit":"13/小时","approvalId":"","deptId":test_user,"dimensionId":3,"informantId":"20192","remark":"","standardId":1530}]
        test_01=requests.post(url=all_url,json=jsondata).json()
        assert test_01['code']==0
def test_projectTree():
        '''获取登录账号的可填报积分项目树'''
        all_url = test_url + readCSV().get_csv('testdata.csv', 'r')[2][2] + token  # 接口拼接
        print(all_url)
        test_01 = requests.get(all_url).json()
        assert test_01['code']==0
        all_data=test_01['data']
        all = []
        for i in range(len(all_data)):
            for x1,y1 in all_data[i].items():
                if y1=='1-3':
                    all.append('3')
        if '3' in all:
            b = test_01['data'][-1]['childProjectTree']
            c = b[0]['childProjectTree']
            d = c[0]['childProjectTree']
            all.append(d[0]['value'])
            all.append(d[0]['points'])
        else:
            print('未找到公共积分缺勤扣分项')

        print(all)

        # for i in range(len(all_data)):
        #     for x1,y1 in all_data[i].items():
        #         if y1=='1-3':
        #             all.append('3')
                # print(y1)
        all_2=[]
        all_3 = []
        # for i in range(len(all_data)):
        #     for item in all_data[i].items():
        #         if '1-3' in item:
        #             all.append('3')
        #         all_2.append(item)
        # a=(all_2[-1])
        # print(a)
        # for i in range(len(a[-1])):
        #     for item in a[i].items():
        #         all_3.append(item)

        # print(all_2)
        # print(all_3)
        # for j in range(len(y1)):
        #         for x2,y2 in y1.item():
        #         print(x2,y2)


        # print(all)
        # for i in range(len(all_data)):
        #     for j in all_data[i].values():
        #         print(j)
        #         all.append(j)
        # print(all[0])

# @pytest.fixture()
    # def test_user(self):
    #     all_url = readCSV().get_csv('testdata.csv', 'r')[4][2] + token  # 接口拼接
    #     all_info=requests.get(all_url).json()
    #     a=all_info['data']
    #     all_data=[]
    #     for i,j in a.items():
    #         # print(j)
    #         all_data.append(j)
    #     dept=all_data[7]
    #     assert all_info['code'] == 0
    #     return dept
    # def test_addIntegral(self,test_user):
    #     nowtime=time.strftime('%Y%m%d%H%M%S',time.localtime())
    #     print(nowtime)
    #     all_url = test_url + readCSV().get_csv('testdata.csv', 'r')[3][2] +nowtime+'?'+ token  # 接口拼接
    #     print(all_url)
    #     jsondata=[{"applyIntegral":13,"applyNum":1,"applyUnit":"13/小时","approvalId":"","deptId":test_user,"dimensionId":3,"informantId":"20192","remark":"","standardId":1530}]
    #     test_01=requests.post(url=all_url,json=jsondata).json()
    #     assert test_01['code']==0