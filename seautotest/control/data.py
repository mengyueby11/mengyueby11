import re
from seautotest.lib import *
var=[]
# 这个方法是将自定义函数计算出来,eval函数可以用过字符的方法计算出结果内容，函数嵌套函数也是可以的
def json_data(data):
    # 正则匹配出 data 中所有的变量，返回列表 不包含这些内容则返回空
    keys=re.findall(r'<(.*?)>',data)
    # 返回是个list，采用替换的方法进行数据重组
    for r in keys:
        # 第一个参数是原来的值，第二个是参数是b.py传递过来的值
        data=data.replace('<'+r+'>',str(eval(r)))
    return data

if __name__=='__main__':
    data="<b.Jsondata(11881)>"
    print(json_data(data))