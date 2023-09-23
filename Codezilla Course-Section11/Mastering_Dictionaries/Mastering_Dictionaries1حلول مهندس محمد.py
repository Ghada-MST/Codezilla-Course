
#another answers to project2 mastering dictionaries
#project2############################################################################

menu = {"Margherita Pizza": 100, "Pepperoni Pizza": 120,  
"Meat Lovers Pizza": 150, "Chicken Pizza": 130, 
"Beef Burger": 100, "Chicken Burger": 80} 


update = menu.copy()
check = len(update)
while True:
  item_name = input("Enter item to be deleted (Press enter to exit): ").title()
  if item_name == '' and len(menu)< check:
    print('The new menu:')
    for item,price in menu.items(): 
      print(f'{item} : {price:.2f} EGP')
    break
  elif item_name == '':
    break
  elif item_name in menu:  
    sure_msg = input(f'Are you sure you want to delete {item_name}? (y/n): ').lower()
    if sure_msg == 'n':
      continue
    elif sure_msg == 'y':
      del menu[item_name]
      
    else:
      print('Renter your choice')
      continue
  else:
    print('Item not found')
    continue
 

#project2############################################################################

menu = {"Margherita Pizza": 100, "Pepperoni Pizza": 120,  
"Meat Lovers Pizza": 150, "Chicken Pizza": 130, 
"Beef Burger": 100, "Chicken Burger": 80} 


update = menu.copy()
check = len(update)
while True:
  item_name = input("Enter item to be deleted (Press enter to exit): ").title()
  if item_name == '' and len(menu) != check:
    print('The new menu:')
    for item,price in menu.items(): 
      print(f'{item} : {price:.2f} EGP')
    break
  elif item_name == '':
    break
  elif item_name in menu:  
    sure_msg = input(f'Are you sure you want to delete {item_name}? (y/n): ').lower()
    if sure_msg == 'n':
      continue
    elif sure_msg == 'y':
      
      del menu[item_name]
      
    else:
      print('Renter your choice')
      continue
  else:
    print('Item not found')
    continue
 

#project2############################################################################

menu = {
    "Margherita Pizza": 100,
    "Pepperoni Pizza": 120,
    "Meat Lovers Pizza": 150,
    "Chicken Pizza": 130,
    "Beef Burger": 100,
    "Chicken Burger": 80
}

update = []

while True:
  item_name = input("Enter item to be deleted (Press enter to exit): ").title()
  if item_name == '' and update:
    print('The new menu:')
    print(*update, sep="\n")
    break
  elif item_name == '':
    break
  elif item_name in menu:
    sure_msg = input(
        f'Are you sure you want to delete {item_name}? (y/n): ').lower()
    if sure_msg == 'n':
      continue
    elif sure_msg == 'y':
      del menu[item_name]
      update = [f'{item} : {price:.2f} EGP' for item, price in menu.items()]
    else:
      print('Renter your choice')
      continue
  else:
    print('Item not found')
    continue