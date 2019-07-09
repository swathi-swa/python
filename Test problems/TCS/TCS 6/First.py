n=int(input())
a=list(map(int,input().split()))
for i in  range(n-2):
    temp=a[i]
    a[i]=a[i+2]
    a[i+2]=temp
print(*a)
