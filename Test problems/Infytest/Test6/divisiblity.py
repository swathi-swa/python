def check_numbers(num1,num2):
    num_list=set()
    for i in range(num1,num2+1):
        for j in range(num1,num2+1):
            if(i%j==0 and i not in num_list and i!=j):
                num_list.add(i)
    count=len(num_list)
    return [num_list,count]
num1,num2=map(int,input().split())
print(check_numbers(num1, num2))
