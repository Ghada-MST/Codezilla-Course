
company_name = 'Codezilla'

name = input("Enter your name: ")

birthday = input('Enter your birhtdate: ')

email = input('Enter your email: ')

last_3_litters = name[-3:]

id = f'{company_name}-{last_3_litters}{birthday}'

index_of_at = email.index('@')

new_email = f'{email[:index_of_at]}@codezilla.com'


print (f'''{'-'*20} 
Your id is {id}
Your email is {new_email}''')