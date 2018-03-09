'''
Author:Ranxf
'''

"""
启动程序后，让用户输入工资，然后打印商品列表
允许用户根据商品编号购买商品
用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
可随机退出，退出时，打印已购买商品和余额
"""

product_list = [
    ("Iphone", 5800),
    ("mac pro", 1200),
    ("Bike", 800),
    ("Watch", 10600),
    ("Coffice", 50),
    ("python", 60),
]
shopping_list = []
salary = input("Please your salary：")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):
            # print(product_list.index(item), item)
            print(index, item)

        user_choice = input("选择要买什么？>>>")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >=0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart, your current balance is \033[31;1m%s\033[0m] " % (p_item, salary))
                else:
                    print("\033[41;1m 您的余额只剩%s,请重新选择\033[0m]" % salary)
            else:
                print("商品不存在")
        elif user_choice == "q":
            print("-------------shopping list------------")
            for p in shopping_list:
                print(p)
            print("Your current balance: ", salary)
            exit()
        else:
            print("invalid option")

