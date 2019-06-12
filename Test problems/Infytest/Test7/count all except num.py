s=str(input())
ns=""
for i in s:
    if(i>='a' and i<='z' or i>='A' and i<='Z'):
        ns=ns+i
    else:
        continue
print(ns)
        
