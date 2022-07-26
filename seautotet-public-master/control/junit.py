import timeit
from xml.dom.minidom import Document
from pathlib import Path
from control.data import gettime
from datetime import datetime
from control.log import logger


class Junit:
    def __init__(self):
        # 创建DOM文档对象
        self.doc = Document()
        self.pstarttime =  datetime.now()  # 程序开始时间
        # 创建用例套件集
        self.testsuites = self.doc.createElement('testsuites')
        self.doc.appendChild(self.testsuites)
        # 当前时间
        self.nowtime = gettime()
        # 创建用例套件
        self.testsuite = self.doc.createElement('testsuite')

    # 测试用例套件
    def suite(self, error, failures, tests, skips):
        # 错误用例的数量
        self.testsuite.setAttribute('errors', str(error))
        # 失败用例的数量
        self.testsuite.setAttribute('failures', str(failures))
        # 项目的名称
        self.testsuite.setAttribute('hostname', 'seautotest')
        # 用例数量
        self.testsuite.setAttribute('tests', str(tests))
        # 跳过用例的数量
        self.testsuite.setAttribute('skipped', str(skips))
        # 项目类型
        self.testsuite.setAttribute('name', 'API')
        # 时间
        self.testsuite.setAttribute('timestamp', str(datetime.isoformat(self.pstarttime)))

        self.settime()

    # 每条用例是一个case
    def case(self, id, title, time):
        # 创建case标签
        self.testcase = self.doc.createElement('testcase')
        # 用例的名称
        self.testcase.setAttribute('name', str(title))
        self.case_timer = time
        self.settime()
    # 跳过用例的case
    def skip_case(self, message):
        skip = self.doc.createElement('skipped')
        skip.setAttribute('message', message)
        self.testcase.appendChild(skip)

    # 设置时间
    def settime(self):
        # logger.info(self.time)
        endtime = datetime.now()
        # 单个用例的执行时间
        td = endtime - self.case_timer
        time = float(
            (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10 ** 6)) / 10 ** 6
        self.testcase.setAttribute('time', str(time))
        self.testcase.setAttribute('priority', 'M')
        self.testsuite.appendChild(self.testcase)

    # 失败的用例
    def failure(self, message):
        # 创建失败用例的标签
        failure = self.doc.createElement('failure')
        # 为什么失败了这个用例
        failure.setAttribute('message', str(message))
        # 类型为失败
        failure.setAttribute('type', 'Failure')
        # 添加到testcase下
        self.testcase.appendChild(failure)

    # 生成xml  是allure的数据源
    def write_toxml(self):
        # 计算执行的时间， 用当前时间-开始时间 是总耗时
        td = datetime.now() - self.pstarttime
        td_time = float(
            (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10 ** 6)) / 10 ** 6
        self.testsuite.setAttribute('time', '%s' % td_time)
        self.testsuites.appendChild(self.testsuite)
        file = Path('control/junit') / ('API' + '-' + 'ReportJunit@' + self.nowtime + '.xml')
        f = open(file, 'w')
        self.doc.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='gbk')
        f.close()
