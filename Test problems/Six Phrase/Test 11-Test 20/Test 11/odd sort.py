n=int(input())
a=list(map(int,input().split()))
r=[]
for i in range(0,n):
  if(i%2==0):
    r.append(a[i])
    r.sort()
print(*r,end=" ")
