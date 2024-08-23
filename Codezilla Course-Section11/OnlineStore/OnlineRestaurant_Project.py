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
  'Pizzas': pizzas,
  'Burgers': burgers,
  'Drinks': drinks,
  'Soups': soups,
  'Desserts': desserts
}

order = {}

options_message = ('''\n1. Add another item
2. View the order
3. Clear the order
4. Remove item from the order
5. Exit
Please enter your choice: ''')

print('Welcome to Codezilla restaurant')

while True:
  while True:
    #display the main menu
    print('\nOur delecious menu')
    for i, item in enumerate(menu, 1):
      print(f'{i}. {item.title()}')
    #get th order item from the user
    user_input = input(
      '\nPlease, enter the number of the item you want (Press enter to go to the options menu): '
    )
    #if the user press enter to exit
    if user_input == '':
      break
    #if the user enter valid number of the item from the menu
    elif user_input.isdigit():
      #create a list of items in main menu
      menu_lst = list(menu.keys())
      #convert the user choice to integer
      user_input = int(user_input)
      #if the valid number in the items range
      if user_input in range(len(menu_lst) + 1):
        #get the order item
        order_category = menu_lst[user_input - 1]
        #display the sub-menu with the prices
        for i, item in enumerate(menu[order_category], 1):
          print(f'{i}. {item.title()}: {menu[order_category][item]} EGP')
        #get th order sub-item number from the user
        user_order = input(
          '\nPlease, enter the number of the item you want (Press 0 to return to the previous menu): '
        )
        #if the user press 0 to return back to the main menu
        if user_order == "0":
          continue
        #if the user enter valid number of the sub-item from the sub-menu
        elif user_order.isdigit():
          #convert the user choice to integer
          user_order = int(user_order)
          #create a list of sub-items in sub-menu
          sub_menu_lst = list(menu[order_category].keys())
          #if the valid number in the items range
          if user_order in range(len(sub_menu_lst) + 1):
            #get the order sub-item
            order_item = sub_menu_lst[user_order - 1]
            #get the sub-item price
            order_price = menu[order_category][order_item]
            #get the user needed quantity
            user_order_quantity = int(input('\nPlease, enter the quantity: '))

            #update the order quantity
            order_quantity = order.get(order_item, {}).get(
              'quantity', 0) + user_order_quantity
            #the total price of the single sub-item
            item_total_price = order_quantity * order_price

            print(
              f'{order_item} {order_category} added to the order successfully')

            #check and ask the user to add a comment
            check = input(
              '\nDo you want to add a comment to the order (y/n)? ').lower()
            if check == 'y':
              comment = input('\nAdd your comment here: ')
              print('\nWe will take your comment into consideration.')
            elif check == 'n':
              comment = 'No comment'
            else:
              print('\nInvalid choice, please renter your choice')
              continue
            #create an order info
            order_info = {
              order_item: {
                'category': order_category,
                'comment': comment,
                'price': order_price,
                'quantity': order_quantity,
                'item_total_price': item_total_price
              }
            }
            #update the order
            order.update(order_info)
            break
          else:
            print('\nInvalid choice,please renter your choice')
            continue
        else:
          print('\nInvalid choice,please renter your choice')
          continue
      else:
        print('\nInvalid choice,please renter your choice')
        continue
    else:
      print('\nInvalid choice,please renter your choice')
      continue
      #display the options menu
  user_option = input(options_message)

  #if the user chooses number 1 to add an order
  if user_option == '1':
    check = input(
      '\nAre you sure you want to add an order? (y: to return back to the menu / n: to exit the program) '
    ).lower()
    if check == 'y':
      continue
    elif check == 'n':
      break
    else:
      print('\nInvalid choice, please renter your choice')
      continue
  #if the user chooses number 2 to view the order
  elif user_option == '2':
    if order:
      #display the order
      for item, info in order.items():
        print(f"""\nItem: {item} {info['category']}
Price: {info['price']} EGP
Quantity: {info['quantity']} units
----------------------
Item Total price: {info['item_total_price']}\n""")
    else:
      print('\nThere is no order yet!!')
      continue
  #if the user chooses number 3 to clear the order
  elif user_option == '3':
    #check if the user sure to clear the order
    if order:
      check = input(
        '\nAre you sure you want to clear the order? (Y/N): ').lower()
      if check == 'y':
        order.clear()
        print('\nOrder cleared successfully!')
      elif check == 'n':
        continue
      else:
        print('Invalid choice,please renter your choice')
        continue
    else:
      print('\nThere is no order to clear!')

  #elif user chooses 4 to remove item from the order
  elif user_option == '4':
    #if there is order
    if order:
      #display the order for the user
      print('Your current order is:\n-------------------------')
      for item, info in order.items():
        print(f"""\nItem: {item}
Price: {info['price']} EGP
Quantity: {info['quantity']} units""")
      #ask the user for the item he want to delete
      item_to_remove = input(
        '\nPlease, enter the item you want to remove: ').title().strip()
      #check meassge
      check = input(
        '\nAre you sure you want to remove this item (y/n): ').lower()
      if check == 'y':
        #check if the item is in the order
        if item_to_remove in order:
          del order[item_to_remove]
          print(f'{item_to_remove} has been removed from the order')
        else:
          print(f'{item_to_remove} is not in the order')
      elif check == 'n':
        continue
      else:
        print('Invalid choice,please renter your choice')
        continue
    else:
      print('There is no order yet.')
  #if the user chooses 5 to exit
  elif user_option == '5':
    break
  #if user_option is invalid
  else:
    print('\nInvalid choice,please renter your choice')
    continue

#greeting message
print('\nThanks for choosing Codezilla restaurant')
print('****************************************')
if order:
  print('\nYour order is:')
  #print the order to the user
  for item, info in order.items():
    print(f"""\nItem: {item} {info['category']}
Client comment: {info['comment']}
Price: {info['price']} EGP
Quantity: {info['quantity']} units
----------------------
Item Total price: {info['item_total_price']}\n""")
  Total_price = sum([info['item_total_price'] for item, info in order.items()])

  print(f'''***********************
The total price is: {Total_price}''')
