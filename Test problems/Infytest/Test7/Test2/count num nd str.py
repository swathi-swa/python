def countdigits(s):
    c=[]
    l1=0
    l2=0
    for i in s:
        if(i>="a" and i<="z"):
            l1+=1
        elif(i>="A" and i<="Z"):
            l1+=1
        elif(i>="0" and i<="9"):
            l2+=1
    c.append(l1)
    c.append(l2)
    return c
s=input()
print(countdigits(s))
