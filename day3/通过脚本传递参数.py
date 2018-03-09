'''
Author:Ranxf
'''

import sys

f = open("file_op", "r", encoding="utf-8")
f_new = open("file_op.new", "w", encoding="utf-8")

find_str = sys.argv[1]
replace_str = sys.argv[2]


for find_str in f:
    if find_str in line:
        line = line.replace(find_str, replace_str)
    f_new.write(line)
f.close()
f_new.close()
