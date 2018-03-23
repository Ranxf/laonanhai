'''
Author:Ranxf
'''

"""
装饰器
"""

import time
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以通过变量也能调用函数


def now():
    now_time = time.strftime("%H:%m:%d %H-%M-%S")
    print(now_time)

f = now
f()

# 函数对象有一个__name__属性，可以拿到一个函数的名字
name = now.__name__
print('fun_name: ', name)

f_name = f.__name__
print('f_name: ', f_name)

# 现在假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now（）函数的定义，这种在代码运行期间动态增加功能的方式，成为装饰器
# 本质上，装饰器就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志装饰器
