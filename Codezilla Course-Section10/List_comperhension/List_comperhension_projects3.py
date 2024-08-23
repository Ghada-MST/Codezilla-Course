# A list of available fruits
available_fruits = [
# Format: [item name, price for kg]
["Apple", 30],
["Banana", 20],
["Orange", 25],
["Mango", 40],
["Strawberry", 35],
["Blueberry", 50],
["Peach", 45],
["Pineapple", 55],
["Watermelon", 30],
["Grapes", 50],
["Cherry", 60],
["Kiwi", 45]
]

fruits_total_price = 0
total_fruits = ''


while True:
  
  print('''Welcome to Codezilla fruits store!
1.View available fruits and buy
2.Total price of basket
3.Quit''')

  choice = input('Enter the number of your choice: ')

  
  if choice == '1':
    
    print(f'''Available fruits:
{'-'*20}''')
    fruits_menu = [print(f'{index}.{fruit}: {price} EGP.') for index,(fruit,price) in enumerate(available_fruits,1) ]
    
    item_num = int(input('Enter the number of item (press 0 to return to the previous menu): '))
    if item_num in range(1,len(available_fruits)+1):
      fruits_total_price += available_fruits[item_num-1][1]
      total_fruits+= available_fruits[item_num-1][0]
      print(f'{available_fruits[item_num-1][0] } added to the basket successfully')
    elif item_num ==0:
      continue 
    else:
      print('error in entry')
 
  elif choice== '2':
    if fruits_total_price: 
      print(f'The total price of the basket is: {fruits_total_price}')
    else:
      print('Your basket is empty')
      break
  elif choice=='3':
    if fruits_total_price:
      print('Final Basket')
      fruits_menu = [print(f'{fruit}: {price} EGP.') for index,(fruit,price) in enumerate(available_fruits,1) if fruit in total_fruits]
      print("-"*30)
      print(f'The total price {fruits_total_price}')
    break
    
  else:
    print('Error in entry')
    
  continue


if not fruits_total_price:
  print('Your basket is empty')

print('''Thanks for choosing Codezilla fruit store.
See you again!!''')






