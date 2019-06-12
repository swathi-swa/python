def exchange(l):
    m=[]
    mid=len(l)//2
    for i in range(len(l)-1,mid-1,-1):
        m.append(l[i])
    for i in range(0,mid):
        m.append(l[i])
    return m
l=list(map(int,input().split()))
print(*exchange(l))
