n=input()
l=len(n)
s=[]
s.append(-1)
c=0
for i in range(l):
    if(n[i]=='('):
        s.append(i)
    else:
        s.pop()
        if(len(s)!=0):
            c=max(c,i-s[len(s)-1])
        else:
            s.append(i)
print(c)
