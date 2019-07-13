# your code goes here
a=list(map(int,input().split()))
a.sort()
d=len(a)
m=max(a)
mn=min(a)
for i in range(d):
	if(a[i]<m):
		mn=a[i]
print(m,end=" ")
print(mn)
