#project1###############################
def average(*num_lst):
  print(num_lst)
  # try:
  #   if type(num_lst[0]) in (list,tuple,set):
  #     num_lst = num_lst[0]
  #     return sum(num_lst)/len(num_lst)

  #   elif not type(num_lst) is int:
  #     return 'Please Enter Numbers to Calculate Average'

  #   return (sum(num_lst)/len(num_lst))
  # except TypeError:
  #   return "Cannot Enter a String"
  # except ZeroDivisionError:
  #    return "Please Enter Numbers to Calculate Average"
  try:
    if [True for x in num_lst if isinstance(x, str)]:
      return 'Cannot Enter a String'
    elif len(num_lst) > 1:
      return sum(num_lst) / len(num_lst)
    return sum(*num_lst) / len(*num_lst)
  except ZeroDivisionError:
    return "Please Enter Numbers to Calculate Average"
  except TypeError:
    return "Please Enter Numbers to Calculate Average"


print(average(1, 2, 3, 4, 5))
print(average([1, 2, 3, 4, 5]))
print(average((1, 2, 3, 4, 5)))
print(average({1, 2, 3, 4, 5}))

#this code will raise the following error messages
print(average([]))  # Please Enter Numbers to Calculate Average
print(average())  # Please Enter Numbers to Calculate Average
print(average("Hello"))  # Cannot Enter a String
print(average(1, 2, 3, 4, "5"))  # Cannot Enter a String

#another answer حل مهندس محمد
# 1. Make average function that takes a list of numbers and returns the average of the numbers
# and it deals with the following cases and raises the following exceptions:

# # this code works fine
# print(average(1, 2, 3, 4, 5))
# print(average([1, 2, 3, 4, 5]))
# print(average((1, 2, 3, 4, 5)))
# print(average({1, 2, 3, 4, 5}))

# # this code will raise the following error messages
# print(average([])) # Please Enter Numbers to Calculate Average
# print(average("Hello")) # Cannot Enter a String
# print(average(1, 2, 3, 4, "Hello")) # Cannot Enter a String
# print(average())# Please Enter Numbers to Calculate Average

### answer 1 ###


def average(*args):
  # Check if a single argument is a list, tuple, or set, and if so, flatten it
  if len(args) == 1 and isinstance(args[0], (list, tuple, set)):
    args = args[0]

  # # Another Solution
  # if len(args) == 1 and type(args[0]) in (list, tuple, set):
  #     args = args[0]

  # Check if the argument is empty
  if not args:
    raise Exception("Please Enter Numbers to Calculate Average")

  try:
    # Calculate the average of the arguments
    return sum(args) / len(args)

  # If an argument is a string, raise TypeError
  except TypeError:
    raise TypeError("Cannot Enter a String")


#project2###############################
import copy

employees = [
  {
    'name': 'Mohamed Ali',
    'age': 25,
    'salary': 45_000,
    'department': 'Sales'
  },
  {
    'name': 'Islam Ahmed',
    'age': 30,
    'salary': 60_000,
    'department': 'Marketing'
  },
  {
    'name': 'Osama Ashraf',
    'age': 35,
    'salary': 38_000,
    'department': 'Sales'
  },
  {
    'name': 'Seif Ali',
    'age': 40,
    'salary': 77_000,
    'department': 'Engineering'
  },
  {
    'name': 'Ayman Hamed',
    'age': 45,
    'salary': 80_000,
    'department': 'Sales'
  },
  {
    'name': 'Ahmed Alaa',
    'age': 33,
    'salary': 76_000,
    'department': 'Marketing'
  },
]


def give_raise(employees, criteria='Sales', bonus=10_000):
  try:
    if len(employees) == 0:
      return 'No employees in the list'
    new_employees = copy.deepcopy(employees)
    found = False
    for employee in new_employees:
      if employee['department'] == criteria:
        found = True
        employee['salary'] += bonus

    if not found:
      raise NameError()
    return new_employees
  except TypeError:
    print('Only integers are allowed')
  except NameError:
    print('Department not found')


def print_employees(employees, new_employees, criteria):
  for employee in employees:
    if employee['department'] == criteria:
      employee_name = employee['name']
      salary = employee['salary']
      raised_salary = [
        employee['salary'] for employee in new_employees
        if employee_name == employee['name']
      ][0]
      print(f'{employee_name} salary was {salary} and is now {raised_salary}')


# Give a raise of $10,000 to employees who meet the criteria of
#being in the Sales department
new_employees = give_raise(employees, 'Sales', 10_000)
# Print the new and old information of employees who meet the criteria
print_employees(employees, new_employees, 'Sales')

