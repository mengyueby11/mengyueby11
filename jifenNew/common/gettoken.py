import requests


class Token():
    def web_address(self):
        address="http://testjf.jtyjy.com"
        return address
    #获取token
    def get_token(self,datas,url):
        # self.all_url='http://oauth.jtyjy.com/api/oneLogin/sso'
        try:
            respon=requests.get(url,params=datas,timeout=5).json()
        except Exception as e:
            print("token接口调用失败，失败原因：%s"%e)
        else:
            data=respon['data']
            #分割token
            token=data.split('=')[1]
            return token
    #token展示
    def token_way(self,datas,url,way=None):
        if way==1:
            return {'token':self.get_token(datas,url)}
        else:
            return 'token'+'='+self.get_token(datas,url)
    #获取登录账户的个人信息
    def get_user(self,datas,url_token):
        url='http://oauth.jtyjy.com/api/oneLogin/getAndFlush?'
        datas=self.token_way(datas,url_token,1)
        try:
            respon=requests.get(url,params=datas,timeout=5).json()
        except Exception as e:
            print("个人信息接口调用失败，失败原因：%s"%e)
        else:
            a=respon['data']
            user={}
            for key,value in a.items():
                if value!=None and value!=-1 and value!=0:
                    user[key]=value
            #断言
            assert respon['code']==0
            return user
# if __name__=='__main__':
#     Token=Token()
#     token=Token.get_user({'serverId': '29','empno': '21899','pwd': '024043'})
#     print(token)