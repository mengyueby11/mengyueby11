# -*- coding: utf-8 -*-
# @Time : 2022/3/11 11:46 
# @Author : daixilin
# @File : test_goods.py 
# @Project: newMarket
import requests
import pytest
import pymysql
import time
import json
from common import gettoken
from common.readCSV import readCSV
token='token'+'='+gettoken.get_token()
test_url ="http://testjf.jtyjy.com"
import random
#登录测试用例
"""
title=积分管理-积分填报接口测试

1.step1获取积分管理列表 >> expect 接口调用成功
2.step2获取积分项目>> expect 接口调用成功
3.step3填报积分>> expect 接口调用成功

"""
class TestIntegralMge():
    def test_integral_management(self):
        ''' 获取积分管理 '''
        all_url = test_url + readCSV().get_csv('testdata.csv','r')[1][2]+token#接口拼接
        test_01 = requests.get(all_url).json()
        assert test_01['code']==0
        assert test_01['msg']=='请求成功'
    @pytest.fixture()
    def test_user(self):
        all_url = readCSV().get_csv('testdata.csv', 'r')[4][2] + token  # 接口拼接
        try:
            all_info=requests.get(all_url).json()
        except requests .exceptions as a:
            print('接口调用失败：%s'%a)
        else:
            a=all_info['data']
            all_data=[]
            for i,j in a.items():
                all_data.append(j)
            user=[]
            dept=all_data[7]
            user.append(dept)
            empno=all_data[9]
            user.append(empno)
            assert all_info['code'] == 0
            return user
    @pytest.fixture()
    def test_projectTree(self):
        '''获取登录账号的可填报积分项目树'''

        all_url = test_url + readCSV().get_csv('testdata.csv', 'r')[2][2] + token  # 接口拼接
        test_01 = requests.get(all_url).json()
        assert test_01['code'] == 0
        all_data = test_01['data']
        all = []
        for i in range(len(all_data)):
            for x1, y1 in all_data[i].items():
                if y1 == '1-3':
                    all.append('3')
        if '3' in all:
            b = test_01['data'][-1]['childProjectTree']
            c = b[0]['childProjectTree']
            d = c[0]['childProjectTree']
            all.append(d[0]['value'])
            all.append(d[0]['points'])
        else:
            print('未找到公共积分缺勤扣分项')
        return all
    def test_addIntegral(self,test_user,test_projectTree):
        cn = pymysql.connect(host='192.168.2.31',
                             user='mysql',
                             passwd='123456',
                             database='jtyjy_integral_test',
                             charset='utf8')
        self.cursor = cn.cursor()
        # print(test_projectTree)
        # print(int(test_projectTree[2]))
        # print(test_projectTree[1].split('-')[1])
        # nowtime=time.strftime('%Y%m%d%H%M%S',time.localtime())
        num=random.randint(1, 1000000)
        all_url = test_url + readCSV().get_csv('testdata.csv', 'r')[3][2] +str(num)+'?'+ token  # 接口拼接
        fg = time.strftime('%Y%m%d%H%M', time.localtime())
        jsondata=[{"applyIntegral":int(test_projectTree[2]),
                   "applyNum":1,
                   "applyUnit":"",
                   "approvalId":"",
                   "deptId":test_user[0],
                   "dimensionId":test_projectTree[0],
                   "informantId":test_user[1],
                   "remark":"接口测试"+fg,
                   "standardId":test_projectTree[1].split('-')[1]}]
        try:
            test_01=requests.post(url=all_url,json=jsondata).json()
        except requests .exceptions as a:
            print('接口调用失败：%s'%a)
        else:
            assert test_01['code']==0
            try:
                sql = "select * from tb_integral where remark='接口测试"+fg+"'"+"and informant_id =" + test_user[1]
                print(sql)
                self.cursor.execute(sql)
            except:
                print('数据库查询失败')
            else:
                print('数据库查询成功')
                all = self.cursor.fetchall()
                if all:
                    print('测试数据添加成功')
                    try:
                        sql = "delete from tb_integral where remark='接口测试" + fg + "'" + "and informant_id =" + test_user[1]
                        self.cursor.execute(sql)
                    except:
                        print('清除数据失败')
                    else:
                        print('清除数据成功')
                else:
                    print('测试数据添加失败')
            print('接口调用成功')
        self.cursor.close()
if __name__ == "__main__":
    pytest.main(['-vs', 'test_integral.py'])