#another answer حل مهندس محمد

# 2. Make a program that takes the dictionary of employees and give a raise to employees who meet the given criteria
#  and returns a new list of updated employees, using clean code.
# like this:

import copy


def main():
  # Original list of employees
  employees = [
    {
      'name': 'Mohamed Ali',
      'age': 25,
      'salary': 45_000,
      'department': 'Sales'
    },
    {
      'name': 'Islam Ahmed',
      'age': 30,
      'salary': 60_000,
      'department': 'Marketing'
    },
    {
      'name': 'Osama Ashraf',
      'age': 35,
      'salary': 38_000,
      'department': 'Sales'
    },
    {
      'name': 'Seif Ali',
      'age': 40,
      'salary': 77_000,
      'department': 'Engineering'
    },
    {
      'name': 'Ayman Hamed',
      'age': 45,
      'salary': 80_000,
      'department': 'Sales'
    },
    {
      'name': 'Ahmed Alaa',
      'age': 33,
      'salary': 76_000,
      'department': 'Marketing'
    },
  ]

  criteria = "Sales"

  # Give a raise of $10,000 to employees who meet the criteria
  new_employees = give_raise(employees, criteria, 10_000)

  # Print the new and old information of employees who meet the criteria
  print_employees(employees, new_employees, criteria)


def give_raise(employees, criteria, amount):
  """
    Gives a raise to employees who meet the given criteria and 
    returns a new list of updated employees.

    :param employees: A list of employees, where each employee is 
    a dictionary containing their name, age, salary, and department.

    :param criteria: A function that takes an employee dictionary 
    and returns True if the employee should receive a raise.

    :param amount: The amount of the raise to give to each qualifying 
    employee.

    :return: A new list of employees with the raise applied to 
    qualifying employees, without modifying the original list.
    """
  # Make a deep copy of the original list of employees
  new_employees = copy.deepcopy(employees)

  try:
    # Give a raise to qualifying employees
    for employee in new_employees:
      if employee['department'] == criteria:
        employee['salary'] += amount

    # Return the new list of employees with the raise applied
    return new_employees

  except TypeError:
    print("Error: employees must be a list of dictionaries, \
criteria must be a function, and amount must be a number.")

  except Exception as error_message:
    print(f"An error occurred while giving a raise to employees \
who meet the criteria: {error_message}.")


def print_employees(employees, new_employees, criteria):
  """
    Prints the updated information of employees who meet the given criteria.

    :param employees: A list of employees, where each employee is 
    a dictionary containing their name, age, salary, and department.

    :param new_employees: A new list of employees with the raise applied to 
    qualifying employees, without modifying the original list.

    :param criteria: A function that takes an employee dictionary and 
    returns True if the employee should receive a raise.
    """
  try:
    for employee, new_employee in zip(employees, new_employees):
      if employee['department'] == criteria:
        print(f"{employee['name']} salary was {employee['salary']:,.2f}$ \
and is now {new_employee['salary']:,.2f}$")

  except Exception as error_message:
    print(f"An error occurred while printing the updated \
information of employees who meet the criteria: {error_message}.")


if __name__ == "__main__":
  main()

# Output:
# Mohamed Ali salary was 45,000.00$ and is now 55,000.00$
# Osama Ashraf salary was 38,000.00$ and is now 48,000.00$
# Ayman Hamed salary was 80,000.00$ and is now 90,000.00$

#project3###############################
import random
import time
import os
# dictionary with the words and definitions
WORDS = {
  "Absence": "The lack or unavailability of something or someone.",
  "Approval": "Having a positive opinion of something or someone.",
  "Answer": "The response or receipt to a phone call, question, or letter.",
  "Attention": "Noticing or recognizing something of interest.",
  "Amount": "A mass or a collection of something",
  "Borrow":
  "To take something with the intention of returning it after a period of time.",
  "Baffle": "An event or thing that is a mystery and confuses.",
  "Ban": "An act prohibited by social pressure or law.",
  "Banish": "Expel from the situation, often done officially.",
  "Banter": "Conversation that is teasing and playful.",
  "Characteristic":
  "referring to features that are typical to the person, place, or thing.",
  "Cars": "Four-wheeled vehicles used for traveling.",
  "Care": "extra responsibility and attention.",
  "Chip": "a small and thin piece of a larger item.",
  "Cease": "to eventually stop existing.",
  "Dialogue": "A conversation between two or more people.",
  "Decisive": "a person who can make decisions promptly.",
}


