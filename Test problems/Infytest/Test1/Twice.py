2.        Replace each value in a list with twice the preceding value (and the first value with 0)

Sample Input 0

1 2 3
Sample Output 0

0 2 4


number=list(map(int,input().split()))
print(0,end=" ")
for i in range(1,len(number)):
    print(number[i-1]*2,end=" ")
