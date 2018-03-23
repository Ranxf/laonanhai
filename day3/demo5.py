
# **kwargs接收N个关键字参数，转换成字典的形式


def test2(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])
    print(kwargs['sex'])


test2(name='zhangsan', age=8, sex='male')
test2(**{'name': 'zhangsan', 'age': '22', 'sex': 'male'})
