from jifenNew.common.readYaml import yamlFile
from jifenNew.common.gettoken import Token
class TestIntegralMag():
    # @pytest.fixture()
    def projectTree(self,users):
        token=Token().token_way(users['data'],users['url'])
        print(token)
        # data=readMysql.database_query().invocation_interface('积分项目树',token)
        # print(data)


if __name__ == "__main__":
    users=yamlFile().read_yaml('../otherdata/test.yaml')
    print(users)

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