#project1##########################
# 1. Fix the Hamada Class
class Hamada:

  def __init__(self, name, age, job):
    self.name = name
    self.age = age
    self.job = job

  def stupid(self, name, opinion=True):
    if opinion:
      print(f'{self.name} is stupid')
    else:
      print(f'{self.name} is not stupid')


# make an instance of the class Hamada
hamada = Hamada('Hamada', 25, "IT")
# print the attributes of the instance
print(hamada.name)
print(hamada.age)
print(hamada.job)
# call the method stupid() of the instance
hamada.stupid("Hamada", opinion=False)
# add an attribute to the instance hamda
hamada.phonenumber = '0123456789'
# print the attribute phonenumber of the instance
print(hamada.phonenumber)
# Edit the attribute age of the instance hamada
hamada.age = 35
# print the attribute age of the instance
print(hamada.age)


#project2##########################
class Item:

  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def display(self):
    total_price = self.price * self.quantity
    print(f"""
Name: {self.name}
Price: ${self.price}
Quantity: {self.quantity}
Total price: ${total_price}""")


item1 = Item("Atomic Habits", 10, 2)
item2 = Item("Deep Work", 20, 1)
# Display item information
item1.display()
item2.display()

# output# Result item1:
# Name: Atomic Habits
# Price: $10
# Quantity: 2
# Total Price: $20
# # Result item2:
# Name: Deep Work
# Price: $20
# Quantity: 1
# Total Price: $20


#project3##########################
class BankAccount:

  def __init__(self, account, balance):
    self.account = account
    self.balance = balance

  def display_balance(self):
    print(f'Account {self.account} balance: {self.balance}')

  def add_money(self, money):
    if money > 0:
      self.balance += money
      print(f"added {money} into account {self.account}.")
    else:
      print("Invalid amount. added amount must be positive.")

  def withdraw(self, money):
    if money < self.balance:
      self.balance -= money
      print(f"Withdrew {money} from account {self.account}.")
    else:
      print("Insufficient funds or invalid amount.")

  def __str__(self):
    return "hello"


account1 = BankAccount("5577", 1000)
account1.display_balance()  # Account 5577 balance: 1000
account1.add_money(500)  # added 500 into account 5577.
account1.display_balance()  # Account 5577 balance: 1500
account1.add_money(-100)
# Invalid amount. added amount must be positive.
account1.display_balance()  # Account 5577 balance: 1500
account1.withdraw(200)  # Withdrew 200 from account 5577.
account1.display_balance()  # Account 5577 balance: 1300
account1.withdraw(1500)
# Insufficient funds or invalid amount.
account1.display_balance()  # Account 5577 balance: 1300