def main():
  message = """\n1. Review random word
2. Test yourself
3. Exit"""
  while True:
    print(message)
    choice = input('\nEnter your choice: ')
    if choice == '1':
      review_random_word()
    elif choice == '2':
      test_yourself()
    elif choice == '3':
      break
    else:
      print('\nInvalid option')
      continue


def review_random_word():
  rand_word = random.choice(list(WORDS))
  rand_def = WORDS[rand_word]

  print(f"""\nWord: {rand_word}
Definition: {rand_def}
---------------------------------""")


def test_yourself():
  rand_word = random.choice(list(WORDS))
  rand_def = WORDS[rand_word]

  print(rand_def)
  time.sleep(5)
  os.system("clear")

  attempt = 3
  for _ in range(attempt + 1):
    user_word = input('Enter the word: ').title()

    if user_word == rand_word:
      print('Great job!!')
      break
    elif user_word != rand_word:
      if attempt == 1:
        print(f'Incorrect answer, you have {attempt-1} attempts remaining')
        print('------------------')
        print(f'The correct answer is {rand_word}')
        print('Better luck next time.')
        break
      attempt -= 1
      x = "s" if attempt == 2 else ""
      print(f'Incorrect answer, you have {attempt} attempt{x} remaining')


if __name__ == '__main__':

  main()

#another answer حل مهندس محمد

import random
import time
import os

# dictionary with the words and definitions
WORDS = {
  "Absence": "The lack or unavailability of something or someone.",
  "Approval": "Having a positive opinion of something or someone.",
  "Answer": "The response or receipt to a phone call, question, or letter.",
  "Attention": "Noticing or recognizing something of interest.",
  "Amount": "A mass or a collection of something",
  "Borrow":
  "To take something with the intention of returning it after a period of time.",
  "Baffle": "An event or thing that is a mystery and confuses.",
  "Ban": "An act prohibited by social pressure or law.",
  "Banish": "Expel from the situation, often done officially.",
  "Banter": "Conversation that is teasing and playful.",
  "Characteristic":
  "referring to features that are typical to the person, place, or thing.",
  "Cars": "Four-wheeled vehicles used for traveling.",
  "Care": "extra responsibility and attention.",
  "Chip": "a small and thin piece of a larger item.",
  "Cease": "to eventually stop existing.",
  "Dialogue": "A conversation between two or more people.",
  "Decisive": "a person who can make decisions promptly.",
}


def main():
  """Main function that runs the program."""
  while True:
    # print the options
    display_options()

    # get the user choice
    choice = input("Enter your choice: ")

    # if the user chooses to review a random word
    if choice == "1":
      review_word()

    # if the user chooses to test themselves
    elif choice == "2":
      test_yourself()

    # if the user chooses to exit
    elif choice == "3":
      break

  # if the user chooses an invalid option
    else:
      print("Invalid option")

  # print message to the user
  print("Have a nice day!")


def display_options():
  """Display the available options for the user."""

  options = """1. Review Random Word
2. Test Yourself
3. Exit"""
  print(options)


def review_word():
  """Display a random word and its definition."""
  # get a random word from the dictionary
  word = random.choice(list(WORDS.keys()))

  # print the word and the definition
  print(f"Word: {word}")
  print(f"Definition: {WORDS[word]}")
  print("-" * 20)


def test_yourself():
  """Display a random word and allow the user to test themselves on its definition."""
  # get a random word from the dictionary
  word = random.choice(list(WORDS.keys()))

  # print the definition
  print(f"Definition: {WORDS[word]}")

  # allow the user to see the definition for 5 seconds
  time.sleep(5)

  # clear the screen
  os.system("cls")

  # allow the user to have 3 attempts to answer the question
  for i in range(3):
    # get the user answer
    answer = input("Enter the word: ")

    # if the user answer is correct
    if answer.lower() == word.lower():
      print("Correct answer")
      break

    # if the user answer is wrong
    else:
      # number of remaining attempts
      remaining_attempts = 2 - i

      # string to display the number of attempts
      attempts_str = "attempt" if remaining_attempts == 1 else "attempts"
      print(
        f"Incorrect answer, you have {remaining_attempts} {attempts_str} remaining."
      )

      # if the user failed to answer the question after 3 attempts show the correct answer
      if remaining_attempts == 0:
        print("-" * 20)
        print(f"The correct answer is {word}.")
        print("Better luck next time.")
      continue


if __name__ == '__main__':
  main()
