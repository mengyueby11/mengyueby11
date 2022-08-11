import xlrd
import xlsxwriter
from pathlib import Path

# 操作Excel的工具类
class Excel():
# 初始化方法 参数type：为r是读取excel，为w是写入excel获取不同的实例，参数file_name是将要读取的文件
    def __init__(self,type,file_name):
        #读取excel
        if type=='r':
            #打开文件
            self.workbook=xlrd.open_workbook(file_name)
            self.sheet_names=self.workbook.sheet_names()
            #装载所有数据的list
            self.list_data=[]
            #将测试数据内调用的方法，改编成自定义里面的变量
            self.dict_data=[]
        #写入excel
        elif type=='w':
            self.workbook=xlsxwriter.Workbook(file_name)
        #获取到所有的sheet_names,sheetl,sheet2获取到所有，获取到的是一个list
    def read(self):
        #循环编辑
        for sheet_name in self.sheet_names:
