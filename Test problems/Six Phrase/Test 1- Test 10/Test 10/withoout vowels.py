s=input()
v={'a','e','i','o','u','A','E','I','O','U'}
ss=''
for i in s:
  if i in v:
    continue
  else:
    ss=ss+i
print(ss,end="")
