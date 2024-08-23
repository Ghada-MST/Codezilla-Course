#project1##########################################
pizzas = {
  "Margherita": 120,
  "Pepperoni": 200,
  "Hawaiian": 150,
  "Meat Lovers": 250,
  "Mushroom": 140,
}


# Margherita Pizza: 120 EGP
# Pepperoni pizza: 200 EGP
def pizza_price():
  for pizza, price in pizzas.items():
    print(f'{pizza} pizza: {price}EGP')


pizza_price()

#project2##########################################


def print_employee_info(name, age, salary, section=''):
  print(f"Name: {name.title()}")
  print(f"Age: {age}")
  print(f"Salary: {salary}")
  print(f"section: {section}")


# 1.
print_employee_info("Mohamed ahmed", 25, 10_000)

#2.
print_employee_info("hassan Ali", 33, 15_000)

#3.
print_employee_info(salary=20_000, age=30, name="Ali Hassan")

#4.
print_employee_info("Ahmed Mohamed", 35, salary=15_000)

#5.
print_employee_info("Hazem Khaled", age='unknown', salary=15_000)

#6.
print_employee_info("Hamed Ali", 25, 14_000)

#7.
print_employee_info("Mohamed khedr", salary=13_000, age=25, section="IT")

#project3##########################################


def print_students_info(name, age, city="Cairo", school="Codezilla"):
  print(f"Name: {name.title()}")
  print(f"Age: {age}")
  print(f"City: {city.title()}")
  print(f"School: {school.title()}")


# Print the following Information for each Student:

# name: "Ahmed Mohamed",
# age: 25,
# city: "Cairo",
# School: "Codezilla"
print_students_info("Ahmed Mohamed", 25)

# name: "Mohamed Ahmed",
# age: 33,
# city: "Cairo",
# School: "Al-Azhar"
print_students_info("Mohamed Ahmed", 33, school="Al-Azhar")

# name: "Ali Hassan",
# age: 30,
# city: "Alexandria",
# School: "Codezilla"
print_students_info("Ali Hassan", 30, city="Alexandria")

# name: "Hazem Khaled",
# age: 35,
# city: "New York",
# School: "Khaled ibn al-Walid"
print_students_info("Hazem Khaled", 35, "New York", "Khaled ibn al-Walid")
# name: "Hamed Ali",
# age: 25,
# city: "Tanta",
# School: "Al Durra"
print_students_info("Hamed Ali", school="Al Durra", city="Tanta", age=25)

#project4##########################################

name = "hamada codezilla"

grades = {
  'Math': 99,
  'English': 98,
  'Science': 99,
  'Arabic': 100,
  'History': 99
}


def student_info(student_name, grades, school='Codezilla'):
  print(f'''Student: {student_name.title()}
School:{school.title()}
Grades:
-----------''')
  for subject, grade in grades.items():
    print(f'{subject.title()}: {grade}')


student_info(name, grades)
