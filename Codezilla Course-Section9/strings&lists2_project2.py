


full_name = input('Enter your full name: ').strip().title()
birthdate = input('Enter your birth date (dd-mm-yyyy): ').strip()
current_year = input('Enter the current year: ').strip()


first_name = full_name.split()[0]

birth_year = birthdate.split('-')[-1]
 
age = int(current_year) - int(birth_year) 


print(f'''{'-'*20}
Hello, {first_name}
Welcome at Age Calculator
{'-'*20}
Your age is: {age}''')
