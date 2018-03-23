# 参数可扩展的函数


# 与位置参数一起使用
def test3(name, **kwargs):
    print(name)
    print(kwargs)

test3('zhangsan')  # 这样转参数，会接收一个name和一个空字典----->>正确
test3('lisi', age=8, sex='male')  # 与位置参数结合,以关键字方式传参------>>正确


# 与默认参数一起使用
def test4(name, age=8, **kwargs):  # 默认参数不能写在参数最后，参数组置后
    print(name)
    print(age)
    print(kwargs)

test4('wangwu', sex='male', hobby='study', age=3)   # 此处的age传参可以写在最后，也可以写在对应的位置


# 所有类型的参数结合在一起（位置参数，默认参数，带数组的参数，带字典的参数）
def test5(name, age=18, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

test5('amy', age=28, sex='male', hoddy='study')  # 在这个没有位置参数，所以*args在运行的时候接收为空元组；后面两个参数为两个关键字参数。所以传给**kwargs