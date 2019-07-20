n=int(input())
m=0
for i in range(1,n+1):
    k=str(i)
    m+=k.count('1')
print(m)
