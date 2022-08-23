import datetime
import allure
import pytest
from jifenNewOne.common.readYaml import yamlFile
from jifenNewOne.common import general


@allure.feature('积分管理')
@allure.story('积分列表')
class TestIntegralMge():
    @allure.title('根据工号查询该账号可查看积分列表')
    @allure.tag('单个接口测试')
    # 设置测试用例的级别  blocker > critical > normal > minor > trivial
    # 1、 blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
    # 2、 critical级别：临界缺陷（ 功能点缺失）
    # 3、 normal级别：普通缺陷（数值计算错误）
    # 4、 minor级别：次要缺陷（界面错误与UI需求不符）
    # 5、 trivial级别：轻微缺陷（必输项无提示，或者提示不规范）
    @allure.severity('blocker')
    @allure.step("获取积分管理列表")
    @pytest.mark.parametrize('user', yamlFile().read_yaml('../otherdata/test.yaml'))
    def test_integral_management(self, user):
        # 用例描述
        """
            有token的情况下查询该账户可查询积分列表，接口正常返回查询的积分数据
        """
        users = general.Users_Data(user['empno'])
        ''' 获取积分管理 '''
        tokenDate = {
            'token': general.Token().get_token(users, general.data.token_url),
            'page': '1',
            'rows': '100',
            'deptId': '',
            'status': '',
            'standard': '',
            'dimensionId': '',
            'type': ''
        }
        result,api = general.Interface(users, '获取积分管理列表1', jsondata=tokenDate)
        numstr = '获取积分管理列表接口调用成功'
        print(f"执行时间：{datetime.datetime.now()}")
        print(f"接口调用成功，查询道的结果为{result['data']}")
        with allure.step("结果: {}".format(numstr)):
            pass
        return
    @allure.step('获取积分管理列表')
    @allure.title('无token查看积分列表')
    @allure.tag('单个接口测试')
    def test_invalid_token(self):
        # 用例描述
        """
            无token的情况下查询该账户可查询积分列表，接口返回未登录或登录已失效
        """
        respon, url_api = general.database_query().invocation_interface('获取积分管理列表', general.data.web_address)
        assert respon['msg'] == '未登录或登录已失效'
        assert respon['code'] == 10000
        result = "测试通过，测试结果为：\n%s" % respon['msg']
        with allure.step("结果: {}".format(result)):
            pass
        return


# if __name__ == '__main__':
#     pytest.main(['-vs', 'test_integral_list.py'])
