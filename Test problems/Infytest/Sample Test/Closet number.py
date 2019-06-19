ar=list(map(int,input().rstrip().split()))
t=int(input())
n=len(ar)
min=n
minnum=0
for i in range(0,n):
    if(min>abs(t-ar[i])):
        min=abs(t-ar[i])
        minnum=ar[i]
print(minnum)
