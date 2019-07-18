n=int(input())
s1=[]
for i in range(0,n):
     s1.append(int(input()))    
s=0
for i in range(0,2):
    s+=s1[i]
for i in range(3,len(s1)):
    for j in range(2,i):
        if(i%j==0):
            s+=s1[i]
            break
        else:
            continue
print(s)








            
