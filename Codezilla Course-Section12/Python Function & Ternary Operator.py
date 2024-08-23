#project1-1#####################################################
#Make a function that sees if two numbers are
#divisible by each other or not with the default option
#to see if the number is divisible by 2 or not in 4 different ways.


#using if statement
def divisible_by_2(number, divisor=2):
  if number % divisor == 0:
    return True

  else:
    return False


#using return statement
def divisible_by_2(number, divisor=2):
  if number % divisor == 0:
    return True

  return False


#using ternary operator
def divisible_by_2(number, divisor=2):
  return True if number % divisor == 0 else False


#using comparison operators
def divisible_by_2(number, divisor=2):
  return number % divisor == 0


print(divisible_by_2(333, 3))

#project2-1#####################################################

#Make a function that returns a list the word Even if the number is even
#and Odd if the number is odd using ternary operator.


def even_odd_list(nums_lst):
  return ['Even' if num % 2 == 0 else "Odd" for num in nums_lst]


nums_lst = [15, 99, 65, 34, 28, 71, 333]
print(even_odd_list(nums_lst))

#project3-1#####################################################

#Make a function that takes a number and returns prime word
#if the number is prime and not prime if the number is not prime.
#يكفي التحقق من نصف العدد ل prime number range(2,num/2)


def isprime(num):
  if num <= 1:
    return 'number is not prime'
  for i in range(2, num):
    if num % i == 0:
      return 'number is not prime'

  return 'number is prime'


print(isprime(10))
print(isprime(11))
print(isprime(12))
print(isprime(13))

#project4-1#####################################################

#Make a function that converts unit from kilometers
#to miles and vice versa and the default unit is
#kilometers and allows to convert from Celsius to
#Fahrenheit and vice versa.
#Celsius to Fahrenheit Formula: (°C * 1.8) + 32 = °F
#Fahrenheit to Celsius Formula: (°F - 32) / 1.8 = °C
#to convert kilometers to miles, simply multiply the number of kilometers by 0.62137
#1 kilometer is equal to 0.621371 miles (often shortened to . 62). 1 mile is equal to 1.609344 kilometers.


def convert_unit(num, unit="km"):
  if unit.lower() == "km":
    result = num * 0.621371
    return f'{num} km is {result:.2f} miles'
  elif unit.lower() == "miles":
    result = num / 0.621371
    return f'{num} miles is {result:.2f} km'
  elif unit.lower() == "celsius":
    result = (num * 1.8) + 32
    return f'{num} celsius is {result:.2f} Fahrenheit'
  elif unit.lower() == "fahrenheit":
    result = (num - 32) / 1.8
    return f'{num} fahrenheit is {result:.2f} Celsius'

  else:
    return "Invalid unit"


print(convert_unit(100))
# output: 100 km is 62.14 miles

print(convert_unit(100, "Miles"))
# output: 100 miles is 160.93 km

print(convert_unit(30, "Celsius"))
# output: 30 Celsius is 86.00 Fahrenheit

print(convert_unit(86, "Fahrenheit"))

# output: 86 Fahrenheit is 30.00 Celsius


#project1-2#####################################################
def special_sum(numbers, **kwargs):
  print(kwargs)  # this code is a hint to see what is inside kwargs

  if kwargs.get("only_even"):  #True
    return sum([number for number in numbers if number % 2 == 0])
  elif kwargs.get("only_odd"):  #True
    return sum([number for number in numbers if number % 2 != 0])
  elif kwargs.get("only_positive"):  #True
    return sum([number for number in numbers if number > 0])
  elif kwargs.get("only_negative"):  #True
    return sum([number for number in numbers if number < 0])
  elif kwargs.get("only_positive_even"):  #True
    return sum(
      [number for number in numbers if number % 2 == 0 and number > 0])
  elif kwargs.get("only_negative_even"):  #True
    return sum(
      [number for number in numbers if number % 2 == 0 and number < 0])
  elif kwargs.get("only_positive_odd"):  #True
    return sum(
      [number for number in numbers if number % 2 == 1 and number > 0])
  elif kwargs.get("only_negative_odd"):  #True
    return sum(
      [number for number in numbers if number % 2 == 1 and number < 0])

  return sum(numbers)
  # complete the rest of the code here


