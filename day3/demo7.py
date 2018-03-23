# # 局部变量:函数里面的变量即为局部变量，只在函数里有效
#
#
# def change_name(name):
#     print("befor change", name)
#     name = 'San Zhang'  # 这个函数就是这个变量的作用域
#     print("after change", name)
#
# name = 'zhangsan'
# change_name(name)
# print(name)
#
#
# # 全局变量：在整个程序中都生效的变量，在整个代码的顶层定义的变量就是全局变量
#
# company = 'ali'  # 全局变量
#
#
# def change_name(name):
#     company = 'tengxu'  # 局部变量
#     print("befor change", name, company)
#     name = 'zhangsan'  # 这个函数就是这个变量的作用域
#     print("after change", name)
#
# print(company)
#
# name = 'lisi'
# change_name(name)
# print(name, company)
#
#
# # 在函数里面，默认情况下局部变量不能更改全局变量，如果想在函数中将局部变量改为全局变量的方法：改之前申明global，不建议使用这种方法
#
# company = 'ali'  # 全局变量
#
#
# def change_name(name):
#     global company
#     company = 'tengxu'    # 局部变量
#     print("befor change", name, company)
#     name = 'zhangsan'  # 这个函数就是这个变量的作用域
#     print("after change", name)
#
# print('company: ', company)   # 执行查看函数调用前打印的情况
# name = 'lisi'
# change_name(name)
# print(name)
# print('company: ', company)   # 执行查看函数调用后打印的情况


# # 不建议使用这种方法
# def chang_name():
#     global name
#     name = 'zhangsan'
#
# chang_name()
# print(name)


# 局部变量改全局变量

company = 'ali'  # 全局变量
names = ['zhangsan', 'sili', 'wangwu']


def change_name():
    names[0] = '张三'
    print("inside_func: ", names)          # 运行查看执行结果

change_name()
print('ouside_func：', names)   # 运行查看执行结果
