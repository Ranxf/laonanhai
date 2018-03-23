# 高阶函数：把一个函数当成实参数传给另一个函数(在不修改被装饰函数)；返回值中包含函数名


# # 这是一般普通的函数
# def add(a, b):
#     return a + b
#
#
# # 高阶函数
# def add(a, b, f):
#     return f(a) + f(b)
#
# res = add(3, -6, abs)
# print(res)


# def bar():
#     print("in the bar")
#
#
# def test1(func):
#     print(func)
#
#
# test1(bar)

# 返回值中包含函数名(不修改函数的调用方式)
import time


def bar():
    time.sleep(3)
    print("in the bar")


def test2(func):
    print(func)
    return func

# print(test2(bar()))
test2(bar())