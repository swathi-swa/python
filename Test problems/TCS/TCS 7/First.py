(partially current)


n,s,x=map(int,input().split())
flag=0
for i in range(n+1):
    if(i+i==s or i^i==x):
        print("Yes")
        break
else:
    print("No")
    
---------------------------------------------------------------------    
    
n=list(map(int,input().split()))
v=len(n)
c=0
for i in range(v+1):
    if(n[i]>=n[v-1]):
        c+=n[i]
        b=bin(c^n[i])
        print("Yes")
        break
    else:
        print("No")
        break
    
    
