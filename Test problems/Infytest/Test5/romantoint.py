def romantoint(s):
    sym={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    val=0
    for i in range(len(s)):
        if(i>0 and sym[s[i]] > sym[s[i-1]]):
            val+=sym[s[i]]-2*sym[s[i-1]]
        else:
            val+=sym[s[i]]
    return(val)
s=input()
print(romantoint(s))
