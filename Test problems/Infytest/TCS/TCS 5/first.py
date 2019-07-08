def sub(a,n):
    m=1
    l=1
    for i in range(1,n):
        if(a[i]>a[i-1]):
            l+=1
        else:
            if(m<l):
                m=l
            l=1
    if m<l:
        m=l
    return m
a=list(map(int,input().split(" ")))
n=len(a)
print(sub(a,n))
