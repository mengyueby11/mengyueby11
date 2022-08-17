import requests
api=
try:
    respon = requests.get(api,j).json()
except requests.exceptions.ReadTimeout as a:
    print("%s接口调用失败，失败原因：%s" % (api, a))
    return -1
else:
    print(respon)