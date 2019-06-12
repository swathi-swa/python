4.      Write a python function to create and return a new dictionary from the given dictionary(item:price). Given the following input, create a new dictionary with elements having price more than 200.

prices = {'ACME': 45.23,'AAPL': 612.78, 'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}

Input Format

string

Constraints

n

Output Format

dictionary

Sample Input 0

{ 'ACME': 45.23,'AAPL': 612.78, 'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
Sample Output 0

{'AAPL': 612.78, 'IBM': 205.55}





import ast
def create_new_dictionary(prices):
    n=ast.literal_eval(prices)
    new_dict={}
    for key,value in n.items():
        if value> 200.0:
            new_dict[key]=value
    sorted_d= sorted(new_dict.items())
   
    return dict(sorted_d)
prices=input()
print(create_new_dictionary(prices))
