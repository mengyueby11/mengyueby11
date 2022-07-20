# -*- coding: utf-8 -*-
# @Time : 2022/3/11 11:35 
# @Author : daixilin
# @File : gettoken.py 
# @Project: newMarket
import requests
from common import readCSV
def get_token():
    all_url =readCSV.readCSV().get_csv('testdata.csv', 'r')[0][2]
    respon = requests.get(all_url).json()#请求接口
    data=respon['data']
    token=data.split('=')[1]#分割token
    return  token
if __name__=='__main__':
    print(get_token())