from itertools import permutations
n=int(input())
a=list(map(int,input().split()))
r=int(max(("".join(i) for i in permutations(str(i)for i in a)),key=int)) 
print(r)
