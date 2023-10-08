
# available items
pizzas = {
  "Margherita": 100,
  "Pepperoni": 120,
  "Meat Lovers": 150,
  "Chicken": 130
}
burgers = {"Beef": 100, "Chicken": 80, "Bacon": 120}
drinks = {"Coke": 30, "Sprite": 25, "Fanta": 25, "Pepsi": 30}
soups = {"Chicken Soup": 50, "Beef Soup": 60, "Mushroom Soup": 40}
desserts = {"Ice Cream": 50, "Chocolate Cake": 60, "Cheese Cake": 70}

menu = {
  'pizzas': pizzas,
  'burgers': burgers,
  'drinks': drinks,
  'soups': soups,
  'desserts': desserts
}

print(menu)

order = {}

options_message = ('''1. Add another item
2. View the order
3. Clear the order
4. Exit
Please enter your choice: ''')

print('Welcome to Codezilla restaurant')

while True:
  print('Our delecious menu')
  for i, item in enumerate(menu, 1):
    print(f'{i}. {item.title()}')
  user_input = input(
    '\nPlease, enter the number of the item you want (Press enter to exit): ')
  if user_input == '':
    break

  elif user_input.isdigit():
    menu_lst = list(menu.keys())
    user_input = int(user_input)
    if user_input in range(len(menu_lst) + 1):
      order_category = menu_lst[user_input - 1]
      for i, item in enumerate(menu[order_category], 1):
        print(f'{i}. {item.title()}: {menu[order_category][item]} EGP')
      user_order = input(
        '\nPlease, enter the number of the item you want (Press 0 to return to the previous menu): '
      )
      if user_order == "0":
        continue
      elif user_order.isdigit():
        user_order = int(user_order)
        sub_menu_lst = list(menu[order_category].keys())
        if user_order in range(len(sub_menu_lst) + 1):
          order_item = sub_menu_lst[user_order - 1]
          order_price = menu[order_category][order_item]
          user_order_quantity = int(input('\nPlease, enter the quantity: '))
          order_quantity = order.get(order_category, {}).get(
            order_item, {}).get('quantity', 0) + user_order_quantity
          item_total_price = order_quantity * order_price
          item_category = order_item, order_category
          order_info = {
            item_category: {
              'price': order_price,
              'quantity': order_quantity,
              'item_total_price': item_total_price
            }
          }

          order.update(order_info)

          user_option = input(options_message)
          if user_option == '1':
            continue
          elif user_option == '2':
            for item, info in order.items():
              print('\nItem:')
              print(*item)
              print(f"""Price: {info['price']} EGP
Quantity: {info['quantity']} units
----------------------
Item Total price: {info['item_total_price']}\n""")

          elif user_option == '3':
            order.clear()
          elif user_option == '4':
            break
          else:
            print('Invalid choice,please renter your choice')
            continue

        else:
          print('Invalid choice,please renter your choice')
          continue
      else:
        print('Invalid choice,please renter your choice')
        continue
    else:
      print('Invalid choice,please renter your choice')
      continue
  else:
    print('Invalid choice')

print('\nThanks for choosing Codezilla restaurant')
print('****************************************')
if order:
  print('Your order is:')
  for item, info in order.items():
    print('\nItem:')
    print(*item)
    print(f"""Price: {info['price']} EGP
Quantity: {info['quantity']} units
----------------------
Item Total price: {info['item_total_price']}\n""")
  Total_price = sum([info['item_total_price'] for item, info in order.items()])
  print(f'''{'*'*30}
The total price is: {Total_price}''')
