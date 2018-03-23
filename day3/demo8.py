# 传一个值，每次除以2直到不能除为止

def calc(n):
    print(n)
    if int(n/2)>0:
        return calc(int(n/2))
    print('--->>', n)

calc(10)