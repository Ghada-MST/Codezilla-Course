#project1#######################################################

students = { 
    "Mohamed Hassan": {"grades": { 
        "math": 100, 
        "english": 90, 
        "science": 80, 
        "arabic": 100,  
        "history": 97}, 
        "school": "Codezilla" 
    }, 
    "Ahmed Kamal": {"grades": { 
        "math": 100, 
        "english": 95, 
        "science": 93, 
        "arabic": 100, 
        "history": 94}, 
        "school": "Codezilla" 
    }, 
    "Ali Adel": {"grades": { 
        "math": 85, 
        "english": 83, 
        "science": 87, 
        "arabic": 100, 
        "history": 90}, 
        "school": "Al-Azhar" 
    }, 
    "Hossam Yehia": {"grades": { 
        "math": 100, 
        "english": 94, 
        "science": 98, 
        "arabic": 100, 
        "history": 100}, 
        "school": "Al-Azhar" 
    } 
} 
all_percentages = []
students_lst = []
for student in students:
  student_grades = students[student]['grades']
  total_student_grades = sum(student_grades.values())
  len_subjects = len(students[student]['grades'])
  percentage = total_student_grades/len_subjects
  
  all_percentages.append(percentage)
  students_lst.append(student)


max_percentage = max(all_percentages)
idx= all_percentages.index(max_percentage)
student_successed = students_lst[idx]
print(f'{student_successed} has the highest total percentage which is {max_percentage:.2f}%')
print('*'*50)
for subject, grade in students[student_successed]['grades'].items():
  print(f'{subject.title()} : {grade}')

#####another answer#################
students = { 
    "Mohamed Hassan": {"grades": { 
        "math": 100, 
        "english": 90, 
        "science": 80, 
        "arabic": 100,  
        "history": 97}, 
        "school": "Codezilla" 
    }, 
    "Ahmed Kamal": {"grades": { 
        "math": 100, 
        "english": 95, 
        "science": 93, 
        "arabic": 100, 
        "history": 94}, 
        "school": "Codezilla" 
    }, 
    "Ali Adel": {"grades": { 
        "math": 85, 
        "english": 83, 
        "science": 87, 
        "arabic": 100, 
        "history": 90}, 
        "school": "Al-Azhar" 
    }, 
    "Hossam Yehia": {"grades": { 
        "math": 100, 
        "english": 94, 
        "science": 98, 
        "arabic": 100, 
        "history": 100}, 
        "school": "Al-Azhar" 
    } 
} 

students_percentage = {}

for student in students:
  student_grades = students[student]['grades']
  total_student_grades = sum(student_grades.values())
  len_subjects = len(students[student]['grades'])
  percentage = total_student_grades/len_subjects
  students_percentage = students_percentage | {student:percentage}
  #or students_percentage[student] = percentage

max_percentage = max(students_percentage.values())

for student,percentage in students_percentage.items():
  if max_percentage == percentage:
    print(f'{student} has the highest total percentage which is {max_percentage:.2f}%')
    print('*'*50)
    for subject, grade in students[student]['grades'].items():
      print(f'{subject.title()} : {grade}')
    



#project2#############################################################
inventory = {"Paracetamol": {"price":25, "quantity":10}, 
            "Aspirin": {"price":15, "quantity":20}, 
            "Ibuprofen": {"price":20, "quantity":15}, 
            "Cough Syrup": {"price":30, "quantity":5}, 
            "Augmentin": {"price":100, "quantity":7}, 
            "Amoxicillin": {"price":80, "quantity":8}, 
            "Panadol": {"price":25, "quantity":10}, 
            "Zinc": {"price":15, "quantity":20}, 
            "Vitamin C": {"price":20, "quantity":15}, 
            "Fucidin": {"price":30, "quantity":5}, 
            "Kolanog": {"price":100, "quantity":2}, 
            } 

new_inventory = {}

print('*Welcome to codezilla pharmacy*')
intro_msg = '''Enter item name(press Enter to exit): 
1. Add new items
2. Remove items
3. Update items
4. Check Avaliable quantity
5. Print treatment information
6. Exit
'''

while True:
  choice = input(f'{intro_msg}Enter your choice : ')
  if choice == '1':
    while True:
      print('---Entering new item---')
      item_name = input('Enter item name (Press enter to exit): ').title()
      if item_name == '':
        break
      item_price = float(input('Enter item price: '))
      item_quantity = int(input('Enter item quantity: '))
      inventory.update({item_name:{'price':item_price, 'quantity':item_quantity}})
      print(f'{item_name} added successively')
      #or new_inentory[item_name] = {'price': item_price, "quantity":item_quantity}
   #inventory = {**inventory ,**new_inventory}
  
  elif choice == '2':
    while True:
      print('---Deleting item---')
      item_name = input('Entering item name to be deleted (Press enter to exit): ').title()
      if item_name == '':
        break
      elif item_name in inventory:
        double_check = input(f'Are you sure you want to delete {item_name}? (y/n): ')
        if double_check == 'y':
          del inventory[item_name]
          #inventory.pop(item_name)
          print(f'{item_name} deleted successively')
        elif double_check == 'n':
          continue
        else:
          print('Inavlid entry')
          continue
      else:
        print('Item not avaliable')
    #print(inventory)    

  elif choice == '3':
    while True:
      print('---Updating item---')
      item_name = input('Enter item name to be updated (Press enter to exit): ').title()
      if item_name == '':
        break
      elif item_name in inventory:
        item_price = float(input('Enter the new price: '))
        item_quantity = int(input('Enter the new quantity: '))
        inventory = inventory | ({item_name:{'price':item_price, 'quantity':item_quantity}})
        #inventory[item_name]['price'] = item_price
        #inventory[item_name]['quantity'] = item_quantity
        print(f'{item_name} updated successively')
      else:
        print('Item not avaliable')
    print(inventory)

  elif choice == '4':
    while True:
      print('---Checking item---')
      item_name = input('Entering item name to be checked (Press enter to exit): ').title()
      if item_name == '':
        break
      elif item_name in inventory:
        item_quantity = inventory[item_name]['quantity']
        print(f'We have {item_quantity} {item_name} units')
      else:
        print('Item not avaliable')  
        
  elif choice == '5':
    while True:
      print('---Printing treatment information---')
      item_name = input('Entering item name (Press enter to exit): ').title()
      if item_name == '':
        break
      elif item_name in inventory:
        item_quantity = inventory[item_name]['quantity']
        item_price = inventory[item_name]['price']
        print(f'''Item: {item_name}
Price : {item_price}
Quantity : {item_quantity}''')
      else:
        print('Item not avaliable') 

  
  elif choice == '6':
    break

  else:
    print('Renter your choice')
    continue
print('Have a nice day!!')