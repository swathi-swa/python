from collections import Counter
a=str(input())
b=sorted(a)
di=Counter(b)
for i in di:
    print(i,di[i])
