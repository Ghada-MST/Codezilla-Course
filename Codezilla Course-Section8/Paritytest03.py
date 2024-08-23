

amount_of_money = float(input("Enter the amount of money you have: "))

print('-'*20)

item1_price = float(input("Enter the price of the first item : "))
item2_price = float(input("Enter the price of the second item : "))
item3_price = float(input("Enter the price of the third item : "))

print('-'*20)
total_prices = item1_price + item2_price + item3_price 
diff_money = amount_of_money - total_prices 

if  total_prices <= amount_of_money:
  print(f"Items have been purchased successfully \nThe remaining amount is {diff_money:.2f}$")

else:
  print(f"Sorry, You don't have enough balance \nYou need to add extra {-diff_money:.2f}$")