import requests

class zentao_interface:
    def __init__(self):
        self.zentao_address = "http://127.0.0.1:80/zentao/api.php/v1"
        jsondata ={"account": "liubiying", "password": "liu+123456"}
        self.token=self.Token(jsondata)

    def  Token(self,jsondata):
        url = self.zentao_address + '/tokens'
        try:
            respon = requests.post(url, json=jsondata, timeout=5).json()
        except Exception as a:
            print("获取token失败，失败原因:%s" % a)
        else:
            token = respon['token']
            token={"token":token}
            return  token

    def zentao_projects(self):
        projects=[]
        url=self.zentao_address+'/projects'
        try:
            respon=requests.get(url,headers=self.token).json()
        except Exception as a:
            print("获取项目列表失败，失败原因:%s"%a)
        else:
            for i in respon['projects']:
                project={}
                project['id']=i['id']
                project['name'] = i['name']
                project['code']=i['code']
                projects.append(project)
        return projects


# #获取项目列表

if __name__ == '__main__':
    interfaces=zentao_interface()
    projects=interfaces.zentao_projects()
    print(projects)