numbers = [
  1, -2, -3, 4, -5, -6, -7, 8, 9, -10, 11, 12, 13, 14, -15, -16, 17, 18, 19, 20
]

print(f"Sum of all numbers: {special_sum(numbers)}")

print(f"Total even numbers: {special_sum(numbers, only_even=True)}")
print(f"Total odd numbers: {special_sum(numbers, only_odd=True)}")

print(f"Total positive numbers: {special_sum(numbers, only_positive=True)}")
print(f"Total negative numbers: {special_sum(numbers, only_negative=True)}")

print(
  f"Total positive even numbers: {special_sum(numbers,only_positive_even=True)}"
)

print(
  f"Total positive odd numbers: {special_sum(numbers, only_positive_odd=True)}"
)

print(
  f"Total negative even numbers: {special_sum(numbers,only_negative_even=True)}"
)

print(
  f"Total negative odd numbers: {special_sum(numbers, only_negative_odd=True)}"
)

#project2-2#####################################################


def print_grades(name, **kwargs):
  print(f'\n{name.title()}\'s grades: ')
  print('------------------')
  for subject, grade in kwargs.items():
    print(f'{subject.title():10}: {grade}')


print_grades("Mohamed Hamed",
             math=90,
             english=80,
             arabic=100,
             physics=95,
             chemistry=85)

print_grades("Ahmed Khaled",
             math=80,
             english=70,
             arabic=90,
             physics=85,
             chemistry=75)

#project3-2#####################################################
import random
import string
# 1. The user can specify the length of the password and the default length is 8.
# 2. The password must contain at least one uppercase letter.
# 3. The password must contain at least one lowercase letter.
# 4. The password must contain at least one digit.
# 5. The password must contain at least one special character.
# 6. The user can also increase the complexity of the password by making #complex=True,this will make at least half of the password characters to be
#special characters


def generate_password(lenght=8, complex=False):

  selection = [
    string.punctuation, string.ascii_lowercase, string.digits,
    string.ascii_uppercase
  ]
  password = []
  i = 0
  if lenght < 8:
    print('Password lenght should not be less than 8 characters')
    lenght = 8
  while len(password) < lenght:
    if complex:
      password.extend(
        [random.choice(string.punctuation) for i in range(lenght // 2)])
      complex = False
    password.append(random.choice(selection[i]))
    if i == 3:
      i = -1
    i += 1

  random.shuffle(password)
  return ''.join(password)


print(generate_password(10))

#####حل مهندس محمد #################
import random
import string


def password(length=8, complex=False):
  # make sure the length is at least 8
  if length < 8:
    print("Password length must be at least 8 characters")
    length = 8

  # Define the character sets to use for the password
  lowercase_letters = string.ascii_lowercase
  uppercase_letters = string.ascii_uppercase
  digits = string.digits
  special_chars = string.punctuation

  # Create a list of all the characters we will use for the password
  all_chars_lst = [lowercase_letters, uppercase_letters, digits, special_chars]

  # Make sure we have at least one of each type of character
  password = [random.choice(chars) for chars in all_chars_lst]

  # make a string to combine all the characters we will use for the password
  all_chars = ''.join(all_chars_lst)

  # if complex is True, add special characters to the password
  if complex:
    # get at least half of the length of the password
    half_length = (length // 2) + (length % 2)
    # try to understand this line above by typing numbers manually and try to calculate the result

    # If complex is True, add special characters to the list
    password += [random.choice(special_chars) for _ in range(half_length)]

  # Fill the remaining characters with random choices from all_chars
  password += [random.choice(all_chars) for _ in range(length - len(password))]

  # Shuffle the password to make it more random
  random.shuffle(password)

  # Convert the password list to a string and return it
  return ''.join(password)


password_8 = password()
print(password_8)
