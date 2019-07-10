n,p=map(int,input().split())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if(a[i]<=p):
        c+=1
        k=a[i]
    for j in range(i+1,n):
        k=k*a[j]
        if(k<=p):
            c+=1
        else:
            break
print(c)
            
