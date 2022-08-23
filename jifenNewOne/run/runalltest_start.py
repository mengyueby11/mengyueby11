#coding=utf-8
import pytest
import os
if __name__ == "__main__":
	result_dir='../result/xml/'
	report_dir='../result/html/'
	# test_case_dir='../test_general/test_general_interface.py'
	test_case_dir='../test_case'


	#需要安装allure pytest4.6.1版本，pip install pytest-html pip install pytest-rerunfailures
	pytest.main(['-v','--alluredir=%s'%result_dir,'--clean-alluredir',test_case_dir])
	'''
	注：参数详解：
	-s: 表示输出调试信息，包括print打印信息；
	-v: 显示更详细信息；
	-vs：两参数一起用。
	-q：以极简方式运行；	
	-n:：支持多线程或者分布式执行用例；
	如：pytets -vs ./test_case -n 2
			pytest.main(['-vs', './test_case', '-n=2'])
	--reruns NUM :失败用例重跑；
	-x: 只要出现一个用例报错，全部都停止；
	--maxfail=2:出现两个用例失败就停止；
	-k: 测试包含指定字符串用例；
	例：pytest -vs ./test_case -x "ao"
	--html ./report/report.html  :生成html测试报告
	'''
	ret=os.system('allure generate --clean %s -o %s'%(result_dir,report_dir))
	if ret:
		print('生成测试报告失败')
	else:
		print('生成测试报告成功')
	# -s表示控制台打印输出