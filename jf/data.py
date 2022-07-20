# import pymysql
# from itertools import chain
# import pandas as pd
# import xlwt
# #打开数据库
# conn=pymysql.connect(host='192.168.2.31',
#                      user='mysql',
#                      passwd='123456',
#                      database='hr2020',
#                      charset='utf8')
#
# cursor=conn.cursor()
# # #sys_user
# # sys_user_dutyid=sql="SELECT dutyid FROM sys_user where useStatus in (0)"
# # try:
# #     cursor.execute(sys_user_dutyid)
# #     sys_user_dutyid_result=cursor.fetchall()
# #     sys_user_dutyid_result=list(chain.from_iterable(sys_user_dutyid_result))
# #     print(sys_user_dutyid_result)
# # except:
# #     conn.rollback()
# # # managerid
# # empNo=str(15603)
# # managerid="select empId from sys_user where empno in ("+empNo+")"
# # try:
# #     cursor.execute(managerid)
# #     managerid_result=cursor.fetchall()
# #     managerid_result=str(list(chain.from_iterable(managerid_result))[0])
# #     print(managerid_result)
# # except:
# #     conn.rollback()
# # #hr_hrmresource_manager
# # # hr_hrmresource_manager="SELECT dutyid FROM hr_hrmresource_manager where managerid in ("+managerid_result+")"
# #判断是否存在兼职
# # empno=7134
# # parttimeduty="select m.dutyId from emp_parttimeduty m where m.empId in (select u.empId from sys_user u where u.empno in ("+str(empno)+"))"
# # cursor.execute(parttimeduty)
# # parttimeduty_result=cursor.fetchall()
# # parttimeduty_result=list(chain.from_iterable(parttimeduty_result))
# #
# # if len(parttimeduty_result)>0:
# #     print(parttimeduty_result)
# # else:
# #     print("该用户无兼职")
# sql="select su.dutyId,su.empNo,m.parentId,su.empName,m.dutyName,n.titleName,a.fulldeptName from ((sys_duty m left join sys_user su on m.dutyid=su.dutyid)" \
#             "left join sys_title n on m.titleId=n.titleId)" \
#             "left join sys_department a on m.deptId=a.deptId where a.fullDeptName is not null or trim(a.fullDeptName)!='' " \
#             "and m.useStatus=0"
# cursor.execute(sql)
# result=cursor.fetchall()
# df = pd.DataFrame(list(result))
# #删除存在空值的行
# df=df.dropna(axis=0,how='any')
# instr=["dutyId","empNo","parentId","empName","dutyName","titleName","fulldeptName"]
# df.columns=instr
# print(df)
# cursor.close()
# conn.close()
#
#
# book=xlwt.Workbook(encoding='utf-8',style_compression=0)
# sheet=book.add_sheet('')

a=11
print("aaa=%s"%a)