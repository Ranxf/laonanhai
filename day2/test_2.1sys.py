'''
Date:2017.12.26
Author:Ranxf
'''
# import sys
#
# print(sys.path)
# print(sys.argv)
#
# print(sys.argv[2])  # 把用户的输入的参数当作一条命令交给os.system来执行


import os
test_dir = os.system("dir")
print("--->", test_dir)   # 执行命令，输出到屏幕，不保存结果
print(os.system("df -h"))

test_dir = os.popen("dir").read()
print("--->", test_dir)

# os.mkdir("new_dir")