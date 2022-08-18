import pytest
from jifenNew.common.readYaml import yamlFile
from jifenNew.common.readMysql import database_query
from jifenNew.common.gettoken import Token
import random
import time


@pytest.mark.parametrize('users',yamlFile().read_yaml('../otherdata/test.yaml')[0])
class TestIntegralMag():
    '''
    fixture是pytest特有的功能
    用pytest.fixture标识，定义在函数前面。
    在你编写测试函数的时候，你可以将此函数名称做为传入参数，pytest将会以依赖注入方式，将该函数的返回值作为测试函数的传入参数
    conftest.py 配置里可以实现数据共享，不需要 import 就能自动找到fixture
    scope=“module” 可以实现多个.py 跨文件共享前置
    scope=“session” 以实现多个.py 跨文件使用一个 session 来完成多个用例
    1.scope：可以理解成fixture的作用域，默认：function，还有class、module、package、session四个【常用】
    2.autouse：默认：False，需要用例手动调用该fixture；如果是True，所有作用域内的测试用例都会自动调用该fixture
    3.name：默认：装饰器的名称，同一模块的fixture相互调用建议写个不同的name
    @pytest.fixture(scope="function", params=None, autouse=False, ids=None, name=None)
   '''
    @pytest.fixture()
    def projectTree(self, users):
        # 随机取值
        def random_sampling(datas):
            datas = random.sample(datas, 1)
            if "childProjectTree" in str(datas[0]['childProjectTree']):
                return random_sampling(datas[0]['childProjectTree'])
            else:
                return datas
        '''获取登录账号的可填报积分项目树'''
        web_address = Token().web_address()
        jsondata = {}
        jsondata['keyWord'] = ''
        token = Token().token_way(users['data'], users['url'])
        data = database_query().invocation_interface('积分项目树', web_address, token, jsondata)
        assert data != 0 - 1
        all_data = data['data']
        for i in all_data:
            if i['name'] == '公共积分':
                if len(i) > 1:
                    datas = random_sampling(i['childProjectTree'])
                    datas=datas[0]
                    datas['dimensionId']=3
                    return datas
        print('未找到填报项')
        return -1
    def test_addIntegral(self,users,projectTree):
        '''填报积分'''
        test_user=Token().get_user(users['data'], users['url'])
        fg=time.strftime('%Y%m%d%H%M%S', time.localtime())
        remark = '接口测试' + fg
        jsondata=[{
            "applyIntegral":int(projectTree['points']),
            "applyNum": 1,
            "applyUnit":projectTree['unit'],
            "approvalId": "",
            "deptId":test_user['deptid'],
            "dimensionId":projectTree['dimensionId'],
            "informantId":test_user['empno'],
            "remark":remark,
            "standardId":projectTree['projectId']
        }]
        token = Token().token_way(users['data'], users['url'])
        web_address=Token().web_address()
        result=database_query().invocation_interface('积分填报',web_address,token,jsondata)
        assert result != 0 - 1
        return result

if __name__ == "__main__":
    # datas=IntegralMag().projectTree({'url': 'http://oauth.jtyjy.com/api/oneLogin/sso',
    #                             'data': {'serverId': 29, 'empno': '20192', 'pwd': '067540'}, 'validate': 'None'})
    pytest.main(['-vs', 'test_integral.py'])
    # users=yamlFile().read_yaml("../otherdata/test.yaml")
    # IntegralMag().addIntegral({'url': 'http://oauth.jtyjy.com/api/oneLogin/sso',
    #                                     'data': {'serverId': 29, 'empno': '11881', 'pwd': '067540'},
    #                                     'validate': 'None'},datas)
