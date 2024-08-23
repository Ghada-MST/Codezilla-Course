
name = input('Enter your name: ').strip().title().split()
print(name)
company_name = input('Enter your company name: ').strip().lower()


birth_year = input('Enter your birth year: ').strip()

email = input('Enter your email: ').strip()


first_3_ltr_company = company_name[:3]

last_2_ltr_name = name[-1][-2:]

id = first_3_ltr_company+'-'+last_2_ltr_name+birth_year

email_at_idx = email.index('@')

new_email = email[:email_at_idx] + f'@{company_name}.com'



first_name = name[0]

print(f'''{'-'* 20}
Hello, {first_name}!
Welcome at {company_name.title()}
{'-'* 20}
Your id is: {id}
Your email is: {new_email}''')



#unpacking

num1,num2,num3 = input('Enter your fav nums: ').split()
print(num1,num2,num3)