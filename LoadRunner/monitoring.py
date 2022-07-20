# 对登录功能进行单点性能测试（一组测试数据）
# 发送首页请求，通过locust进行性能测试
from locust import HttpUser, task, TaskSet


# 定义测试类：用户行为
class UserBehavior(TaskSet):
    # 指定测试任务
    @task
    def test_login(self):
        self.client.get("/")


class WebSiteUser(HttpUser):
    host = "https://www.baidu.com/"
    tasks = [UserBehavior]
    min_wait = 2000
    max_wait = 5000
