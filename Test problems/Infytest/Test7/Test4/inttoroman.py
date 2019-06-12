def num_to_roman(num):
    num_list = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
    symbol_list = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    roman =''
    i = 0
    if num <5000:
        while  num > 0:
            for _ in range(num // num_list[i]):
                roman += symbol_list[i]
                num -= num_list[i]
            i +=1
    return roman
number = int(input())
print(num_to_roman(number))
