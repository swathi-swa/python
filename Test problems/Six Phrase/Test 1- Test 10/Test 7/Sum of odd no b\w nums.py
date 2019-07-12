m,n=list(map(int,input().split()))
s=0
for i in range(m+1,n):
  if(i%2!=0):
    s+=i
print(s,end="")
