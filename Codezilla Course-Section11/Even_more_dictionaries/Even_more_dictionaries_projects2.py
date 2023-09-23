
#project1#####################################################################
pizzas = {"Margherita": 100, "Pepperoni": 120, 
"Meat Lovers": 150, "Chicken": 130}

order = input('What is the pizza you want?? ').title()


if order in pizzas:
  print(f'{order} costs {pizzas[order]}')
  
else:
  print(f'Sorry pizza {order} isn\'t available')
  
  
print()
print()

#project2#####################################################################
pizzas = {"Margherita": 100, "Pepperoni": 120, "Meat Lovers": 
150, "Chicken": 130}

#Print the menu after increasing the prices by 20%.
for pizza, price in pizzas.items():
  new_price = price*1.2
  print(f'{pizza} pizza price is : {new_price} LE')


#another answer
# loop over the pizzas
for pizza in pizzas:
# get the price
  price = pizzas[pizza]
# increase the price by 20%
  pizzas[pizza] = price + (price * 0.2)
# print the pizzas
for pizza in pizzas:
  print(f"{pizza}: {pizzas[pizza]} EGP")


print()
print()

#project3#####################################################################
pizzas = {"Margherita": 100, 
"Pepperoni": 120, 
"Meat Lovers": 150, 
"Chicken": 130,
"Chicken Ranch": 140,
"Cheese": 110
}
for pizza,price in pizzas.items():
  print(f'The price of {pizza} pizza is {price} LE')


print()
print()

#project4#####################################################################
schools = {
"Codezilla School":
{'1100':"Mohamed Gouda", '1101':"Islam Hesham", 
'1102':"Ayman Mohamed", '1103':"Ahmed Khaled"},
"Al Dorra School":
{'2100':"Ahmed Hassan", '2101':"Mahmoud Ali", 
'2102':"Adham Wael", '2103':"Khaled Ali"},
"Mostafa Kamel School":
{'3105':"Hazem Ahmed", '3106':"Omar Mohamed", 
'3107':"Hussein Kamal", '3109':"Ali Ahmed"}
}

students_name_id = input('Enter the student\'s name or his id: ')


for school in schools:
  for id, name in schools[school].items():
    if students_name_id.title() == name or students_name_id == id:
      print(f'The student name is {name}, his id is {id} and his school is: {school}')
  else:
    print('Sorry This name or id has no data here')
    break

#another answer مهندس اسلام
# get user input
user_input = input("Enter student name or id to search for: ").title()
# flag to check if the user input is found or not
not_found = True
# loop over the schools
for school in schools:
# get the students ids and names
  students_ids = schools[school].keys()
  students_names = schools[school].values()
# check if the user input is in the students ids or names
  if (user_input in students_ids) or (user_input in
  students_names):
    print(f"{user_input} is a student in {school}")
    not_found = False
    break
# if the user input is not found 
if not_found:
  print(f"{user_input} is not in our records")
  
print()
print()

#project5#####################################################################

employees = {
"Ahmed Hassan": 12_000,
"Mohamed Ahmed": 20_000,
"Ali Ahmed": 15_000,
"Khaled Ali": 10_000,
"Omar Mohamed": 13_000,
"Hazem Ahmed": 24_000
}

#Increase the salaries of the following employees by 40%.

for employee in employees:
  salary = employees[employee]
  employees[employee] += salary*0.40
print('Annoucement The new salaries for our employees as the following:')
  
for employee, salary in employees.items():
  
  print(f'{employee} new salary is {salary:,.0f}')


#another answer

print('Annoucement The new salaries for our employees as the following:')

for employee , salary in employees.items():
  salary *= 1.40
  print(f'{employee} new salary is {salary:,.0f}')


