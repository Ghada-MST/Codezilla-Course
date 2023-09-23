#project1#############################################################

schools = { 
    "Codezilla": 
        {"Mohamed Hassan":  
            {"math": 100, 
            "english": 90, 
            "science": 85, 
            "arabic": 100,  
            "history": 97}, 
        "Ahmed Kamal": 
            {"math": 100, 
            "english": 95, 
            "science": 93, 
            "arabic": 100, 
            "history": 94} 
        }, 
 
 
    "Al-Azhar":{ 
        "Ali Adel": { 
            "math": 85, 
            "english": 83, 
            "science": 87, 
            "arabic": 100, 
            "history": 90}, 
        "Mariam Ali": { 
            "math": 100, 
            "english": 94, 
            "science": 98, 
            "arabic": 100, 
            "history": 100} 
} 
} 
school_average = {}

for school in schools:
  len_students = len(schools[school])
  percentage_all_students = 0

  for student in schools[school]:
    sum_grades_student = sum(schools[school][student].values())
    len_subjects = len(schools[school][student])
    percentage_per_student = sum_grades_student/len_subjects
    
    percentage_all_students += percentage_per_student
  
  
  average = percentage_all_students/len_students
  
  school_average.update({school : average}) 
  
for school, average in school_average.items():
  print(f'The average total percentage for {school} school is {average:.2f}')
print(school_average)

#another answer
schools = { 
 "Codezilla":{ 
         "Mohamed Hassan":{ 
         "math": 100, 
         "english": 90, 
         "science": 85, 
         "arabic": 100, 
         "history": 97 
         }, 
         "Ahmed Kamal":{ 
         "math": 100, 
         "english": 95, 
         "science": 93, 
         "arabic": 100, 
         "history": 94 
         } 
 }, 
 "Al-Azhar":{ 
         "Ali Adel": { 
         "math": 85, 
         "english": 83, 
         "science": 87, 
         "arabic": 100, 
         "history": 90 
         }, 
         "Mariam Ali": { 
         "math": 100, 
         "english": 94, 
         "science": 98, 
         "arabic": 100, 
         "history": 100 
         } 
 }} 

average_grade_school = [] 
for school, info in schools.items(): 
    for student, grade in info.items(): 
      list_grade_student = [grade_subject for subject, grade_subject in grade.items()] 
      average_grade_student = sum(list_grade_student) / len(list_grade_student) 
      average_grade_school.append(average_grade_student)    
      total_average_school = sum(average_grade_school) / len(average_grade_school) 
    print(f'The Average Total for {school} school is: {total_average_school:.2f}') 
    average_grade_school.clear() 
    print('-'*30) 
 





#project2#############################################################
hot_drinks = {"Coffee": 20, "Tea": 15, "Hot Chocolate": 25} 
cold_drinks = {"Soda": 10, "Iced Tea": 15, "Smoothie": 30} 
desserts = {"Ice Cream": 50, "Chocolate Cake": 60, "Cheesecake": 70} 


menu = {'hot_drinks': hot_drinks,'cold_drinks':cold_drinks,'desserts':desserts}

#make a list of different items' types
menu_lst = ['hot_drinks','cold_drinks','desserts']

#make an empty list to put the order in
order = []

print('Welcome to Codezilla Cafe')

while True:
  #build list for items
  items_lst = []
  option = input('''1. Hot Drinks
2. Cold Drinks
3. Desserts
Please, Enter the number of the item type (Enter to exit): ''')
  
  
  if option == '':
    break
  option = int(option)
  #put a range for options, max range is the lenght of above menu list
  if 1<= option <= (len(menu_lst)):
    #to get the item type iterate through menu list by the mean of option minus 1 
    item_type = menu_lst[option-1]
    #print the menu by enumerate menu with item type as a key
    for idx,(item,price) in enumerate(menu[item_type].items(),1):
      print(f'{idx}.{item} : {price} EGP')
      #create a list of items for chosen item type 
      items_lst.append(item)
    item_num = int(input('Enter item number: '))
    #put a range for item numbers, max range is the lenght of above items list
    if 1<=item_num<=len(items_lst):
      quantity = int(input('Enter item quantity: '))
      #to get the item iterate through items list by the mean of item number minus 1
      item = items_lst[item_num-1]
      price = menu[item_type][item]
      total = price*quantity
      #build a list of dictionaries for the user order
      order.append({'Item':item,'Price':price,'Quantity':quantity,'Total': total})
    else:
      print('Invalid option')
      continue  
  else:
    print('Invalid option')
    continue
#print the order   
if order:
  print(f"{'-'*20} \nYour order is\n{'-'*20}")
  for dict in order:
    for key,value in dict.items():
      print(f'{key} : {value} EGP')
    print('-'*20)
else:
  print('No order found\nhave a nice day!!!')









#another answer################


#project2#############################################################
hot_drinks = {"Coffee": 20, "Tea": 15, "Hot Chocolate": 25} 
cold_drinks = {"Soda": 10, "Iced Tea": 15, "Smoothie": 30} 
desserts = {"Ice Cream": 50, "Chocolate Cake": 60, "Cheesecake": 70} 


menu = {'hot_drinks': hot_drinks,'cold_drinks':cold_drinks,'desserts':desserts}

#make a list of different items' types
menu_lst = ['hot_drinks','cold_drinks','desserts']

#make an empty list to put the order in
order = {}

print('Welcome to Codezilla Cafe')

while True:
  #build list for items
  items_lst = []
  option = input('''1. Hot Drinks
2. Cold Drinks
3. Desserts
Please, Enter the number of the item type (Enter to exit): ''')
  
  
  if option == '':
    break
  option = int(option)
  #put a range for options, max range is the lenght of above menu list
  if 1<= option <= (len(menu_lst)):
    #to get the item type iterate through menu list by the mean of option minus 1 
    item_type = menu_lst[option-1]
    #print the menu by enumerate menu with item type as a key
    for idx,(item,price) in enumerate(menu[item_type].items(),1):
      print(f'{idx}.{item} : {price} EGP')
      #create a list of items for chosen item type 
      items_lst.append(item)
    item_num = int(input('Enter item number: '))
    #put a range for item numbers, max range is the lenght of above items list
    if 1<=item_num<=len(items_lst):
      quantity = int(input('Enter item quantity: '))
      #to get the item iterate through items list by the mean of item number minus 1
      item = items_lst[item_num-1]
      price = menu[item_type][item]
      total = price*quantity
      
      #build a dict of dictionaries for the user order
      order[item] = {'Price':price,'Quantity':quantity,'Total': total}
    else:
      print('Invalid option')
      continue  
  else:
    print('Invalid option')
    continue

total_order_costs = sum([order[item]['Total'] for item in order])
#print(order)
if order:
  print(f"{'-'*20} \nYour order is\n{'-'*20}")
  for item,info in order.items():
    print(f"""Item : {item}
Price : {info['Price']}
Quantity : {info['Quantity']}
Total : {info['Total']} EGP""")
    print('-'*20)


else:
   print('No order found\nhave a nice day!!!')

print(f'The total order price is: {total_order_costs}')

      



     



