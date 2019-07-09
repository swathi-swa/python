import math
def num(a):
    n1=math.sqrt(a)
    if(n1*n1==a):
        return False
    return True
def key(a):
    for i in range(1,a+1):
        if(num(i)==True):
            print("closed",end=" ")
        else:
            print("open",end=" ")
a=int(input())
key(a)
