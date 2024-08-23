

#project1#####################################################################
pizzas = {
"Margherita": 100, 
"Pepperoni": 120, 
"Meat Lovers": 150, 
"Chicken": 130,
"Cheese": 100,
"Veggie": 120,
"Hawaiian": 150,
}
# Pizzas to print:
# Pepperoni
# Chicken
# Hawaiian

for pizza ,price in pizzas.items():
  if pizza == 'Pepperoni' or pizza == 'Chicken' or pizza == 'Hawaiian':
    print(f'Pizza {pizza} costs {price}$')


#another answer

pizza_to_get = ['Pepperoni','Chicken','Hawaiian']
for pizza, price in pizzas.items():
  if pizza in pizza_to_get:
    print(f'{pizza} costs {price} LE')

#another answer
pizza_to_get = ['Pepperoni','Chicken','Hawaiian']
for pizza in pizza_to_get:
    print(f'{pizza} costs {pizzas[pizza]} LE')


print()
print()
#project2#####################################################################

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
# Drinks to print:
# Coke
# Mango Juice
# Tea
# Coffee
drinks_to_print = ['Coke','Mango Juice','Tea','Coffee']
for drink in drinks_to_print:
  print(f'{drink} costs {drinks[drink]}')

print()
print()
#project3#####################################################################
menu = {
"Cheese pizza": 100,
"Veggie pizza": 120,
"Hawaiian pizza": 150,
"Coke": 30,
"Sprite": 25,
"Fanta": 25,
"Pepsi": 30
}
#add the following
# Ice Cream - 30
# Chocolate Cake - 60
# Cheese Cake - 70
# Brownie - 40
# Donut - 30
menu['Ice Cream'] = 30
menu['Chocolate Cake'] = 60
menu['Cheese Cake'] = 70
menu['Brownie'] = 40
menu['Donut'] = 30

print(menu)

#another answer
for dessert ,price in new_menu.items():
  menu[dessert] = price
  
print(menu) 

#another answer
new_menu = {'Ice Cream':30,'Chocolate Cake':60, 'Cheese Cake':70, 'Brownie':40, 'Donut':30}

for key,value in new_menu.items():
  menu.update({key:value})
  
print(menu)


print()
print()



#project4#####################################################################
menu = {
"Cheese pizza": 100,
"Veggie pizza": 120,
"Hawaiian pizza": 150,
"Coke": 30,
"Sprite": 25,
"Fanta": 25,
"Pepsi": 30
}
#Increase the prices of pizzas by 20 percent then print the restaurant menu.

for key,value in menu.items():
  if 'pizza' in key:
    value += value*0.20 # if value = 100, amount of increasing price value*.20 = 20
    menu[key] = value

for key,value in menu.items():
  print(f'{key} costs {value}')



#another answer
# loop through the menu
for item, price in menu.items():
# check if the item is a pizza and update the price
  if "pizza" in item:
    menu[item] = price * 1.2
# print the menu
for item, price in menu.items():
  print(f"{item}: {price} EGP")

print()
print()


#project5#####################################################################

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
soda_drinks = 'Coke','Sprite','Fanta','Pepsi'
for drink, price in drinks.items():
  if drink in soda_drinks:
    print(f'{drink} costs {price}$')