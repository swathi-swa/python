n=int(input())
arr=list(map(int,input().rstrip().split()))
for i in range(0,n):
    c=0
    for j in range(i+1,n):
        if(arr[i]<arr[j]):
            c+=1
            break
    if(c==0):
        print(arr[i],end=" ")
