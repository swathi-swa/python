s1=input()
s2=input()
l=len(s1)+len(s2)
co=0
for i in s1:
    if(i in s2):
        a=s1.count(i)
        b=s2.count(i)
        if(a>b):
            e=b
        else:
            e=a
        co+=e+e
        s1=s1.replace(i,'')
        s2=s2.replace(i,'')
print(l-co)
