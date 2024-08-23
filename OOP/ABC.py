from abc import ABC, abstractmethod
from math import pi


#project1##############################################
class Shape(ABC):

  @abstractmethod
  def area():
    ...


class Circle(Shape):

  def __init__(self, radius):
    self.radius = radius

  def area(self):
    area = pi * self.radius**2  #3.14
    return area


class Rectangle(Shape):

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    area = self.width * self.height
    return area


class Square(Shape):

  def __init__(self, side):
    self.side = side

  def area(self):
    area = self.side**2
    return area


class Triangle(Shape):

  def __init__(self, base, height):
    self.base = base
    self.height = height

  def area(self):
    area = 0.5 * self.base * self.height
    return area


def print_area(shape):
  print(f"The area of {shape.__class__.__name__} is: {shape.area()}")


obj1 = Triangle(10, 10)
print(obj1.area())
print_area(obj1)

obj2 = Circle(10)
print(obj2.area())


#project2######################################
class BankAccount(ABC):

  def __init__(self):
    self.balance = 0

  def deposite(self, amount):
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    if amount > self.balance:
      raise ValueError("Innsufficient funds")
    self.balance -= amount
    return self.balance

  @abstractmethod
  def calculate_interest():
    ...


class SavingAccount(BankAccount):
  INTEREST_RATE = 0.03

  def calculate_interest(self):
    return self.balance * SavingAccount.INTEREST_RATE


class CheckingAccount(BankAccount):
  INTEREST_RATE = 0.01

  def calculate_interest(self):
    return self.balance * CheckingAccount.INTEREST_RATE


account1 = SavingAccount()
print(account1.balance)
account1.deposite(2000)
print(account1.calculate_interest())
account1.withdraw(500)
print(account1.balance)

account2 = CheckingAccount()
account2.deposite(4000)
print(account2.calculate_interest())
