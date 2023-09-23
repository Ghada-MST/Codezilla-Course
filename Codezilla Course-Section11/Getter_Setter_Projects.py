
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
#     print(f'''Employee: {employee_name}
# Age: {employees[employee_name]["age"]}
# Salary: {employees[employee_name]["salary"]}
# Department:{employees[employee_name]["department"]}''')
    print(f'Employee: {employee_name}')
    for key,value in info.items():
      print(f"""{key.title()} : {value}""")
    
  else:
    print(info)
