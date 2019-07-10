(partially current)


n,s,x=map(int,input().split())
flag=0
for i in range(n+1):
    if(i+i==s or i^i==x):
        print("Yes")
        break
else:
    print("No")
    
