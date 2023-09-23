order_cost = input("Enter order cost: ")
Total_cost = float(order_cost) + float(order_cost) * 0.1
print("The Total is " + str(Total_cost))

print()

amount_of_money = input("enter amount of money: ")
num_of_childern = input("enter number of childern: ")
currency = input("enter currency: ")
each_child_money = float(amount_of_money) / float(num_of_childern)
print("-"*30)
print("Each one should get " + str(round(each_child_money, 2)), currency)