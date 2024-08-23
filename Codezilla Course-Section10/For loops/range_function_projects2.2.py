#project 1
  #first method
even_nums = sum(range(28,929,2))
print(even_nums)

  #second method
sum = 0
for even_num in range(28,929,2):
  sum += even_num
print(sum)

  #third method
sum = 0
even_num = 28
while even_num <= 928:
  sum += even_num
  even_num += 2
print(sum)



#project 2
fruits = ['apple', 'banana', 'orange', 'grape', 'mango']

print('Available fruits:')
for i in range(len(fruits)):
  print(f'{i+1}. {fruits[i]}')

#project 3

# a list of pizzas
pizzas = ['Margherita', 'Pepperoni', 'Super Supreme',
'Hawaiian', 'Meat Lovers', 'Cheese Lovers']

print(f'''Welcome to Codezillas Pizza!
The menu of our delicious pizza:
{'-'*30}''')

for i in range(len(pizzas)):
  print(f'{i+1}. {pizzas[i]}')

pizzas_num = int(input('Please, Enter the number of the pizza you want to order from the menu: '))
pizzas_count = input ('Enter the number of pizzas you want: ')


print('-'*30)

end_message = f"""Thanks for choosing codezillas Pizza!
Please, Enjoy your time
While we got {pizzas_count} {pizzas[pizzas_num-1]} ready for you."""

print(end_message)




#solve the problem pleaseee



#project 3

# a list of pizzas
pizzas = ['Margherita', 'Pepperoni', 'Super Supreme',
'Hawaiian', 'Meat Lovers', 'Cheese Lovers']

print(f'''Welcome to Codezillas Pizza!
The menu of our delicious pizza:
{'-'*30}''')

for i in range(len(pizzas)):
  print(f'{i+1}. {pizzas[i]}')


while True:
  pizzas_num = input('Please, Enter the number of the pizza you want to order from the menu: ')
       
  if not pizzas_num.isdigit() :
    print("Error in entry, please try again")
    continue
  pizzas_int=int(pizzas_num)
  if pizzas_int < 1 or pizzas_int > len(pizzas):
    print(f'Please enter a number from 1 to {len(pizzas)}')
  else:
    break
while True:
  pizzas_count = input ('Enter the number of pizzas you want : ')
  if not pizzas_count.isdigit():
     print("Error in entry, please try again")
     continue
  else:
    break


print('-'*30)


mid_message = input('To confirm your order press 1 or cancel press 2: ')

if mid_message == '2':
  print('Bye Bye')

else:
  print('-'*30)

  end_message = f"""Thanks for choosing codezillas Pizza!
Please, Enjoy your time
While we got {pizzas_count} {pizzas[pizzas_int -1]} ready for you."""

  print(end_message)
