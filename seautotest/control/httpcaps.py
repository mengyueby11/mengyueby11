import requests
from seautotest.control.log import logger


def htpp_requests(step,junit,sort='get'):
    data=step['data'].replace("\n","")
    http_type,parmars=datataing(data)
    #记录为何不通过
    content=''
    #记录是否通过
    list_record=[]
    if http_type=='headers':
        httrequst=getattr(requests,sort)(step['element'],headers=eval(parmars))
#处理json类型和参数
def datataing(data):
    if data.strip():
        http_info=data.strip('=',1)
        #获得类型
        http_type=http_info[0]
        #获得请求的参数
        parmars=http_info[1]
    else:
        #获得类型
        http_type='parmars'
        #获得请求的参数
        parmars="{'':''}"
    return http_type,parmars