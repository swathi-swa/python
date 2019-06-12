def sum(l,n):
    a=len(l)
    r=0
    for i in range(1,a-1):
        if(l[i-1]!=n and l[i+1]!=n and l[i]!=n):
            r+=l[i]
    if(l[1]!=n and l[0]!=n):
      r+=l[0]
    if(l[a-2]!=n and l[a-1]!=n):
        r+=l[a-1]
    return r

l=list(map(int,input().split()))
n=int(input())
print(sum(l,n))
