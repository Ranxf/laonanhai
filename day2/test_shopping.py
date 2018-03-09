'''
Author:Ranxf
'''
"""
定义一个商品列表；
定义一个空列表，用于存放用户已买商品；

"""

proc_list = [
    ("Iphone", 6300),
    ("Mac pro", 12000),
    ("star_coffie", 50),
    ("python_book", 68),
    ("Bike", 800),
    ("Tesla", 1320000)
]

shopping_list = []
money = input("please input your money: ")
if money.isdigit():
    salary = int(money)
    # print(salary)
    while True:
        for index, item in enumerate(proc_list):
            print(index, item)

        user_choice = input("选择要买什么？>>>")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(proc_list) and user_choice >= 0:
                p_item = proc_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added \033[32;1m%s\033[0m into shopping cart, your current balance is \033[31;1m%s\033[0m " % (p_item, salary))
                else:
                    print("\033[41;1m您的余额不足%s，请重新选择: \033[0m " % salary)
            else:
                print("\033[41;1m该商品不存在,请重新输入:\033[0m")
        elif user_choice == "q":
            print("------------ shopping list ------------")
            for p in shopping_list:
                print(p)
            print("\n your current balance %s" % salary)
            exit()
        else:
            print("\033[041;1m Invalid input \033[0m")

else:
    print("\033[041;1m Invalid input \033[0m")

