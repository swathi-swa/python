n=list(map(int,input().split()))
n1=n[0]
n2=n[1]
while(n1!=n2):
  if(n1>n2):
    n1=n1-n2
  else:
    n2=n2-n1
print(n2)    
    
