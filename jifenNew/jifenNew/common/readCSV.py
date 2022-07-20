# -*- coding: utf-8 -*-
# @Time : 2022/3/10 15:03 
# @Author : daixilin
# @File : readCSV.py 
# @Project: newMarket
import csv
import os
class readCSV():
    def get_csv(self,name,way):
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))#获取当前路径的上一级路径
        xlsPath=path+r'\otherdata'
        cls = []
        filepath=xlsPath
        filename=filepath+'\\'+name#文件名路径
        with open(filename,way) as f:
            reader=csv.reader(f)
            for i in reader:
                if i[0]!=u'序号':
                    cls.append(i)
        return cls

if __name__=='__main__':
    # print(readCSV().get_csv('testdata.csv','r'))
    print(readCSV().get_csv('testdata.csv','r')[0][2])