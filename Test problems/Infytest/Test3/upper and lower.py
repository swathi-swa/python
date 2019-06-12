def count(sen):
    li=[]
    c1=0
    c2=0
    for i in st:
        if(i>="A" and i<="Z"):
            c1+=1
        elif(i>="a" and i<="z"):
            c2+=1
    li.append(c1)
    li.append(c2)
    return li


st=str(input())
print(count(st))
