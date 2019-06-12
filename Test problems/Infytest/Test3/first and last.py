def re(st):
    new=""
    if(len(st)>=2):
        return(st[0:2]+st[len(st)-2:len(st)])
    else:
        return -1

    
st=str(input())
print(re(st))
