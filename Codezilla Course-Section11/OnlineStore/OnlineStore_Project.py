
# A dictionary of available items
available_items = {
  "Google Pixel 6a": {
    "price": 280,
    "quantity": 5
  },
  "SAMSUNG Galaxy S23 Ultra": {
    "price": 1200,
    "quantity": 3
  },
  "iPhone 13 Pro Max": {
    "price": 1300,
    "quantity": 2
  },
  "Xiaomi Redmi 9A": {
    "price": 100,
    "quantity": 4
  },
  "Huawei P50 Pro": {
    "price": 1000,
    "quantity": 1
  },
  "OnePlus 9 Pro": {
    "price": 800,
    "quantity": 1
  },
}

cart = {}

message = """\nWhat would you like to do?
1. View available items
2. View cart
3. Total cart price
4. Clear cart
5. Remove item from the order
6. Quit"""

print('Welcome to Codezilla store!!')

while True:
  #display intro message
  print(message)
  #get user choice
  user_choice = input('Enter the number of your choice: ')
  # if the user choice is 1

  if user_choice == '1':

    #display the menu of the items
    for i, item in enumerate(available_items, 1):
      item_price = available_items[item]['price']
      item_available_quantity = available_items[item]['quantity']

      #if item quantity is available or not
      if item_available_quantity != 0:
        print(f'{i}. {item}: ${item_price}')
      else:
        print(f'{i}. {item}: ${item_price} (Not available now)')
    item_num = input(
      'Enter the number of the item you want to purchase (Enter 0 to return to the previous menu): '
    )
    #if user want to exit by pressing 0
    if item_num == '0':
      continue
    #check if item number in range and digits
    elif item_num.isdigit():
      item_num = int(item_num)
      #make a list for the available items
      available_item_list = list(available_items)
      #if user choose invalid character or number
      if item_num not in range(len(available_item_list) + 1):
        print('\nInvalid option')
        continue
      #get the item from list 
      item = available_item_list[item_num - 1]
      #get the item price
      item_price = available_items[item]['price']
      #get the item available quantity of the item in the main dictionary
      item_available_quantity = available_items[item]['quantity']
      #get the quantity of the item that the user need to purchase
      user_quantity = input('Please, Enter the quantity: ')
      #check if the item number in digits
      if user_quantity.isdigit():
        #convert user quantity to integers
        user_quantity = int(user_quantity)

        #check if quantity available or not
        if user_quantity <= item_available_quantity:
          item_available_quantity -= user_quantity
          #update the main dictionary
          available_items[item]['quantity'] = item_available_quantity
          #add and update the quantity to the cart(get)
          quantity = cart.get(item, {}).get('quantity', 0) + user_quantity
          #print a note for the user that the item added to the cart
          print(f'\n{item} has been added to the cart successfully.')

          #ask the user to add a comment
          check = input('\nDo you want to add a comment? (y/n): ').lower()
          if check == 'y':
            comment = input('\nWhat is your comment? ')
            print('\nWe will take your comment into consideration.')
          elif check == 'n':
            comment = 'No comment'
          else:
            print('\nInvalid option')
            comment = '--------------'
          # create a cart dictionary
          cart_info = {
            item:{
              'comment': comment,
              'price': item_price, 
              'quantity': quantity
            }
          }
          # update the cart
          cart.update(cart_info)


        #if the user ask for item is not available
        elif item_available_quantity == 0:
          print('\nSorry, this item is not available now.')
        #if the user ask for a quantity more than the available one
        elif user_quantity > item_available_quantity:
          print(
            f'\nSorry, we only have {item_available_quantity} of this item')
        #if the user choice is invalid
        else:
          print('Invalid option')
          continue
      #if the user choice is invalid
      else:
        print('Invalid option')
        continue

    #if the user choice is invalid
    else:
      print('Invalid option')
      continue

  # if the user choice is 2
  elif user_choice == '2':
    #if cart is not empty
    if cart:
      print('Cart:')
      print('--------------------------')
      #print the cart in details
      for item, info in cart.items():
        price = info['price']
        quantity = info['quantity']
        total_item_price = price * quantity
        print(f"""\n{item}: ${price} x {quantity} = ${total_item_price}
--------------------------""")
    #if cart is empty
    else:
      print('\nNo items have been bought')
    #print total cart price
    total_cart_price = sum(
      [info['price'] * info['quantity'] for item, info in cart.items()])
    print(f"""\nTotal cart price: ${total_cart_price}""")
  # if the user choice is 3
  elif user_choice == '3':
    #print total cart price
    total_cart_price = sum(
      [info['price'] * info['quantity'] for item, info in cart.items()])
    print(f"""\nTotal cart price: ${total_cart_price}""")
  # if the user choice is 4
  elif user_choice == '4':
    #if cart is not empty
    if cart:
      #check message if the user want to delete the cart
      check = input('\nAre you sure you want to clear the cart? (y/n): ')
      #if the user chooses yes
      if check == 'y' or check == 'Y':
        #list the items 
        cart_list = list(cart)
        #loop through the items list to reset the quantities in the main dictionary
        for item_to_remove in cart_list:
          #get the quantity of each item in main items dictionary
          item_available_quantity = available_items[item_to_remove]['quantity']
          #get the item to remove quantity
          item_to_remove_quantity = cart[item_to_remove]['quantity']
          #add the quantity to the main available quantity again
          item_available_quantity+=item_to_remove_quantity

        #clear the cart
        cart.clear()
        print('\nCart has been cleared successfully.')
      #if the user chooses no
      elif check == 'n' or check == 'N':
        continue
      else:
        print('\nInvalid option')
        continue
    #if cart is empty
    else:
      print('\nNo items have been bought')

  #Remove item from the order
  elif user_choice == '5':
    #if cart is not empty
    if cart:
      #check message if the user want to Remove an item from the order
      check = input('\nAre you sure you want to remove an item from the order? (y/n): ')
      #if the user check yes
      if check == 'y' or check == 'Y':
        #display the cart
        if cart:
          print('Cart Items:')
          print('--------------------------')
          #print the cart items for the user
          for i, item in enumerate(cart,1):
            print(f'{i}.{item}')
        #list the items 
        cart_list = list(cart)
        #ask the user to choose a number from the cart displayed above
        item_num = int(input('Choose the Item number to be removed: '))
        #iterate through the list by the index chosen by the user
        item_to_remove = cart_list[item_num-1]
        #get the quantity of the item to remove
        item_available_quantity = available_items[item_to_remove]['quantity']
        #get the item to remove quantity
        item_to_remove_quantity = cart[item_to_remove]['quantity']
        #add the quantity to the main available quantity again
        item_available_quantity+=item_to_remove_quantity

        #update the cart 
        cart.pop(item_to_remove)
        #message the item removed successfully
        print(f'\n{item} has been removed from the cart successfully.')

      #if the user chooses no
      elif check == 'n' or check == "N":
        continue
      # if the user choice is invalid
      else:
        print('\nInvalid option')
        comment = '-----------------'
    #if cart is empty
    else:
      print('\nNo items have been bought')

  # if the user choice is to exit
  elif user_choice == '6':
    #check message if the user want to exit the program
    check = input('\nAre you sure you want to exit the program? (y/n): ').strip()
    #exit the program
    if check == 'y' or check == 'Y':
      break
    #if the user chooses no
    elif check == 'n' or check == 'N':
      continue

  # if the user choice is invalid
  else:
    print('\nInvalid option')
    continue

print('\nThanks for choosing Codezilla Online Store')

#if cart is not empty
if cart:
  print('Cart:')
  print('--------------------------')
  #print the cart in details
  for item, info in cart.items():
      print(f"\nClient Comment for {item}: {info['comment']}")
      price = info['price']
      quantity = info['quantity']
      total_item_price = price * quantity
      print(f"""\n{item}: ${price} x {quantity} = ${total_item_price}
--------------------------""")

#if cart is empty
else:
  print('No items have been bought')
#print total cart price
total_cart_price = sum(
  [info['price'] * info['quantity'] for item, info in cart.items() if not item == 'comment'] )
print(f"""\nTotal cart price: ${total_cart_price}""")
