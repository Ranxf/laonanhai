'''
Author:Ranxf
'''

list_1 = [1, 2, 3, 4, 7, 5, 6, 7, 8]
list_1 = set(list_1)

print(list_1, type(list_1))

list_2 = set([2, 6, 0, 66, 22, 8, 4])
print(list_1, list_2)

# 交集
list_3 = list_1.intersection(list_2)
print(list_3)

# 并集
list_4 = list_1.union(list_2)
print(list_4)

# 差集
print(list_1.difference(list_2))
print(list_2.difference(list_1))

# 子集
print(list_1.issubset(list_2))

# 父集
list_5 = [2, 6, 0, 66]
print(list_1.issuperset(list_2))
print(list_2.issuperset(list_5))

# 反向差集,互相没有的合并在一起
print(list_1.symmetric_difference(list_2))

print("--------------------------")

print(list_2.isdisjoint(list_1))
print(list_1 & list_2)  # 交集
print(list_1 | list_2)  # 并集
print(list_1 - list_2)  # 差集
print(list_1 ^ list_2)  # 对称差集

list_1.add(999)
list_1.update([888,777,555])
print(list_1)

list_1.pop()
# list_1.remove()
list_1.discard(888)
