import datetime
import allure
import pytest
from jifenNewOne.common import general
from jifenNewOne.common import readXlsx
def general_datas():
        file_name= '../otherdata/interface_general.xlsx'
        datas=readXlsx.Excel('r',file_name).general_data()
        return datas
class Test_general_interface():
    @pytest.fixture(params=general_datas())
    def f_function(self,request):
        if request!=-1:
            return request.param
    @allure.step('接口调用')
    @allure.description('仅单个接口是否可用，不测试其他逻辑')
    @pytest.mark.usefixtures('f_function')
    def test_interface(self,f_function):
        assert f_function!=-1
        print(f_function)
        allure.dynamic.feature(f_function['所属模块'])
        allure.dynamic.title(f_function['用例标题'])
        allure.dynamic.severity(f_function['severity'])
        allure.dynamic.tag('单个接口测试')
        users=general.Users_Data(f_function['empno'])
        assert users!=-1
        print("个人数据为:%s"%users)
        if f_function['datas']==None and f_function['token']==0:
                respon, url_api=general.database_query().invocation_interface(f_function['接口'],general.data.web_address)
                allure.dynamic.testcase(url_api)
                assert respon['msg'] == '未登录或登录已失效'
                assert respon['code'] == 10000
                result="测试通过，测试结果为：\n%s"%respon['msg']
                with allure.step("结果: {}".format(result)):
                    pass
                return result
        elif f_function['datas']!=None and f_function['token']==1:
            result,api=general.Interface(users, f_function['接口'], f_function['datas'])
            allure.dynamic.testcase(api)
            assert result['code'] == 0
            numstr = '获取积分管理列表接口调用成功'
            print(f"执行时间：{datetime.datetime.now()}")
            print(f"接口调用成功，查询道的结果为{result['data']}")
            with allure.step("结果: {}".format(numstr)):
                pass
            return numstr
# if __name__ == '__main__':
#     # general_datas()
#     pytest.main(['-vs', 'test_general_interface.py'])
