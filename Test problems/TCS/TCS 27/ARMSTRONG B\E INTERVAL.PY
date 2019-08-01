k=list(map(int,input().split()))
n=k[0]
m=k[1]
l=[]
for i in range(n,m+1):
    p=len(str(i))
    t=int(i)
    s=0
    while(t!=0):
        r=t%10
        s+=r**p
        t=t//10
    if(s==int(i)):
        l.append(s)
print(*l)

INPUT:
100 200

OUTPUT:

153
