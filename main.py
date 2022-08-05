#
# import time
#
# import datetime as datetime
#
# Time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
#
# startDate=datetime.datetime.now()
# endDate=startDate+datetime.timedelta(days = 7)
# print(startDate.strftime("%Y-%m-%d"))
# print(endDate.strftime("%Y-%m-%d"))
jsondata={'id': 377, 'isAgree': 1, 'remark': ''}
# for i in ar.keys():
#     print(i)
#     print(ar[i])
s_api=''
# for i in jsondata.keys():
#     print(i)
#     if jsondata[i]==None:
#         s_api=s_api+"&%s="%(str(i))
#     else:
#         s_api = s_api + "&%s=%s" % (str(i), str(jsondata[i]))
for key,value in jsondata.items():
    s_api = str(s_api) + "&%s=%s" % (key,value)
print(s_api)