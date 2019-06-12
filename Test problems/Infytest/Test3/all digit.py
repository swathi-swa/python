#PF-Tryout
def find_five_digit():
    n2=0
    n3=0
    n4=0
    n5=0
    for i in range(9,-1,-1):
        n2=i-2
        n3=n2-2
        n4=n3-2
        n5=n3
        if(n3+n4+n5==i and i+n2+n3+n4+n5==19):
            break
    num=str(i)+str(n2)+str(n3)+str(n4)+str(n5)
    print(num)
find_five_digit()
