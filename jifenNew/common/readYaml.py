import yaml
'''
YAML是一种直观的能够被电脑识别的的数据序列化格式
容易被人类阅读,容易和脚本语言交互
YAML类似于XML，但是语法比XML简单得多，对于转化成数组或可以hash的数据时是很简单有效的
'''
class yamlFile():
    def read_yaml(self,filepath):
        with open(filepath,mode='r',encoding="utf-8") as f:
            #load() :返回一个对象
            value=yaml.load(stream=f,Loader=yaml.FullLoader)
            return value
if __name__=='__main__':
    yamlFile().read_yaml('../otherdata/interface_general.yaml')