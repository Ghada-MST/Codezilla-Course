#project1#########################################


class Item:

  num_of_items = 0
  all_items = []

  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity
    self.total_price = self.price * self.quantity
    Item.num_of_items += 1
    Item.all_items.append(self)

  def __repr__(self):
    return f"Item {self.name,self.price,self.quantity,self.total_price}"


print(f"Number of items: {Item.num_of_items}")

# Create an item
item1 = Item("Atomic Habits", 10, 2)
item2 = Item("Deep Work", 20, 1)
item3 = Item("So Good They Can't Ignore You", 15, 3)
item4 = Item("Digital Minimalism", 12, 2)

# Display the number of items
print(f"Number of items: {Item.num_of_items}")
# output:
# Number of items: 4

# Display all items
print(Item.all_items)
# output:
# [Item('Atomic Habits', 10, 2), Item('Deep Work', 20, 1),
# Item('So Good They Can't Ignore You', 15, 3), Item('Digital Minimalism', 12, 2)]

# print each item in all_items
for item in Item.all_items:
  print(f"""
Name:{item.name}
Price: ${item.price}
Quantity: {item.quantity}
Total Price: ${item.total_price}""")
  print("##################")
# output:
# Name: Atomic Habits
# Price: $10
# Quantity: 2
# Total Price: $20
# ##################
# Name: Deep Work
# Price: $20
# Quantity: 1
# ...

#project2#########################################


class BankAccount:
  bank_name = "Codezilla"
  all_accounts = []
  num_of_accounts = 0

  def __init__(self, account, balance):
    self.account = account
    self.balance = balance
    BankAccount.all_accounts.append(self)
    BankAccount.num_of_accounts += 1

  def display_balance(self):

    print(f"Account {self.account} balance: ${self.balance}")

  def add_money(self, money):

    if money > 0:
      self.balance += money
      print(f"added {money} into account {self.account}.")
    else:
      print("Invalid amount. added amount must be positive.")

  def withdraw(self, money):

    if self.balance < money or money < 0:
      print("Insufficient funds or invalid ")
    else:
      self.balance -= money
      print(f"Withdrew {self.balance} from account {self.account}.")

  def __str__(self) -> str:

    return f"""
Account Number: {self.account}
Balance: ${self.balance}"""

  def __repr__(self) -> str:

    return f"BankAccount('{self.account}',{self.balance})"


print(BankAccount.bank_name)  # Codezilla

account1 = BankAccount("5577", 1000)
account2 = BankAccount("1234", 2000)

print(BankAccount.num_of_accounts)
# 2
print(account1.balance)
print(BankAccount.all_accounts)
# [BankAccount('5577', 1000), BankAccount('1234', 2000)]
account1.display_balance()
# Account 5577 balance: 1000
account2.display_balance()
# Account 1234 balance: 2000
account1.add_money(500)  # added 500 into account 5577.
account1.display_balance()  # Account 5577 balance: 1500
account2.withdraw(1000)  # Withdrew 1000 from account 1234.
account2.display_balance()  # Account 1234 balance: 1000
account1.withdraw(2000)  # Insufficient funds or invalid amount.
account1.withdraw(-1000)  # Insufficient funds or invalid amount.
print(account1)
# Account Number: 5577
# Balance: $1500
print(account2)

# Account Number: 1234
# Balance: $1000
