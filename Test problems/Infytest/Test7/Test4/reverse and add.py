def palin(num,count):
    num=str(num)
    rev=str(num)
    rev=rev[::-1]
    if(rev==num):
        print(count,num)
    else:
        count+=1
        num=int(num)+int(rev)
        palin(num,count)
p=input()
palin(p,0)
