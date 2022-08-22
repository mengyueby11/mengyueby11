
import pytest


data = [
    {"url": "https://www.baidu.com", "http": "get"},
    {"url": "https://www.google.com", "http": "post"}
]


@pytest.fixture(scope='function', params=data)
def f_function(request):
    print("fixture部分-url:{}".format(request.param['url']))
    print("fixture部分-http:{}".format(request.param['http']))
    return request.param

def test_add_by_func_aaa(f_function):
    print("测试用例-url：{}".format(f_function['url']))
    print("测试用例-http：{}".format(f_function['http']))

if __name__ == '__main__':
    pytest.main(['-v', '-s'])
