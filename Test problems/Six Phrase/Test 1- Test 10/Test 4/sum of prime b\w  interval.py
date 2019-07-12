n,m=map(int,input().split())
s=0
for i in range(n+1,m):
  for j in range(2,i):
    if(i%j==0):
      break
  else:
      s+=i
print(s,end="")
