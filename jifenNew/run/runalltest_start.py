#coding=utf-8
import pytest
if __name__ == "__main__":
	# 依次执行命令：　　
	#pytest test_allure.py - -alluredir =./ result - -clean - alluredir
	# allure serve. / result
	#allure generate --clean ../results/xml/ -o ../results/html/
	#./report/xml/ 第2部生成的数据集目录，
	# ./results/html/是生成html报告目录
	# -o是指向目标生成测试报告的目录；
	#需要安装allure pytest4.6.1版本，pip install pytest-html pip install pytest-rerunfailures
	pytest.main(['-s','-q','../test_case/','--alluredir','../results/xml'])
	# -s表示控制台打印输出
	# -vv显示用例详细结果
	# –alluredir ‘./report/xml’ 运行后的结果，是生成xml的数据集合目录