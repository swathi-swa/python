n,m=map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
l=0
for i in range(0,n):
  for j in range(0,m):
    if(a1[i]==a2[j]):
      l=l+1
s=n+m-(2*l)
print(s,end="")
