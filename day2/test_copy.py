'''
Date:2017.12.26
Author:Ranxf
'''

import copy

person = ["name", ['saving', 100]]
"""
p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)
"""

p1 = person[:]
p2 = person[:]
p1[0] = 'alex'
p2[0] = 'fengjie'
print(p1)
print(p2)

p1[1][1] = 50
print()


