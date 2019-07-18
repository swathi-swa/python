n=int(input())
l=[]
for i in range(0,n):
     l.append(int(input())) 
t=int(input())
c=0
for i in range(0,n-1):
    for j in range(i+1,n):
        if(l[i]+l[j]==t):
            c+=1
if(c!=0):
    print(c)
else:
    print("-1")
