"""
函数返回值
函数返回值的作用：后面的程序需要这个函数的返回结果
"""


def test1():
    """未定义返回值"""
    print('in the test1')  # 函数体


def test2():
    '''定义返回值'''
    print('in the test2')  # 函数体
    return 0  # 定义返回值，结束函数的效果


def test3():
    '''定义返回值有数字，字符，元组，字典'''
    print('in the test3')  # 函数体
    return 1, 'hello', ['zhangsan', 'lisi'], {'name': 'emy'}

x = test1()  # 函数体的返回值
y = test2()  # 函数体的返回值
z = test3()  # 函数体的返回值
print(x)
print(y)
print(z)

