import pymysql
#读取数据库脚本
def py_sql(SQLpath):
	db = pymysql.connect(host="192.168.2.31", user="mysql", password="123456", db="test001")
	c = db.cursor()
	try:
		with open(SQLpath,encoding='utf-8',mode='r') as f:#读取整个sql文件，以分号切割,[:-1]删除最后一个字符，也就是空字符串
			sql_list = f.read().split(';')[:-1]
			for x in sql_list:#判断包含空行的
				if '\n' in x:#替换空行为1个空格
					x = x.replace('\n', '')#判断多个空格时
				if ' ' in x:#替换为空
					x = x.replace('', '')#sql语句添加分号结尾
				global sql_item
				sql_item = x + ';'
				print(sql_item)
				c.execute(sql_item)
				print("成功sql: %s"%sql_item)
	except Exception as e:
		print(e)
		print('失败sql: %s'%sql_item)

	finally:
		c.close()
		db.commit()
		db.close()
if __name__ == '__main__':
	py_sql('../sqldata/test.sql')