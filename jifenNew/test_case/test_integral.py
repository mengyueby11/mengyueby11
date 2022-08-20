import pytest
import allure
from jifenNew.common.readYaml import yamlFile
from jifenNew.control import tb_integral
#模块
@allure.feature('积分管理')
#子功能
@allure.story('提报积分')
@pytest.mark.parametrize('user', yamlFile().read_yaml('../otherdata/test.yaml'))
class TestIntegralMag():
    # fixture标记的函数可以应用于测试类外部,使用时users_info可以取函数返回值
    @pytest.fixture()
    def users_info(self,user):
        return tb_integral.general.Users_Data(user['empno'])
    def intergral(self,users,status):
        # print(user)
        # print('---------------查询个人账户信息-------------------\n')
        # # self.users = tb_integral.general.Users_Data(user['empno'])
        # # print(self.users)
        print('---------------随机生成填报项-------------------\n')
        with allure.step('获取提报项'):
            Integraldata = tb_integral.projectTree(users, '公共积分')
        assert Integraldata != -1
        try:
            print('---------------填报积分-------------------\n')
            with allure.step('填报积分'):
                empno, remark,Integral_jsondata = tb_integral.addIntegral(users, Integraldata)
            print(empno, remark)
        except Exception as e:
            print('填报积分失败,失败原因：%s'%e)
        else:
            print('---------------查询审核信息-------------------\n')
            with allure.step('查询提报积分详情'):
                approval_data = tb_integral.integral_approval(empno, remark)
            print(approval_data)
            assert approval_data != -1
            print('---------------审核-------------------\n')
            with allure.step('审核提报积分'):
                result = tb_integral.integral_audit(approval_data, status)
            assert result != -1
            datas={
                'empno':empno,
                'remark':remark,
                'Integral_jsondata':Integral_jsondata
            }
            return datas
    #提报通过
    #标题
    @allure.title('提报积分-审批：通过')
    # #用例级别
    # @allure.serverity(allure.serverity_level.BLOCKER)
    def test_auditIntegral_pass(self,users_info):
        datas=self.intergral(users_info,tb_integral.general.data.integral_status['通过'])
        with allure.step('测试通过删除测试数据'):
            print('---------------删除提报的积分-------------------\n')
            tb_integral.intergral_dalete(datas['empno'], datas['remark'])
    #提报拒绝
    @allure.title('提报积分-审批：不通过')
    def test_auditIntegral_reject(self, users_info):
        datas=self.intergral(users_info, tb_integral.general.data.integral_status['拒绝'])
        print('---------------删除提报的积分-------------------\n')
        with allure.step('测试通过删除测试数据'):
            tb_integral.intergral_dalete(datas['empno'], datas['remark'])
    # 提报驳回
    @allure.title('提报积分-审批：驳回-修改重新提交')
    def test_auditIntegral_overrule(self, users_info):
        datas=self.intergral(users_info, tb_integral.general.data.integral_status['驳回'])
        print('---------------驳回详情-------------------\n')
        with allure.step('查看驳回详情'):
            detail=tb_integral.integral_detail(users_info,datas['empno'], datas['remark'])
        print('---------------随机生成填报项-------------------\n')
        with allure.step('获取积分项'):
            Integraldata = tb_integral.projectTree(users_info, '公共积分')
        assert Integraldata != -1
        try:
            print('---------------驳回修改-------------------\n')
            with allure.step('修改驳回积分'):
                empno, remark, Integral_jsondata = tb_integral.addIntegral(users_info, Integraldata,detail['approvalId'])
            print(empno, remark)
        except Exception as e:
            print('驳回修改失败,失败原因：%s' % e)
        else:
            print('驳回修改成功')
if __name__ == "__main__":
    pytest.main(['-vs', 'test_integral.py'])

