"""
带参数的函数:关键字参数和位置参数
关键参数不能写在位置参数前面
"""


def test(x, y):
    print(x)
    print(y)

test(5, 8)  # 位置参数与形参一一对应
test(x=1, y=6)  # 关键字参数与形参顺序无关
test(y=9, x=3)  # 关键字参数与形参顺序无关


# 默认参数
def test1(x, y=2):
    print(x)
    print(y)

test1(1)
test1(1, y=3)

# 默认参数特点：调用函数时默认参数可有可无，不是必传参数
# 默认参数应用场景：占位或默认初始设置路径或默认端口3306


# 参数组，有n个参数，实参不固定的情况下
def test2(*args):
    print(args)

test2(1, 2, 3, 4, 5)
test2(*[1, 2, 3, 4, 5, 6])  # args=tuple(1,2,3,4,5,6)


def test3(x, *args):
    print(x)
    print(args)

test3(1, 2, 3, 4, 5, 6, 7)
