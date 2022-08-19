import pytest
from jifenNew.common.readYaml import yamlFile
from jifenNew.common import general

class Test_token():
    '''
    数据驱动 ：其实就是测试用例的数据放到excel，yaml，csv，mysql，然后通过去改变数据达到改变测试用例的执行结果
    @pytest.mark.parametrize(args_name,args_value)
    args_name：参数名，字符串，多个参数中间用逗号隔开
    args_value：参数值（列表，元组，字典列表，字典元组），有多个值用例就会执行多少次，是list,多组数据用元祖类型;传三个或更多参数也是这样传。list的每个元素都是一个元组，元组里的每个元素和按参数顺序一一对应
    '''
    @pytest.mark.parametrize('users',yamlFile().read_yaml('../otherdata/test.yaml'))
    def test_token(self,users):
        users['empno']
        users=general.Users_Data(users['empno'])
        token=general.Token().get_token(users, jifenNew.otherdata.data.token_url)
        return token

if __name__=='__main__':
    '''
    pytest.main()：main中传入不同的指令用以执行指定测试用例
    -s: 显示程序中的print/logging输出
    -v: 丰富信息模式, 输出更详细的用例执行信息
    -q: 安静模式, 不输出环境信息
    -k：关键字匹配，用and区分：匹配范围（文件名、类名、函数名）
    '''
    pytest.main(['-vs','gettoken.py'])