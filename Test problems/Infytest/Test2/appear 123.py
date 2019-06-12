def check(l):
    for i in range(0,len(l)-1):
        if (l[i]==1 and l[i+1]==2 and l[i+2]==3):
            return True
    return False
l=list(map(int,input().split()))
print(check(l))
