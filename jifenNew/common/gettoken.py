import requests


class Token():
    #获取token
    def get_token(self,datas,url):
        respon=requests.get(url,params=datas,timeout=5).json()
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
    def get_user(self,datas,url_token,users_url):
        # url='http://oauth.jtyjy.com/api/oneLogin/getAndFlush?'
        datas=self.token_way(datas,url_token,1)
        respon=requests.get(users_url,params=datas,timeout=5).json()
        a=respon['data']
        user={}
        for key,value in a.items():
            if value!=None and value!=-1 and value!=0:
                    user[key]=value
        #断言
        assert respon['code']==0
        return user
