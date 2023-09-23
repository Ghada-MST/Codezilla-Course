
#project1############################################################################

menu = {"Margherita Pizza": 100, "Pepperoni Pizza": 120, 
"Meat Lovers Pizza": 150, "Chicken Pizza": 130} 

update = False
while True:
  new_item = input('Enter the name of the item to add to the menu (press Enter to exit): ').title()
  if new_item == '':
    break
  else:
    item_price = float(input('Enter item price: '))
    #menu[new_item] = item_price
    menu.update({new_item:item_price})
    update = True

if update:
  print('The new menu:')
  for item,price in menu.items(): 
    print(f'{item} : {price:.2f} EGP')


#project2############################################################################

menu = {"Margherita Pizza": 100, "Pepperoni Pizza": 120,  
"Meat Lovers Pizza": 150, "Chicken Pizza": 130, 
"Beef Burger": 100, "Chicken Burger": 80} 


update = False
while True:
  item_name = input("Enter item to be deleted (Press enter to exit): ").title()
  if item_name == '':
    break
  elif item_name in menu:  
    sure_msg = input(f'Are you sure you want to delete {item_name}? (y/n): ').lower()
    if sure_msg == 'n':
      continue
    elif sure_msg == 'y':
      #menu.pop(item_name)
      del menu[item_name]
      update = True
    else:
      print('Renter your choice')
      continue
  else:
    print('Item not found')
    continue
    
if update:
  print('The new menu:')
  for item,price in menu.items(): 
    print(f'{item} : {price:.2f} EGP')


#project3############################################################################
menu = {"Margherita Pizza": 100, "Pepperoni Pizza": 120,  
"Meat Lovers Pizza": 150, "Chicken Pizza": 130, 
"Beef Burger": 100, "Chicken Burger": 80} 

old_menu = menu.copy()

while True:
  update_item = input("Enter item name to be updated (Press enter to exit): ").title()
  if update_item == '':
    break
  elif update_item not in menu:
    print('Item not found')
    continue  
  else:
    new_price = float(input('Enter the new price: '))
    menu[update_item] = new_price
    print(f'{update_item} has been updated')
    
if sum(menu.values()) != sum(old_menu.values()): 
  print('The new menu: ')
  for item, price in menu.items():
    print(f'{item} : {price:.2f} EGP')


    
#project4############################################################################
menu = {"Margherita Pizza": 100, "Pepperoni Pizza": 120,
"Meat Lovers Pizza": 150, "Chicken Pizza": 130,
"Beef Burger": 100, "Chicken Burger": 80}

old_menu = menu.copy()
sum_old_menu = sum(old_menu.values())


while True:
  choice = input("""1. Add new items
2. Remove items
3. Update items
4. Exit

Enter your choice: """)
  
  if choice == '1':
    item = input('Enter the name of the item to add to the menu (Press Enter to exit): ').title()
    if item == "":
      continue
    price = float(input('Enter item price: '))
    menu[item] = price
    print(f'{item} has been added')
    
  elif choice == '2':
    item = input('Enter the item name to be deleted (Press Enter to exit): ').title()
    if item == "":
     continue
    elif item not in menu:
      print('Item not avaliable in the menu')
      continue
    sure_msg = input(f'Are you sure you want to delete {item}? (y/n): ').lower()
    if sure_msg == 'y':
      del menu [item] 
      print(f'{item} has been deleted')
    elif sure_msg == 'n':
      continue
    else:
      print('Renter your choice')
      continue
  elif choice == '3':
    item = input('Enter the item name to be updated (Press Enter to exit): ').title()
    if item == "":
      continue
    elif item not in menu:
      print('Item not avaliable in the menu')
      continue
    price = float(input('Enter the new price: '))
    menu.update({item:price})
    print(f'{item} has been updated')
  

  elif choice == "4":
    break

if sum_old_menu != sum(menu.values()):
  print('The new menu:')
  for item,price in menu.items():
    print(f'{item} : {price:.2f} EGP')





#project5############################################################################
from random import choice
words = {
"Absence":"The lack or unavailability of something or someone.",
"Approval":"Having a positive opinion of something or someone.",
"Answer":"The response or receipt to a phone call, question, or letter.",
"Attention":"Noticing or recognizing something of interest.",
"Amount":"A mass or a collection of something",
"Borrow":"To take something with the intention of returning it after a period of time.",
"Baffle":"An event or thing that is a mystery and confuses.",
"Ban":"An act prohibited by social pressure or law.",
"Banish":"Expel from the situation, often done officially.",
"Banter":"Conversation that is teasing and playful.",
"Characteristic":"referring to features that are typical to the person, place, or thing.",
"Cars":"Four-wheeled vehicles used for traveling.",
"Care":"extra responsibility and attention.",
"Chip":"a small and thin piece of a larger item.",
"Cease":"to eventually stop existing.",
"Dialogue":"A conversation between two or more people.",
"Decisive":"a person who can make decisions promptly."
}
key_list = list(words)

print('Welcome to English helper program ')

while True:
  print("""\n1. Review random word
2. Test yourself
3. Exit""")
  
  random_word = choice(key_list)
  definition = words[random_word]
  
  option = input("Enter your choice: ")

  if option == "1":
    print(f'''Word: {random_word}
Definition: {definition}''')
    continue
    
  elif option == "2":
    print(f'Definition: {definition}')
    for attempt in range(2,0,-1):
      answer = input('Guess the word: ').title()
      if answer != random_word:
        if attempt == 1 :
          print(f'''Wrong answer you have no more attempts
The word is {random_word}''')
          break
        print(f'Wrong answer you have {attempt-1} more attempt')
        
      elif answer == random_word:
        print("well done ✅")
        break
        
  elif option == "3":  
    break

  else:
    print('Invalid option')

print('Have a nice day!')

#another answer for option 2

# elif option == 2:
#   print(f'Definition: {definition}')
  
#   for i in range(2):
#    answer = input('Guess the word: ').title()
#    if answer == random_word:
#       print("well done ✅")
#       break 
#    else:
#      if i == 0:
#        print(f'Wrong answer you have one more attempt')
#      else:
#        print(f'''Wrong answer you have no more attempts
# The word is {random_word}''')