def find(num):
  for i in range(0,len(num)):
    if(num[i]==9 and i<=3):
        return True
  return False
num=list(map(int,input().split()))
print(find(num))
