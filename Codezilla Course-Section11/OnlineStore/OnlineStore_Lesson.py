available_items = {
  'Iphone 12': {
    'price': 700,
    'quantity': 4
  },
  'Iphone 12 pro': {
    'price': 1000,
    'quantity': 2
  },
  'Iphone 12 pro max': {
    'price': 1200,
    'quantity': 1
  }
}

message = '''
1. View available products
2. View my cart
3. View total price of the cart
4. Quit'''

cart = {}

while True:
  print(message)
  user_input = input("Enter your choice number from the previous menu: ")
  #if user chose number 1
  if user_input == '1':
    print('The available items are: ')
    #display the menu for the user
    for i, item in enumerate(available_items, 1):
      #get the price of item
      item_price = available_items[item]['price']
      #get the quantity of item
      availabe_quantity = available_items[item]['quantity']
      #check if the quantity is available or not
      if availabe_quantity == 0:
        print(f'{i}. {item} : ${item_price} (out of stock)')
      else:
        print(f'{i}. {item} : ${item_price}')
    #get the product name the user need
    product_num = input(
      'Enter the number of product you want (Press Enter to exit): ')
    #user exit ordering
    if product_num == '':
      continue
    #user enter nums between 1 to 3
    elif product_num.isdigit():
      #convert product_num to int
      product_num = int(product_num)
      if product_num in range(len(available_items) + 1):
        #convert product_num to int
        product_num = int(product_num)
        #make a list for products
        products_list = list(available_items)
        #get the order user needs from the list
        order_name = products_list[product_num - 1]
        #get the price of order
        order_price = available_items[order_name]['price']
        #get the quantity of order
        availabe_order_quantity = available_items[order_name]['quantity']

        #get the quantity of the order
        # if order_name not in cart:
        #   order_quantity =1
        # else:
        #   order_quantity +=1
        if availabe_order_quantity != 0:
          order_quantity = cart.get(order_name, {}).get('quantity', 0) + 1

          #create order information
          order_info = {
            order_name: {
              "price": order_price,
              'quantity': order_quantity
            }
          }
          #add the user order and its price in a new dictionary
          cart.update(order_info)

          #subtract order from the main menu quantity
          availabe_order_quantity -= 1

          #update the main menu with the new quantites
          available_items[order_name]['quantity'] = availabe_order_quantity

          #print a note to user that order added to cart
          print(f'{order_name} added successfully to the cart')
        else:
          print('item is out of stock')
      else:
        print('Please, Choose number from 1 to 3')
    else:
      print('Invalid choice')
      continue
  #if user chose number 2
  elif user_input == '2':
    if cart:
      for item, info in cart.items():
        print(f"""Product:{item}
Price: ${info['price']}
Quantity: {info['quantity']}
------------------------------""")
    else:
      print('Your cart is empty')
  #if user chose number 3
  elif user_input == '3':
    total_price = sum(info['price'] * info['quantity']
                      for item, info in cart.items())
    print(f'The total cost of the cart is ${total_price}')

  #if user chose number 4
  elif user_input == '4':
    break

  #if user chose unavaialble input
  else:
    print('Invalid choice')
    continue
#display the cart at the end of the shopping with a greeting meesage
print('\nThanks for choosing Codezilla store')
if cart:
  for item, info in cart.items():
    total_price = sum(info['price'] * info['quantity']
                      for item, info in cart.items())

    print(f"""Product:{item}
Price: ${info['price']}
Quantity: {info['quantity']}
-------------------------""")
  print(f'The total cost of the cart is ${total_price}')
else:
  print('Your cart is empty')
