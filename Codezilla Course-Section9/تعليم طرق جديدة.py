
#unpacks the items of the lists.
lst = [1, 2, 3, 4, 5, 6]
print(*lst, sep=', ')


lst = [25,4,2013]
print(*lst, sep=' / ')


#list_methods_Project2.py
top_5_salaries_int = sorted_salaries[-5:]
top_5_salaries_str = map(str,top_5_salaries_int)
top_5_salaries = ', '.join(top_5_salaries_str)


#reverse a string
txt = 'don don park'[::-1]
print(txt)


lst=['dodo','soso','timo']
i = 0
while i < len(lst):
  print(lst[i])
  i+=1


#even odd without if condition

user_num = int(input('Enter a number:'))
check_and_Multiply = user_num * (8 + (user_num % 2))
print(check_and_Multiply)



prices = [10.99, 20.99, 30.99, 40.99, 50.99]
lst = []
for price in prices :
lst.append(f"{price}$")

print(f'The price list is {lst}')