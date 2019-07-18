n=int(input())
c= 0
b= 1
while( b * (b + 1) < 2 * n): 
    a = (1.0 * n- (b * (b + 1) ) / 2) / (b + 1) 
    if (a - int(a) == 0.0): 
        c += 1
    b += 1
print(c)
