import math
n=int(input())
for i in range(2,n-1):
  if(n%i==0):
      print("0.00")
else:
  print(math.sqrt(n))
