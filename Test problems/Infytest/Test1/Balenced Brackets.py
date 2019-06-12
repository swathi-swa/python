5.  Balanced Brackets

Sample Input

3
{[()]}
{[(])}
{{[[(())]]}}
Sample Output

YES
NO
YES



def valid(l,r):
    if(l=='(' and r==')'):
       return True 
    if(l=='{' and r=='}'):
       return True 
    if(l=='['and r==']'):
       return True 
    return False
def nest(S):
        stack=[] 
        for sym in S:
            if (sym=='[' or sym=='{' or sym=='('):
                stack.append(sym) 
            else:
                if len(stack)==0:
                    return False
                last=stack.pop()
                if not valid(last,sym):
                    return False
        if (len(stack)!=0):
            return False
        return True
N=int(input())
for i in range(0,N):
    s=input()
    if nest(s):
        print("YES")
    else:
        print("NO")
        
