import math
s=input("").split(" ")
q=int(s[0])
w=int(s[1])
c=(q**2)+(w**2)
d=math.sqrt(c)
print("{:.2f}".format(d),end="")
