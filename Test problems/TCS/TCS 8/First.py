n,m=map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
b=[]
c=0
for i in range(n):
    for j in range(m):
        if(a1[i]+a2[j] not in b):
            b.append(a1[i]+a2[j])
            c+=1
print(c)
            
