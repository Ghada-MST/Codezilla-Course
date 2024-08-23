# dictionary of available items with their prices and quantity
items = {
  'iPhone 13': {
    'price': 1000,
    'quantity': 10
  },
  'MacBook Pro': {
    'price': 2000,
    'quantity': 5
  },
  'AirPods Pro': {
    'price': 250,
    'quantity': 2
  },
  'iPad Pro': {
    'price': 800,
    'quantity': 15
  },
  'Apple Watch Series 7': {
    'price': 600,
    'quantity': 3
  },
}

cart = {}


def main():
  print('Welcome to Codezilla store!')
  message = """\nAvailable Options:
---------------------
1. View available items
2. View cart
3. Total cart price
4. Clear cart
5. Remove an item from cart
6. Quit"""
  while True:
    print(message)
    choice = input('\nEnter the number of your choice: ')

    if choice == "1":
      view_available_items()
    elif choice == "2":
      view_cart()
    elif choice == "3":
      total_cart_price()
    elif choice == "4":
      clear_cart()
    elif choice == "5":
      remove_item()
    elif choice == "6":
      if quit():
        break
    else:
      print('\nInvalid choice, Please enter a number between 1 and 6')


def view_available_items():
  print('\n<<<<<<<Store Items>>>>>')
  #display the menu
  for i, (item, info) in enumerate(items.items(), 1):
    #if items not available
    if info['quantity'] == 0:
      print(f'{i}. {item}: {info["price"]}$ (Not available)')
    else:
      print(f'{i}. {item}: {info["price"]}$')
  #try except to raise errors
  try:
    #ask user for order
    item_num = int(
      input(
        '\nNumber of the item to purchase (Enter 0 to return to the previous menu: '
      ))
    if item_num > len(items) or item_num < 0:
      print('Sorry, This number is out of range')
      return
    elif item_num == 0:
      return
    item = list(items)[item_num - 1]
    item_quantity = items[item]['quantity']
    item_price = items[item]['price']
    if item_quantity == 0:
      print('Sorry, this item is not available')
      return

    print(f"Available quantity: {item_quantity}")
    purchased_quantity = int(input('Please, Enter the quantity: '))
    #purchased quantity less than zero raise error
    if purchased_quantity < 0:
      print('\nPlease enter a whole number')
      return
    #purchased quantity less than available quantity
    elif purchased_quantity <= item_quantity:

      updated_quantity = cart.get(item, {}).get('quantity', 0)
      each_item_price = (purchased_quantity + updated_quantity) * item_price

      order_info = {
        item: {
          "price": item_price,
          "quantity": purchased_quantity + updated_quantity,
          "item total price": each_item_price
        }
      }
      cart.update(order_info)

      print(cart)
      items[item]['quantity'] -= purchased_quantity
      print(items)
      print(f'\n{item} has been added to the cart successfully')

    #purchased quantity greater than available quantity
    else:
      print(f'\nSorry we only have {item_quantity} of this item')

  except ValueError:
    print('\nInvalid choice, enter whole numbers only.')


def view_cart():
  total_cart_price = sum(
    [info["item total price"] for item, info in cart.items()])
  if not cart:
    print('\nNo items in the cart')
    return
  print("""\nCart
--------------------------""")
  for i, (item, info) in enumerate(cart.items(), 1):
    print(
      f'{i}. {item}: ${info["price"]:,.2f} x {info["quantity"]} = ${info["item total price"]:,.2f}'
    )
  print(f"""--------------------------
Total price of the cart: {total_cart_price:,.2f}""")


def total_cart_price():
  if not cart:
    print('No items in the cart')
    return
  total_cart_price = sum(
    [info["item total price"] for item, info in cart.items()])
  print(f"Total price of the cart: ${total_cart_price:,.2f}")


def clear_cart():
  #if the cart is empty
  if not cart:
    print('No items in the cart')
    return
  #check message

  answer = input('Are you sure you want to clear the cart (y/n): ').lower()
  if answer == 'y':
    for item, info in cart.items():
      purchased_quantity = info['quantity']
      items[item]['quantity'] += purchased_quantity

    cart.clear()
    print('The cart cleared successfully')
  elif answer == 'n':
    return
  #why when i did try and except it didnot work here
  #and if i left without else or anything it return automatically
  else:
    print('Invalid choice')


def remove_item():
  #if the cart is empty
  if not cart:
    print('No items in the cart')
    return
  for i, (item, info) in enumerate(cart.items(), 1):
    print(
      f'{i}. {item}: ${info["price"]:,.2f} x {info["quantity"]} = ${info["item total price"]:,.2f}'
    )
  try:
    item_num = int(input('\nEnter the item number you want to remove: '))
    if item_num not in range(1, len(cart) + 1):
      print('Sorry, This number is out of range')
      return
    answer = input('\nAre you sure you want to delete an item (y/n): ').lower()
    if answer == 'y':
      item = list(cart)[item_num - 1]
      purchased_quantity = cart.get(item).get('quantity')
      items[item]['quantity'] += purchased_quantity

      del cart[item]
      print(f'\n{item} removed from the cart successfully')
      return
    elif answer == 'n':
      return
    #why when i did try and except it didnot work here
    #and if i left without else or anything it return automatically to the function with no error
    else:
      print('Invalid choice')
  except ValueError:
    print('\nInvalid choice, enter whole numbers only.')


def quit():
  check = input('\nAre you sure you want to quit (y/n): ').lower()
  if check == "y":
    print("\nThank you for shopping at Codezilla store")
    total_cart_price = sum(
      [info["item total price"] for item, info in cart.items()])
    print("""\nCart:
-----------------""")
    for i, (item, info) in enumerate(cart.items(), 1):
      print(
        f"""{i}. {item}: ${info["price"]:,.2f} x {info["quantity"]} = ${info["item total price"]:,.2f}
-----------------""")
    print(f"""\nTotal price of the cart: ${total_cart_price}
******************************
See you next time""")
    return True
  elif check == 'n':
    return

  else:
    print('Invalid choice')


if __name__ == '__main__':
  main()
