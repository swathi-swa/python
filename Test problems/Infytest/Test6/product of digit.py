num=int(input())
pro=1
while(num>0):
    rev=num%10
    pro=pro*rev
    num=num//10
print(pro)
