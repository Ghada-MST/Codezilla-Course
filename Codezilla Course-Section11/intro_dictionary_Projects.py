#project1##########################################################
#1. Create a dictionary called fruits that contains the following information:
# Apple - 20
# Banana - 15
# Orange - 10
# Strawberry - 30
# Mango - 25
fruits_prices = {
    'Apple': 20,
    'Banana': 15,
    'Orange': 10,
    'Strawberry': 30,
    'Mango': 25
}
print(fruits_prices)

#project2###################################################################
#1. Create a dictionary called students that contains the following information:
# Mohamed Hassan - 83
# Ahmed Khaled - 97
# Ali Hamed - 75
# Mahmoud Samir - 89
students_grades = {
      'Mohamed Hassan': 83,
      'Ahmed Khaled': 97,
      'Ali Hamed': 75,
      'Mahmoud': 89
}
print(students_grades)

#project3#################################################################
#Create a dictionary called drinks that contains the following information:
# Coke - 10
# Sprite - 8
# Fanta - 8
# Pepsi - 10

drinks_prices = {
      'Coke': 10,
      'Sprite': 8,
      'Fanta': 8,
      'Pepsi': 10
}
print(drinks_prices)

#project4############################################################3#
#Create a dictionary with the order of codezilla students in a competition.
# The key is the order and the value is the name of the student
# 1 - Mohamed Ahmed
# 2 - Ahmed Khaled
# 3 - Ali Hamed
# 6 - Mahmoud Samir
# 8 - Ahmed Hassan

names = {
      1:'Mohamed Ahmed',
      2:'Ahmed Khaled',
      3:'Ali Hamed',
      6:'Mahmoud Samir',
      8:'Ahmed Hassan'
}
print(names)

#project5################################################################
grades = {
("Ahmed", "Hassan"): 87,
("Hossam", "Ali"): 90,
("Mohamed", "Kamel"): 74,
("Ali", "Hamed"): 100,
("Ahmed", "Khaled"): 95
}
print(grades)

#project6################################################################

pizzas = {
"Margherita": 100, 
"Pepperoni": 120, 
"Meat Lovers": 150, 
"Chicken": 130,
"Cheese": 100,
"Veggie": 120,
"Hawaiian": 150,
}

print(pizzas["Pepperoni"])
print(pizzas["Chicken"])
print(pizzas["Hawaiian"])


#project7################################################################
drinks = {
"Coke": 30,
"Sprite": 25,
"Fanta": 25,
"Pepsi": 30,
"Tea": 20,
"Coffee": 25,
"Orange Juice": 30,
"Mango Juice": 30
}
print(drinks["Coke"])
print(drinks["Mango Juice"])
print(drinks["Tea"])
print(drinks["Coffee"])


#project8################################################################
menu = {
"Cheese pizza": 100,
"Veggie pizza": 120,
"Hawaiian pizza": 150,
"Coke": 30,
"Sprite": 25,
"Fanta": 25,
"Pepsi": 30
}
menu['Ice Cream'] = 30
menu["Chocolate Cake"]  = 60
menu ['Cheese Cake']= 70
menu ['Brownie'] = 40
menu ['Donut'] = 30
menu ['Hawaiian pizza'] = 190
print(menu)

#project9################################################################
drinks = {
"Latte": 30,
"Coke": 30,
"Sprite": 25,
"Fanta": 25,
"Pepsi": 30,
"Tea": 20,
"Coffee": 25,
"Orange Juice": 30,
"Mango Juice": 30
}
print(drinks['Coke'])
print(drinks["Sprite"])
print(drinks["Fanta"])
print(drinks["Pepsi"])

#project10################################################################

# Available Pizzas:
pizzas = {"Margherita": 100, "Pepperoni": 120, "Meat Lovers": 
150, "Chicken": 130}

print('Avaliable pizzas:')
for pizza in pizzas:
  print(f'{pizza} costs {pizzas[pizza]}')
