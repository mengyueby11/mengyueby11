import requests

def Token(empNo):
    token = "http://oauth.jtyjy.com/api/oneLogin/sso?serverId=29&empno=" + str(empNo) + "&pwd=123456"
    respon = requests.get(token).json()  # 请求接口
    token = respon['data'].split("=")[1]
    token = 'token' + '=' + token
    return token
while True:
    url="http://testjf.jtyjy.com/mobile/home?"
    empNo=input("请输入工号：\n")
    if empNo=="T" or empNo=="t":
        break
    token = Token(empNo)
    print("\n")
    print(url+token)
    print("\n")