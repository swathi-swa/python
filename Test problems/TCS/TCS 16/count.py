n=int(input())
m=0
for i in range(1,n+1):
    k=str(i)
    m+=k.count('1')
print(m)


Sample Input 0

13
Sample Output 0

6
Explanation 0

Total number of 1's from 0 to 13 is 6. The occurence of 1 are in the numbers 1,10,11,12,13
