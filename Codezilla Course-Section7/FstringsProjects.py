#fstrings projects

order_cost = float(input("Enter order cost: "))
Total_cost = order_cost + order_cost * 0.1
print(f"The Total is {Total_cost}")


print()

amount_of_money = input("enter amount of money: ")
num_of_childern = input("enter number of childern: ")
currency = input("enter currency: ")
each_child_money = float(amount_of_money) / float(num_of_childern)
print("-"*30)
print(f"Each one should get {each_child_money:.2f} {currency}")


print()

name = input ("enter your name: ").title().strip() 
print(f'Welcome {name} at Codezilla Python Course \nYour name is {len(name)} characters long')


print()


#lessons praticing

print(f'your name lenght is {len("dodo")}')


name = 'codezilla'
print(f'hello, "{name}"')

print("yur name is {len('ahmed')}")