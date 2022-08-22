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
        print("执行%s语句" % sql)
        self.testjf_cur.execute(sql)
        print("%s语句执行成功" % sql)
        sql = self.testjf_cur.fetchall()
        assert len(sql) > 0
        print("查询到的数据为：%s" % sql)
        sql = list(chain.from_iterable(sql))
        return sql

    # 执行sql语句
    def Execution(self, type, *args):
        sql = "select sentence,hr from inquire where type in ('%s')"
        sql = self.Data_Query(sql, type)
        print("数据库查询的数据为:%s" % sql)
        assert sql != -1
        if sql[1] == 0:
            print("执行%s语句" % sql[0])
            self.jtyjy_cur.execute(sql[0], args)
            print("%s数据查询成功\n" % sql[0])
            result = self.jtyjy_cur.fetchall()
            assert len(result) > 0
            return result
        elif sql[1] == 1:
            print("执行%s语句" % sql[0])
            self.hr2020_cur.execute(sql[0], args)
            print("%s数据查询成功\n" % sql[0])
            result = self.hr2020_cur.fetchall()
            assert len(result) > 0
            return result

    # 删除数据
    def ExecutionDel(self, type, *args):
        sql = "select sentence,hr from inquire where type in ('%s')"
        sql = self.Data_Query(sql, type)
        print("数据库查询的数据为:%s" % sql)
        # print(sql)
        assert sql != -1
        if sql[1] == 0:
            print("执行%s语句删除" % sql[0])
            self.jtyjy_cur.execute(sql[0], args)
            self.jtyjy_integral_test.commit()
            row = self.jtyjy_cur.rowcount
            assert row != 0
            print("%s语句删除成功\n" % sql[0])
            return row
        elif sql[1] == 1:
            print("执行%s语句删除" % sql[0])
            self.hr2020_cur.execute(sql[0], args)
            self.hr2020.commit()
            row = self.hr2020_cur.rowcount
            assert row != 0
            print("%s语句删除成功\n" % sql[0])
            return row

    # 接口判断
    def invocation_interface(self, name, web_address, token=None, jsondata=None):
        sql = "select api,Post,code from interface where name in ('%s')"
        # 查询接口
        api = self.Data_Query(sql, name)
        print("查询到的接口为%s" % api)
        # 获取项目网址
        assert api != -1
        # 接口地址拼接
        url_api = str(web_address + api[0])
        print("拼接后的接口地址为：%s" % url_api)
        # print(url_api)
        # get
        if api[1] == 0:
            if token != None:
                respon = requests.get(url_api % token, params=jsondata, timeout=5).json()
                return respon, url_api % token
            else:
                respon = requests.get(url_api, params=jsondata, timeout=5).json()
                return respon, url_api
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
        test_01 = requests.post(url=url_api, json=jsondata, timeout=5).json()
        return test_01, url_api

    # 结果判断
    def result_info(self, test_01, api):
        print("%s接口调用判断" % api)
        assert test_01['code'] == 0
        print("接口调用成功!")
        return test_01

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
