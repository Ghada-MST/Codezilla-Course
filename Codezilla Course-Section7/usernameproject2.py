#get name, year,month, day of birth form the user
name = input("enter your name: ").strip().title()
year = int(input('enter your birth year: '))
month = input('enter your birth month: ')
day = input('enter your birth day: ')
#add year to the name lenght 
add_year_to_name_len = len(name) + year
#build username name + day +month+ added year to name lenght
#In name replace spaces with underscores and convert letters to lower case
user_name = f"{name.replace(' ','_').lower()}_{day}_{month}_{add_year_to_name_len}"
print("-"*30)
#greet user
print(f"Hello, {name}")
#print user name
print(f'Your username is....\n{user_name}@codezilla.com')