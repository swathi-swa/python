n=int(input())
a=list(map(int,input().split()))
max=0
def find(x,y):
    while(y):
        x,y=y,x%y
    return x
def gcd(a):
    n1=a[0]
    n2=a[1]
    g=find(n1,n2)
    for i in range(2,len(a)):
        g=find(g,a[i])
    return g
for i in range(1,n+1):
    b=a[:i-1]+a[i:n]
    ans=gcd(b)
    if(ans>max):
        max=ans
print(max)
