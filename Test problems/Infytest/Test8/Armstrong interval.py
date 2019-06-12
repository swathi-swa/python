a=int(input())
b=int(input())
for i in range(a,b+1):
    temp=i
    sum=0
    m=len(str(i))
    while(temp!=0):
        rem=temp%10
        sum=sum+(rem**m)
        temp=temp//10
    if(sum==i):
        print(i)



