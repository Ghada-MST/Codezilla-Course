#project1##########################


def filter_strings(string_lst, char):
  return [string for string in string_lst if char in string]


strings = ['apple', 'banana', 'pear', 'orange']
filtered_strings = filter_strings(strings, 'g')
print(filtered_strings)
# output: ["orange"]

#project2##########################
#Make a function that takes a list of numbers and
#returns a list of numbers without duplicates.


def remove_duplicates(numbers_lst):
  unique_numbers = []
  for num in numbers_lst:
    if num not in unique_numbers:
      unique_numbers.append(num)

  return unique_numbers


#another answer
def remove_duplicates(numbers_lst):
  unique_numbers = set(numbers_lst)
  return list(unique_numbers)


#another answer
def remove_duplicates(number_lst):
  unique_numbers = {}
  for num in number_lst:
    unique_numbers.setdefault(num)
  return list(unique_numbers)


numbers = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)

# output: [1, 2, 3, 4, 5]

#project3##########################
import copy


#Make a program that takes the dictionary of
#employees and give a raise to employees who meet
#the given criteria and returns a new list of updated
#employees like this:
def give_raise(employees, criteria, bonus):
  new_employees = copy.deepcopy(employees)
  for employee in new_employees:
    if employee['department'] == criteria:
      employee['new_salary'] = employee['salary'] + bonus

  return new_employees


def print_employees(employees, new_employees, criteria):
  for employee in new_employees:
    if 'new_salary' in employee:
      print(
        f"{employee['name']} salary was {employee['salary']}$ and is now {employee['new_salary']}$"
      )


#another answer


def give_raise(employees, criteria, bonus):
  new_employees = copy.deepcopy(employees)
  for employee in new_employees:
    if employee['department'] == criteria:
      employee['salary'] += bonus
  return new_employees


def print_employees(employees, new_employees, criteria):
  for employee in employees:
    if employee['department'] == criteria:
      employee_name = employee['name']
      salary = employee['salary']
      raised_salary = [employee['salary'] for employee in new_employees if employee_name == employee['name']][0]
      print(f'{employee_name} salary was {salary} and is now {raised_salary}')


# Original list of employees
employees = [{
  'name': 'Mohamed Ali',
  'age': 25,
  'salary': 45_000,
  'department': 'Sales'
}, {
  'name': 'Islam Ahmed',
  'age': 30,
  'salary': 60_000,
  'department': 'Marketing'
}, {
  'name': 'Osama Ashraf',
  'age': 35,
  'salary': 38_000,
  'department': 'Sales'
}, {
  'name': 'Seif Ali',
  'age': 40,
  'salary': 77_000,
  'department': 'Engineering'
}, {
  'name': 'Ayman Hamed',
  'age': 45,
  'salary': 80_000,
  'department': 'Sales'
}, {
  'name': 'Ahmed Ali',
  'age': 33,
  'salary': 76_000,
  'department': 'Marketing'
}]
# Give a raise of $10,000 to employees who meet the criteria of
#being in the Sales department
new_employees = give_raise(employees, 'Sales', 10_000)

# Print the new and old information of employees
print_employees(employees, new_employees, 'Sales')

# Output:
#Mohamed Ali salary was 45,000.00$ and is now 55,000.00$
#Osama Ashraf salary was 38,000.00$ and is now 48,000.00$
#Ayman Hamed salary was 80,000.00$ and is now 90,000.00$
