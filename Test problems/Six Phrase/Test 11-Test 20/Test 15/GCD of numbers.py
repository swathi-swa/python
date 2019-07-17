def gcd(x,y):
  while(y):
    x,y=y,x%y
  return x
l=list(map(int,input().split()))
num1=l[1]
num2=l[2]
ans=gcd(num1,num2)
for i in range(3,len(l)):
  ans=gcd(ans,l[i])
print(ans,end="")

