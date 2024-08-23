#project1###########################################################
products = { 
"T-shirt": {"price": 300, "quantity": 10}, 
"Shirt": {"price": 250, "quantity": 20}, 
"Pants": {"price": 300, "quantity": 15}, 
"Shoes": {"price": 400, "quantity": 5}, 
"Socks": {"price": 25, "quantity": 7}, 
"Hat": {"price": 50, "quantity": 8}, 
"Gloves": {"price": 50, "quantity": 10}, 
"Sweater": {"price": 500, "quantity": 20}, 
"Jacket": {"price": 900, "quantity": 15}, 
"Coat": {"price": 1000, "quantity": 5}, 
"Scarf": {"price": 110, "quantity": 2}, 
} 

while True:
  user_input = input('Enter the product name (Press enter to exit): ').title().strip()

  if user_input == '':
    print('Thanks for choosing Codezilla!')
    break
    
  product_info = products.get(user_input,{})
  price = product_info.get('price','Not available')
  quantity = product_info.get('quantity','Not available')

  print(f'''Product: {user_input}
Price: {price} 
Quantity: {quantity}''')


#project2###########################################################
patients = { 
"Mohamed Hassan": {"age": 25, "disease": "Cough", "room": 1}, 
"Ahmed Kamal":{"age": 30, "disease": "Sore Throat", "room": 2}, 
"Ali Adel": {"age": 35, "disease": "Arm Fracture", "room": 3}, 
"Hossam Yehia": {"age": 40, "disease": "ACL", "room": 4} 
}

while True:
  patient_name = input('Enter the patient name (Press Enter to exit): ').title()
  if patient_name == '':
    break
  patient_info = patients.get(patient_name,{})
  age = patient_info.get("age",'Not Found')
  disease = patient_info.get("disease",'Not Found')
  room = patient_info.get("room",'Not Found')

  message = f'''Patient: {patient_name}
Age: {age}
Disease: {disease}
Room: {room}'''
  print(message)





#project3###########################################################
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
  user_input = input('Enter treatment names separated by comma (Press enter to exit): ').title()
  if user_input == '':
    break
    
  treatment_list = user_input.split(',')

  for treatment in treatment_list:
    treatment_info = inventory.get(treatment,{})
    price = treatment_info.get("price",'Not available')
    quantity = treatment_info.get("quantity",'Not available')

    print(f'''Item:{treatment}
Price: {price}
Quantity: {quantity}
--------------------------''')


#another answer مهندس اسلام

check_items={}

while True:
  user_input = input('Enter treatment names separated by comma (Press enter to exit): ').title()
  if user_input == '':
    break

  treatment_list = user_input.split(',')
  not_available = {'price':'Not available','quantity':'Not available'}

  for treatment in treatment_list:
    check_items[treatment] = inventory.get(treatment,not_available)

  for treatment,info in check_items.items():
    print(f'''Item: {treatment}
Price: {info['price']}
Quantity: {info['quantity']}
---------------------------------------''')


#project4###########################################################
students = { 
    "Mohamed Hassan": {"grades": { 
        "math": 100, 
        "english": 90, 
        "science": 80, 
        "arabic": 100,  
        "history": 97} 
    }, 
    "Ahmed Kamal": {"grades": { 
        "math": 100, 
        "english": 95, 
        "science": 93, 
        "arabic": 100, 
        "history": 94} 
    }, 
    "Ali Adel": {"grades": { 
        "math": 85, 
        "english": 83, 
        "science": 87, 
        "arabic": 100, 
        "history": 90} 
    }, 
    "Hossam Yehia": {"grades": { 
        "math": 100, 
        "english": 94, 
        "science": 98, 
        "arabic": 100, 
        "history": 100} 
    } 
}    

user_input = input('Enter student name: ').strip().title()


totlal_grades = students.get(user_input,{})
info_grades = totlal_grades.get('grades','No grades available')


print(f'Student: {user_input}')
print('********************')

if user_input in students:
  for subject,grade in info_grades.items():
    print(f'{subject.title()} : {grade}')

else:
  print(info_grades)
    