3.  Write a function build_index_grid(rows, columns) that, given a number of rows and columns, creates a list of lists of that shape that includes the 'row,column' of that location.

For example, after the following code is executed: new_index_grid = build_index_grid(4,3) new_index_grid would contain: [['0,0', '0,1', '0,2'], ['1,0', '1,1', '1,2'], ['2,0', '2,1', '2,2'], ['3,0', '3,1', '3,2']] Note that these are strings.

Sample Input 0

4 3
Sample Output 0

[['0,0', '0,1', '0,2'],
['1,0', '1,1', '1,2'],
['2,0', '2,1', '2,2'],
['3,0', '3,1', '3,2']]




r,c=map(int,input().split())
l=[]
for i in range(0,r):
    n=[]
    for j in range(0,c):
        temp=str(i)+','+str(j)
        n.append(temp)
    l.append(n)
print("[",end="")
print(*l,sep=',\n',end="")
print("]")
