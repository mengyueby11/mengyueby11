import pytest
from jifenNew.common.readYaml import yamlFile
from jifenNew.control import tb_integral

@pytest.mark.parametrize('user',yamlFile().read_yaml('../otherdata/test.yaml'))
class TestIntegralMag():
    def intergral(self,user,status):
        print(user)
        print('---------------查询个人账户信息-------------------\n')
        self.users = tb_integral.general.Users_Data(user['empno'])
        print(self.users)
        print('---------------随机生成填报项-------------------\n')
        Integraldata = tb_integral.projectTree(self.users, '公共积分')
        assert Integraldata != -1
        try:
            print('---------------填报积分-------------------\n')
            empno, remark,Integral_jsondata = tb_integral.addIntegral(self.users, Integraldata)
            print(empno, remark)
        except Exception as e:
            print('填报积分失败,失败原因：%s'%e)
        else:
            print('---------------查询审核信息-------------------\n')
            approval_data = tb_integral.integral_approval(empno, remark)
            print(approval_data)
            assert approval_data != -1
            print('---------------审核-------------------\n')
            result = tb_integral.integral_audit(approval_data, status)
            assert result != -1
            datas={
                'empno':empno,
                'remark':remark,
                'Integral_jsondata':Integral_jsondata
            }
            return datas
    #提报通过
    def test_auditIntegral_pass(self,user):
        datas=self.intergral(user,tb_integral.general.data.integral_status['通过'])
        print('---------------删除提报的积分-------------------\n')
        tb_integral.intergral_dalete(datas['empno'], datas['remark'])
    #提报拒绝
    def test_auditIntegral_reject(self, user):
        datas=self.intergral(user, tb_integral.general.data.integral_status['拒绝'])
        print('---------------删除提报的积分-------------------\n')
        tb_integral.intergral_dalete(datas['empno'], datas['remark'])
    # 提报驳回
    def test_auditIntegral_overrule(self, user):
        datas=self.intergral(user, tb_integral.general.data.integral_status['驳回'])
        print('---------------驳回详情-------------------\n')
        detail=tb_integral.integral_detail(self.users,datas['empno'], datas['remark'])
        print('---------------随机生成填报项-------------------\n')
        Integraldata = tb_integral.projectTree(self.users, '公共积分')
        assert Integraldata != -1
        try:
            print('---------------驳回修改-------------------\n')
            empno, remark, Integral_jsondata = tb_integral.addIntegral(self.users, Integraldata,detail['approvalId'])
            print(empno, remark)
        except Exception as e:
            print('驳回修改失败,失败原因：%s' % e)
        else:
            print('驳回修改成功')



if __name__ == "__main__":
    pytest.main(['-vs', 'test_integral.py'])

