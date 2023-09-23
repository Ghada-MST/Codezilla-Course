
#project1############################################################################
students = {
"Mohamed": {"grades": [100, 90, 80], "age": 20},
"Ahmed": {"grades": [100, 95, 93], "age": 21},
"Ali": {"grades": [85, 83, 87], "age": 19},
"Sara": {"grades": [100, 94, 98], "age": 21}
}


print(*students['Mohamed']['grades'], sep='-')

print(students['Ali']["age"])

print(students["Sara"]["age"])

sara_grades = students["Sara"]["grades"]
print(*sara_grades,sep='\n')

print()
print()
#project2############################################################################

students2 = {
"Mohamed": {"grades": {
"math": 100,
"english": 90,
"science": 80,
"arabic": 100, 
"history": 97},
"school": "Codezilla"
},
"Ahmed": {"grades": {
"math": 100,
"english": 95,
"science": 93,
"arabic": 100,
"history": 94},
"school": "Codezilla"
},
"Ali": {"grades": {
"math": 85,
"english": 83,
"science": 87,
"arabic": 100,
"history": 90},
"school": "Al-Azhar"
},
"Sara": {"grades": {
"math": 100,
"english": 94,
"science": 98,
"arabic": 100,
"history": 100},
"school": "Al-Azhar"
}
}


#Mohamed grades in math and English
print(f'Mohamed\'s grade in math is: {students2["Mohamed"]["grades"]["math"]}')
print(f'Mohamed\'s grade in english is: {students2["Mohamed"]["grades"]["english"]}')

#Mohamed School
print(f'Mohamed\'s school is: {students2["Mohamed"]["school"]}')
print('*'*30)

#Ahmed grades in math, science, and Arabic
print(f'Ahmed\'s grade in math is: {students2["Ahmed"]["grades"]["math"]}')
print(f'Ahmed\'s grade in science is: {students2["Ahmed"]["grades"]["science"]}')
print(f'Ahmed\'s grade in Arabic is: {students2["Ahmed"]["grades"]["arabic"]}')
print('*'*30)

#Ali school and grades in history, science, and Arabic
print(f'Ali\'s school is: {students2["Ali"]["school"]}')
print(f'Ali\'s grade in history is: {students2["Ali"]["grades"]["history"]}')
print(f'Ali\'s grade in science is: {students2["Ali"]["grades"]["science"]}')
print(f'Ali\'s grade in Arabic is: {students2["Ali"]["grades"]["arabic"]}') 
print('*'*30)

#Sara grades in math, science, and history
print(f'Sara\'s grade in math is: {students2["Sara"]["grades"]["math"]}')
print(f'Sara\'s grade in science is: {students2["Sara"]["grades"]["science"]}')
print(f'Sara\'s grade in history is: {students2["Sara"]["grades"]["history"]}')
print()
print()
#project3############################################################################

restaurant_menu = {
"Burgers": {"Beef": 100, "Chicken": 80, "Bacon": 120},
"Pizzas": {"Cheese": 100, "Pepperoni": 120, "Veggie": 100},
"Drinks": {"Coke": 20, "Fanta": 20, "Sprite": 20},
"Desserts": {"Ice Cream": 50, "Chocolate Cake": 60,
 "Cheese Cake": 70},
"Sides": {"Fries": 30, "Onion Rings": 40, "Potato Wedges": 
50}
}

# chicken burger price
print(f"the chicken burger price is : {restaurant_menu['Burgers']['Chicken']}")
# veggie pizza price
print(f"the veggie pizza price is : {restaurant_menu['Pizzas']['Veggie']}")
# coke price
print(f"the coke price is : {restaurant_menu['Drinks']['Coke']}")
# chocolate cake price
print(f"the chocolate cake price is : {restaurant_menu['Desserts']['Chocolate Cake']}")
# Onion Rings price
print(f"the Onion Rings price is : {restaurant_menu['Sides']['Onion Rings']}")

print()
print()

#project4############################################################################
employees = {
"Mohamed Hassan": {"age": 35, "salary": 20_000, 
"department": "IT"},
"Ahmed Khaled": {"age": 24, "salary": 10_000, "department": 
"IT"},
"Ali Hamed": {"age": 30, "salary": 15_000, "department": 
"HR"},
"Mahmoud Samir": {"age": 28, "salary": 12_000, 
"department": "HR"},
"Ahmed Hassan": {"age": 25, "salary": 10_000, "department": 
"IT"}
}

# Mohamed Hassan age
print(f'Mohamed Hassan age is: {employees["Mohamed Hassan"]["age"]}')
print('*'*30)

# Ali Hamed department
print(f'Ali Hamed department is: {employees["Ali Hamed"]["department"]}')
print('*'*30)

# Ahmed Khaled salary
print(f'Ahmed Khaled salary is: {employees["Ahmed Khaled"]["salary"]:,}')
print('*'*30)

# All the information about Mahmoud Samir and Ahmed Hassan in the 
# following format:
# Mahmoud Samir is 28 years old, he works in HR department and
# his salary is 12,000
print(f'Mahmoud Samir is {employees["Mahmoud Samir"]["age"]} years old, he works in {employees["Mahmoud Samir"]["department"]} department and his salary is {employees["Mahmoud Samir"]["salary"]:,}$')
print('*'*30)


print(f'Ahmed Hassan is {employees["Ahmed Hassan"]["age"]} years old, he works in {employees["Ahmed Hassan"]["department"]} department and his salary is {employees["Ahmed Hassan"]["salary"]:,}$')
print()
print()


#project5############################################################################
ali_grades = students2['Ali']['grades']

math_grades = ali_grades['math']
science_grades = ali_grades['science']
english_grades = ali_grades['english']
arabic_grades = ali_grades['arabic']
history_grades = ali_grades['history']

total_ali_grades = [math_grades,science_grades,english_grades,arabic_grades,history_grades]

percentage = sum(total_ali_grades)/len(total_ali_grades)

print(f'The total percentage of Ali score is {percentage:.0f} %')