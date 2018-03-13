"""
为什么要使用函数：减少重复代码;使程序变得可扩展；使程序变得易维护
日志文件处理（框架搭建必须有的）
"""
import time


def logger():
    time_format = '%Y-%m-%d %X'  # 年月日，时分秒
    time_current = time.strftime(time_format)
    with open('a.txt', 'a+') as f:
        f.write('%s end action\n' % time_current)       # 类似写日志文件


# 模拟一个功能，并将日志文件写入日志文件
def test1():
    """文档描述"""
    print('in the test1')  # 日志追加
    logger()      # 写入日志


# 模拟另外一个功能
def test2():
    print('in the test2')  # 日志描述
    logger()  # 写入日志


# 模拟第三个功能
def test3():
    print('in the test3')
    logger()  # 写入日志

# 调用各个功能模块
test1()
test2()
test3()

