'''
Date:2017.12.26
Author:Ranxf
'''
"""
面向对象-----类------class
面向过程-----过程---- def
函数式编程----函数----def

函数定义：将一组语句的集合通过一个名字（即函数名）封装起来，要想执行这个函数，只需调用其函数名即可


函数和过程都是可以调用的，过程就是一个没有返回值的函数而已

面向过程的编程方法：一段一段的逻辑或者一段一段的功能包含在def定义的过程中，使用时直接调用
函数式编程：？
"""


# 语法定义
# 定义一个函数，有返回值
def func1():   # 函数名，括号里可以写入参数
    """testing"""
    print('in the func1')  # 函数体，表示复杂逻辑的代码
    return 0  # 返回值


# 定义一个过程,没有返回值
def func2():
    """testing2"""
    print("in the func2")  # 表示复杂逻辑的代码

# 调用
x = func1()
y = func2()
print('from func1 return is %s' %x)
print('from func2 return is %s' %y)  # 也被当成了一个隐式的函数
