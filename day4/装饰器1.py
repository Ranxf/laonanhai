# 装饰器

"""
装饰器：“器”是函数的意思。装饰器本质是函数，基本语法一样是def定义的；
功能:是用来装饰其他函数的，为其他函数添加附加功能。
原则：1、不能修改被装饰的函数的源代码；2、不能修改被装饰的函数的调用方式；

实现装饰器知识储备
1.函数即“变量”
2.高阶函数
3.嵌套函数

装饰器+
"""
import time


def timmer(func):
    def warpper(*args, **kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the func run time is %s' %(stop_time - start_time))
    return warpper()


@timmer  # 装饰器
# 函数
def test1():
    time.sleep(3)
    print("in the test1")   # 代码块表示该函数实现的功能和逻辑

# 调用
test1()



