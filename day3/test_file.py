'''
Author:Ranxf
'''

# data = open("yesterday", encoding="utf_8").read()
f = open("yesterday", 'r', encoding="utf_8")  # 文件句柄
# data = f.read()
# print(data)
# data2 = f.read()
# print("-------data2-------%s" % data2)

# f.write("\n我爱北京天安门")
# f.write("\n天安门上太阳升")
#
# data = f.read()
# print("---read---", data)
#
# for i in range(5):
#     print(f.readline())

# print(f.readlines())

# for index, line in enumerate(f.readlines()):
#     if index == 9:
#         print("------我是分割线-----")
#         continue
#     print(line.strip())

count = 0
for line in f:
    if count == 9:
        print("------我是分割线------")
        count += 1
        continue
    print(line)
    count += 1

# print(f.tell())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.tell())
# f.seek(0)
# print(f.readline())
#
# print(f.encoding)
# print(f.name)
#
# print(f.flush())
# print(f.buffer)


f.close()