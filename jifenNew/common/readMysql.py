import pymysql
from itertools import chain
import requests
import random


# 数据库查询
class database_query:
    # 数据库连接
    def __init__(self):
        self.Connect_mysql()

    # 语句数据查询
    def Data_Query(self, sql, name):
        sql = sql % name
        # print(sql)
        try:
            self.testjf_cur.execute(sql)
        except Exception as e:
            print('语句数据库查询失败: %s\n失败原因：%s' % (name, e))
        else:
            sql = self.testjf_cur.fetchall()
            # print(sql)
            if len(sql) > 0:
                sql = list(chain.from_iterable(sql))
                return sql

            else:
                print("未查询到该数据: %s\n" % name)
                return -1

    # 执行sql语句
    def Execution(self, type, *args):
        sql = "select sentence,hr from inquire where type in ('%s')"
        sql = self.Data_Query(sql, type)
        # print(sql)
        if sql != -1:
            if sql[1] == 0:
                try:
                    self.jtyjy_cur.execute(sql[0], args)
                except Exception as e:
                    print('数据查询失败: %s\n失败原因：%s' % (sql[0], e))
                else:
                    print("数据查询成功\n")
                    result = self.jtyjy_cur.fetchall()
                    # print(result)
                    if len(result) > 0:
                        return result
                    else:
                        print("%s查询结果为空\n"%type)
                        return -1
            elif sql[1] == 1:
                try:
                    self.hr2020_cur.execute(sql[0], args)
                except Exception as e:
                    print('数据查询失败: %s\n失败原因：%s' % (sql[0], e))
                else:
                    print("数据查询成功\n")
                    result = self.hr2020_cur.fetchall()
                    if len(result) > 0:
                        return result
                    else:
                        print("%s查询结果为空\n", sql[0])
                        return -1
    #删除数据
    def ExecutionDel(self, type, *args):
        sql = "select sentence,hr from inquire where type in ('%s')"
        sql = self.Data_Query(sql, type)
        # print(sql)
        if sql != -1:
            if sql[1] == 0:
                try:
                    self.jtyjy_cur.execute(sql[0], args)
                    self.jtyjy_integral_test.commit()
                except Exception as e:
                    print('原始数据库查询失败: %s\n失败原因：%s' % (sql[0], e))
                else:
                    row=self.jtyjy_cur.rowcount
                    if row==0:
                        print("%s语句删除失败\n" % sql[0])
                        return row
                    else:
                        print("数据库删除成功！\n")
                        return 0
            elif sql[1] == 1:
                try:
                    self.hr2020_cur.execute(sql[0], args)
                    self.hr2020.commit()
                except Exception as e:
                    print('原始数据库查询失败: %s\n失败原因：%s' % (sql[0], e))
                else:
                    row=self.hr2020_cur.rowcount
                    if row == 0:
                        print("%s语句删除失败\n" % sql[0])
                        return row

                    else:
                        print("数据库删除成功！\n")
                        return -1
    # 接口判断
    def invocation_interface(self, name, web_address, token=None, jsondata=None):
        sql = "select api,Post,code from interface where name in ('%s')"
        # 查询接口
        api = self.Data_Query(sql, name)
        # 获取项目网址
        if api != -1:
            # 接口地址拼接
            url_api = str(web_address + api[0])
            # print(url_api)
            # get
            if api[1] == 0:
                try:
                    if token!=None:
                        respon = requests.get(url_api % token, params=jsondata, timeout=5).json()
                    else:
                        respon = requests.get(url_api , params=jsondata, timeout=5).json()
                except requests.exceptions.ReadTimeout as a:
                    print("%s接口调用失败，失败原因：%s" % (url_api % token, a))
                    return -1
                else:
                    if token != None:
                        return respon,url_api % token
                    else:
                        return respon,url_api
            # post
            elif api[1] == 1:
                # 地址中含随机数code
                if api[2] == 1:
                    random_value = random.randint(10000, 1000000)
                    return self.execute_interface_post(url_api % (str(random_value), token), jsondata)
                else:
                    return self.execute_interface_post(url_api % token, jsondata)
    # post接口执行
    def execute_interface_post(self, url_api, jsondata):
        try:
            test_01 = requests.post(url=url_api, json=jsondata, timeout=5).json()
        except requests.exceptions.ReadTimeout as a:
            print("%s接口调用失败，失败原因：%s" % (url_api, a))
            return -1
        else:
            return test_01, url_api
    # 结果判断
    def result_info(self, test_01, api):
        if test_01['code'] == 0:
            print("接口调用成功!")
            return test_01
        else:
            print("%s接口调用失败，失败原因：%s" % (api, test_01['msg']))
            return -1
    # 连接数据库
    def Connect_mysql(self):
        self.jtyjy_integral_test = pymysql.connect(host="192.168.2.31", user="mysql", password="123456",
                                                   db='jtyjy_integral_test')
        self.hr2020 = pymysql.connect(host="192.168.2.31", user="mysql", password="123456", db='hr2020')
        self.testjf_sql = pymysql.connect(host="192.168.2.31", user="mysql", password="123456", db='auto_test')
        self.jtyjy_cur = self.jtyjy_integral_test.cursor()
        self.hr2020_cur = self.hr2020.cursor()
        self.testjf_cur = self.testjf_sql.cursor()
    # 数据库关闭
    def Close_mysql(self):
        self.jtyjy_cur.close()
        self.jtyjy_integral_test.close()
        self.hr2020_cur.close()
        self.hr2020.close()
        self.testjf_cur.close()
        self.testjf_sql.close()
    # 关闭重新连接
    def Updata_mysql(self):
        self.Close_mysql()
        self.Connect_mysql()

# if __name__ == '__main__':
#     database = database_query()
#     # jsondata = {
#     #     "id": '424',
#     #     "isAgree": 1,  # 1:通过 2:拒绝 3:驳回,
#     #     "remark": ""
#     #
#     # }
#     jsondata=data.Jsondata(11881)
#     # print(jsondata)
#     token = Token().token_way({'serverId': '29', 'empno': '11881', 'pwd': '123'},
#                               'http://oauth.jtyjy.com/api/oneLogin/sso')
#     # database.invocation_interface('审核任务',token,jsondata)
#     database.invocation_interface('填报积分', token, jsondata)
