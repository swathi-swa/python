from collections import Counter 
from itertools import repeat, chain 
n=int(input())  
ini_list =list(map(int,input().split()))
ini_list.sort()
result = list(chain.from_iterable(repeat(i, c) 
         for i, c in Counter(ini_list).most_common())) 
print(*result)
