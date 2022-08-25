import requests

def token(url,jsondata):
    url=url+'/tokens'
    respon=requests.post(url,json=jsondata,timeout=5).json()
    print(respon)

if __name__ == '__main__':
    jsondata={"account": "liubiying", "password": "liu+123456"}
    zentao_address="http://127.0.0.1:80/zentao/api.php/v1"
    token(zentao_address,jsondata)