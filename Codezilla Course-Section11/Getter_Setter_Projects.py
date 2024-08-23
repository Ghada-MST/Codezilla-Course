
#project1##################################################################
# available treatments 
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
while True:
  treatment_name = input('Enter treatment name (Press enter to exit): ').title()
  if treatment_name == "":
    break
  information = inventory.get(treatment_name,'Not available')
  
  if information != 'Not available':
    print(f'''Item:{treatment_name}
Price: {information['price']}
Quantity:{information['quantity']}''')
     
  else:
    print(information)

#project2##################################################################
 
employees = { 
    "Mohamed Hassan": {"age": 25, "salary": 5000, "department": 
"HR"}, 
    "Ahmed Kamal": {"age": 30, "salary": 6000, "department": 
"IT"}, 
    "Ali Adel": {"age": 35, "salary": 7000, "department": 
"IT"}, 
    "Hossam Yehia": {"age": 40, "salary": 8000, "department": 
"IT"} 
} 

while True:
  employee_name = input('Enter the employee name (Press enter to exit): ').title()

  if employee_name == "":
    break

  info = employees.get(employee_name,'Not available')
  if info != 'Not available':

    print(f'Employee: {employee_name}')
    for key,value in info.items():
      print(f"""{key.title()} : {value}""")
    
  else:
    print(info)

    
#project3##################################################################

students = { 
    "Mohamed Hassan": { 
    "Password": "123456", 
    "grades": { 
        "math": 100, 
        "english": 90, 
        "science": 80, 
        "arabic": 100,  
        "history": 97} 
    }, 
 
    "Ahmed Kamal": { 
    "Password": "1234", 
    "grades": { 
        "math": 100, 
        "english": 95, 
        "science": 93, 
        "arabic": 100, 
        "history": 94} 
    }, 
    "Ali Adel": { 
    "Password": "12", 
    "grades": { 
        "math": 85, 
        "english": 83, 
        "science": 87, 
        "arabic": 100, 
        "history": 90} 
    }, 
    "Hossam Yehia": { 
    "Password": "33", 
    "grades": { 
        "math": 100, 
        "english": 94, 
        "science": 98, 
        "arabic": 100, 
        "history": 100} 
    } 
}   

while True:
  user_input = input('Enter the student name (Press enter to exit): ').title()
  if user_input == '':
    break

  password = input('Enter the password: ')

  info = students.get(user_input,'not found')
  if info != 'not found' and info['Password'] == password:
    print(f'''Student is {user_input}
Grades:
--------------------------''')
    for subject,grade in info['grades'].items():
      print(f'{subject.title()} : {grade}')
      
    percentage = sum(info['grades'].values())/len(info['grades'])
    print('-------------------------')
    print(f'The total percentage is {percentage:.2f}')
  else:
    print("Wrong Password or student's name")
  
      


#project4##################################################################
pharmacy_prices = { 
"panadol": 32, 
"cold free": 25, 
"omega 3": 45, 
"fuciden": 37, 
"augmentin": 50, 
"zinc": 20, 
"vitamin c": 15 
} 

treatments = input('Enter the names of treatments separated by a comma (Press enter to exit): ').strip().lower()
print('--------------------')
treatments_list = treatments.split(',')

for i,treatment in enumerate(treatments_list):
  price = pharmacy_prices.get(treatments_list[i],'Not available')
  
  print(f'{treatments_list[i].title()}: {price}')
  
#another answerمهندس اسلام 

pharmacy_prices = { 
"panadol": 32, 
"cold free": 25, 
"omega 3": 45, 
"fuciden": 37, 
"augmentin": 50, 
"zinc": 20, 
"vitamin c": 15 
} 

items = {}

user_input = input('Enter the names of treatments separated by a comma (Press enter to exit): ') .strip().lower()

print('------------------')

treatment_list = user_input.split(',')

for treatment in treatment_list:
  items[treatment] = pharmacy_prices.setdefault(treatment,'Not available')

for treatment,price in items.items():
  print(f'{treatment.title()} : {price}')
