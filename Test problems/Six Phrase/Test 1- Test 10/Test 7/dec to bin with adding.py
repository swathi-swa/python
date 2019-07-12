def dtob(s):
  if(s>1):
    dtob(s//2)
  print(s%2,end="")
a,b=list(map(int,input().split()))
s=a+b
dtob(s)
