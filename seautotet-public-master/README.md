
#### 2020年1月21日更新
#### 1.headers 在element可以进行默认配置
#### 2.单独提取出来需要断言的内容
#### 3.优化代码结构
#### 4.接口返回数据关联
#### 5.可以参考用例表的写法

#### 接口自动化测试实战
##### 这是一个从0到1的过程，一步一步搭建的测试接口框架，本教程从开始写框架的思路，和实现过
程深入解析，并且深入到了每个相关的的各个细节，不论你是刚入门的菜鸟，还是一个懂编码经验的工
程师，相信本系列的文章都会对你有所帮助。
##### 你即可以学到从0到1搭建自动化的编码思想，也可以改变成一个接口自动化工具，在需要的时候
可以自己更改代码和维护。
#### 你可以收获什么？
##### 1.完善python基础和编程思
##### 2.有一个设计测试框架思维
##### 3.提升自己能力，在也不怕面试没有编码经验
##### 4.一个可以拿出手的项目，简历中的一个亮点
##### 5.干货分享相比搜索到各种知识，这篇文章或许略有难度，但收获一定是你想不到的
#### 我们的设计思想如下：
- 语言：python3.7
- 请求：requests
- 测试报告：allure测试报告和Excel测试报告并邮件发送测试报告
- 维护：只需要维护Excel表格，表格执行pythoon代码
- 兼容性：向后兼容性强，可以在接口自动化完善的基础上增加 web ui app ui 自动化测试
#### 框架支持如下功能：
- **支持成千上万条接口用例进行测试（经过测试中配电脑，3分钟执行完成5000条接口测试）**
- **详细的Excel测试报告和美观的allure报告输出（这里能让你掌握自定义allure报告）**
- **支持不同类型上传文件（base64，md5，file）上传文件格式**
- **本框架采用多线程和单例等设计模式，代码简单而简约适合初中级学者，使用学习**
- **摆脱普通的测试框架和断言框架的约束，他们能做到的我们一样也可以，学习简单~**
#### 接口自动化篇：
##### [接口自动化第一章之-介绍篇]
(https://blog.csdn.net/weixin_45344334/article/details/94433426)
##### [接口自动化第二章之-封装读取excel工具类]
(https://blog.csdn.net/weixin_45344334/article/details/94457884)
##### [接口自动化第三章之-读取elemen表格数据]
(https://blog.csdn.net/weixin_45344334/article/details/94464861)
##### [接口自动化第四章之-读取用例表格数据]
(https://blog.csdn.net/weixin_45344334/article/details/94492898)
##### [接口自动化第五章之-封装requests请求增加log日志类]
(https://blog.csdn.net/weixin_45344334/article/details/94495117)
##### [接口自动化第六章之-返回结果和预期结果进行格式对比]
(https://blog.csdn.net/weixin_45344334/article/details/94497629)
##### [接口自动化第七章之-完善框架结构，增加allure测试报告]
(https://blog.csdn.net/weixin_45344334/article/details/94499604)
##### [接口自动化第八章之-进行jenkins持续集成]
(https://blog.csdn.net/weixin_45344334/article/details/94500183)

####  接下来详细介绍工具的如何使用！！！
#####  1.分两个Excel来控制脚本,第一个我们取名为elements.xlsx,第二个取名testcase.xlsx
#####  element.xlsx主要是管理接口的ip和链接，方便后面增加ui自动化存放元素：
![elements.xlsx](http://ptzwwmtq3.bkt.clouddn.com/FmRT3VqUzBqLnHR7Bx_aqhLRgElb)
- key：代表的接口名字（不能重复的哦，唯一表示名字）
- type：接口的请求类型（如post，get等等）
- value：是接口的链接（是接口后面的链接哦，如/webapi这种）
##### testcase.xlsx主要用于管理测试步骤和测试数据等：
**testcase的表格设计如下：**
![testcase.xlsx](http://ptzwwmtq3.bkt.clouddn.com/Fsq5S8E_hyEyIhxzjxwtJ1wQn12V)
![testcase.xlsx](http://ptzwwmtq3.bkt.clouddn.com/FkqBoQNBMghYKddQBlx4zSjq2b6W)


#####  Excel报告如下：
![](http://ptzwwmtq3.bkt.clouddn.com/FtPcakfeoJ1Y4ddMC7gRbaZxk0de)

![](http://ptzwwmtq3.bkt.clouddn.com/FrCO0QjnuhYH-o-sLF8EsztrAJc2)

#####  接下来贴出代码结构：
![](http://ptzwwmtq3.bkt.clouddn.com/FqsNh_pf_FgCQgaTvZQE1n7bgMsG)
![](http://ptzwwmtq3.bkt.clouddn.com/Fh3oWrMMyDbrP0t1LNnv2wijTxV_)
![](http://ptzwwmtq3.bkt.clouddn.com/Fl5SLl5HHJP044FWrO7hNfOuLFmY)
#####  config：文件内是存储一些常量，比如存入接口的token唯一标识码等，存入代码生成的手机号
，方便接口接下来的使用等
#####  element：里面存放的是接口的相关配置第一个Excel
#####  junit：生成xml报告，用于allure测试报告展示的数据
#####  control：
- autotest.py:初始化数据，解析Excel数据，记录请求过程，生成测试报告
- data.py:进行Excel读取的数据，进行重组，得到到可以执行的json结构
- httpcaps.py:封装请求，记录用例结果，将结果返回至autotest.py
- junit.py:生成xml测试报告用于展示allure
- log.py:日志类，将输出的日志写到下面的log文件夹内
- testcase.py:执行测试用例
#####  utlis.py:工具类，封装常用的函数
#####  lib：里面存储的是自定义方法，可以在Excel调用函数
#####  log：输出log文件，记录log产生的日志
#####  report：输出excel测试报告
#####  testcase:用例文件
#####  httpstart：调用执行用例，是否生成报告和发送邮件等
#####  如果你想直接获得源码可以加qq群，来一起学习进步。
##### [接口自动化第二章，开始继续学习吧~]
(https://blog.csdn.net/weixin_45344334/article/details/94457884)
**源码下载地址复制地址打开，不然会没有权限：https://gitee.com/zhangmeng1314/seautotet-
public.git**

**qq群：234922431**
