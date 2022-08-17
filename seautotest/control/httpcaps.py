import requests
from seautotest.control.log import logger
from seautotest.control.utlis import iscompare_json,writetoken

def htpp_requests(step,junit,sort='get'):
    data=step['data'].replace("\n","")
    http_type,parmars=datataing(data)
    #记录为何不通过
    content=''
    #记录是否通过
    list_record=[]
    if http_type=='headers':
        httrequst=getattr(requests,sort)(step['element'],headers=eval(parmars))
        print(httrequst)
    else:
        httrequst=getattr(requests,sort)(step['element'],eval(parmars))
        print(httrequst)
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

if __name__ == '__main__':
    step = {'no': '1', 'testdot': '获取验证码功能验证', 'keyword': 'API', 'page': '',
            'element': 'http://127.0.0.1:8888/index',

            'data': "parmars={'phone': '17547817934', 'type': '1'}",

            'expected': "{'msg': '这是我开发的第一个接口', 'msg_code': 0}", 'output': {'msg': '这是我开发的第一个接口', 'msg_code': 0},

            'score': 'Pass', 'remark': '', '_keyword': 'API', '_element': '获取短信验证码',

            '_expected': "{'msg': '这是我开发的第一个接口', 'msg_code': 0}", '_output': ''}

    print(htpp_requests(step, 'get'))