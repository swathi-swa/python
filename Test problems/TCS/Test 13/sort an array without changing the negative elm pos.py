n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(n):
    if(l[i]>=0):
        r.append(l[i])
r.sort()
k=0
for i in range(n):
    if(l[i]>=0):
        l[i]=r[k]
        k+=1
print(*l)
