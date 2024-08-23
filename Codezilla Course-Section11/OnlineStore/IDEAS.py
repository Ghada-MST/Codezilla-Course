

  #if the user need to add a payment method
  elif user_choice == '7':
    #if cart is not empty
    if cart:
      #check message if the user want to add a payment method
      check = input('\nAre you sure you want to add a payment method? (y/n):
                    ')
      #add a payment method
                    if check == 'y' or check == 'Y':
    if user_choice == '7':
        payment_method = input('Please, Enter your payment method: ')
        cart_info = {'payment_method': payment_method}
        cart.update(cart_info)
        print('\nPayment method has been added successfully.')
    elif user_choice == '8':
        if cart:
            check = input('\nAre you sure you want to add a delivery address? (y/n): ')
            if check == 'y' or check == 'Y':
                delivery_address = input('Please, Enter your delivery address: ')
                cart_info = {'delivery_address': delivery_address}
                cart.update(cart_info)
                print('\nDelivery address has been added successfully.')
    elif user_choice == '9':
        if cart:
            check = input('\nAre you sure you want to add a delivery time? (y/n): ')
            if check == 'y' or check == 'Y':
                delivery_time = input('Please, Enter your delivery time: ')
                cart_info = {'delivery_time': delivery_time}
                cart.update(cart_info)
                print('\nDelivery time has been added successfully.')
    elif user_choice == '10':
        if cart:
            check = input('\nAre you sure you want to add a delivery fee? (y/n): ')
            if check == 'y' or check == 'Y':
                delivery_fee = input('Please, Enter your delivery fee: ')
                cart_info = {'delivery_fee': delivery_fee}
                cart.update(cart_info)
                print('\nDelivery fee has been added successfully.')


###########another way to add items to the new order dictionary line 65################

# order = {"Drinks":[{"type":"Coke", 'quantity': 3, 'price':39}, {"type":"Coke", 'quantity': 3, 'price':39}]}
# #key "Drinks" , value [{"type":"Coke", 'q': 3, 'price':39}, {"type":"Coke", 'q': 3, 'price':39}]
# for type, information in order.items():
#     for order  in information:
#         for type_2, quantity, price in order.values():