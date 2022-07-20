# 参考文章：https://blog.csdn.net/swinfans/article/details/88915176
import os
from locust import TaskSet, task, HttpUser


# 创建任务类
class Test1(TaskSet):
    def on_start(self):
        # 初始化方法on_start，相当于setup
        print('初始化方法')

    @task
    # @task装饰器加到定义的方法前面表示这个方法就是一个可执行任务，装饰方法中可以添加数字（@task(2)），表示执行任务的执行次数的比例
    def getindex(self):
        """
        在Locust类中具有一个client属性，它对应着虚拟用户作为客户端所具备的请求能力(请求方法)。
        通常情况下不会直接使用Locust类，因为其client属性没有绑定任何方法，所以在使用Locust时需要先继承Locust类，
        然后再继承子类中的client属性中绑定客户端的现实类。client的post和get方法同requests类。
        :return:
        """
        req = self.client.get('/', name='测试', catch_response=True)
        # 添加断言必须在请求方法中设置catch_ response参数，值为True
        if req.status_code == 200:
            req.success()
        else:
            req.failure('失败')

    def on_stop(self):
        # 清除方法，相当于teardown
        print('清除方法')


# 创建用户类
class BI(HttpUser):
    # wait_time = between()   设置运行过程中的间隔时间，需要在locust中引入between
    tasks = [Test1]
    min_wait = 1000
    max_wait = 2000
    host = 'http://127.0.0.1:81'


if __name__ == '__main__':
    os.system('locust -f testindex.py')