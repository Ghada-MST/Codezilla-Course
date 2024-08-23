class TransactionsHistory:

  def __init__(self):
    self._transaction_history = []

  def add_transaction(self, trans):
    self._transaction_history.append(trans)

  def get_transaction_history(self):
    return self._transaction_history


class BankAccount:

  def __init__(self, account_id, balance=0):
    self._account_id = account_id
    self._balance = balance
    self._transaction_history_instance = TransactionsHistory()

  def check_balance(self, account_id):
    if self._account_id == account_id:
      return self._balance
    raise ValueError("Your aren't allowed to check the balance")

  def deposit(self, amount):
    self._balance += amount
    self._transaction_history_instance.add_transaction(f"Dposit: {amount}")

  def withdraw(self, amount):
    if amount > self._balance:
      print('Insufficient funds')
    else:
      self._balance -= amount
      self._transaction_history_instance.add_transaction(f"Withdraw: {amount}")

  def __str__(self):
    transaction_history_string = '\n'.join(
      self._transaction_history_instance.get_transaction_history())
    return f"\nAccount id: {self._account_id} \nTransaction History: \n{transaction_history_string}"


class SavingsAccount(BankAccount):

  def __init__(self, account_id, balance, interest_rate=0.03):
    super().__init__(account_id, balance=0)
    self.interest_rate = interest_rate

  def apply_interest(self):
    interest_amount = self._balance * self.interest_rate
    self._balance += interest_amount
    self._transaction_history_instance.add_transaction(
      f"Interest applied: {interest_amount}")


class CurrentAccount(BankAccount):
  OVERDRAFT_FEE = 0.01

  def __init__(self, account_id, balance, overdraft_limit=500):
    super().__init__(account_id, balance)
    self.overdraft_limit = overdraft_limit

  def withdraw(self, amount):
    if self._balance - amount < -self.overdraft_limit:
      raise ValueError("This withdrawl exceeds your overdraft limit")
    self._balance -= amount
    self._transaction_history_instance.add_transaction(f"Withdraw: {amount}")
    if self._balance < 0:
      self.apply_overdraft_fee()

  def apply_overdraft_fee(self):
    overdraft_amount = -self._balance * CurrentAccount.OVERDRAFT_FEE
    self._balance -= overdraft_amount
    self._transaction_history_instance.add_transaction(
      f"Applied overdraft fee: {overdraft_amount}")


class Client:
  PHONE_PREFIX = "+20"
  PHONE_LENGHT = 12

  def __init__(self, client_id, client_name, client_phone, client_address):
    self.__id = client_id
    self.__name = client_name
    self.__phone = client_phone
    self.__address = client_address
    self.__bank_accounts = []

  def add_bank_account(self, account):
    self.__bank_accounts.append(account)

  def get_bank_accounts(self,id):
    if self.__id == id:
      for acc in self.__bank_accounts:
         print(acc)
    else:
      raise ValueError("wrong id or not allowed to access this info")

  def __repr__(self):
    return f"{self.__class__.__name__} id: ({self.__id}) name:{self.__name}"

  @property
  def name(self):
    return self.__name

  @property
  def id(self):
    return self.__id

  @property
  def phone(self):
    return self.__phone

  @phone.setter
  def phone(self, new_phone):
    if isinstance(new_phone, str) and Client.isvalid_phone(new_phone):
      self.__phone = new_phone
    else:
      raise ValueError("Invalid phone number format")

  @staticmethod
  def isvalid_phone(phone):
    return phone.startswith(
      Client.PHONE_PREFIX) and len(phone) == Client.PHONE_LENGHT

  @property
  def address(self):
    return self.__address

  @address.setter
  def address(self, new_address):
    self.__address = new_address

  def subscribe(self, event):
    print(f"{event.title} is on {event.date} has been added to your calender")


class Event:

  def __init__(self, title, date):
    self.title = title
    self.date = date

  def party(self):
    print(f"Event: {self.title} is on {self.date}")


saving1 = SavingsAccount("EGS1", 1000)
current1 = CurrentAccount("EGC1", 2000)

current1.deposit(1000)
print(current1)
print(current1.check_balance("EGC1"))
current1.withdraw(1000)
print(current1.check_balance("EGC1"))
current1.withdraw(2500)
print(current1.check_balance("EGC1"))
print(current1)
saving1.deposit(1000)
print(saving1)
saving1.apply_interest()
print(saving1)
current1.apply_overdraft_fee()
print(current1)
# Example usage for Client class
client1 = Client("123", "John Doe", "+20123456789", "NY")
client1.add_bank_account(saving1)
client1.add_bank_account(current1)


event = Event("New Year's event", "29/12/2023")
event.party()
client1.subscribe(event)
print(client1.name)
print(client1.id)
client1.get_bank_accounts("123")
print(client1)
client1.phone = "+20105580898"
print(client1.phone)