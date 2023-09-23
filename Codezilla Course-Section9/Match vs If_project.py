

cairo = ['Islam Mahfouz', 'Mohamed Mesilhy', 
'Hatem Elmaghraby', 'Kareem Embaby']
riyadh = ['Mohamed Gouda', 'Ayman Hamed', 
'Seif Ali', 'Adham Wael']
casablanca = ['Ahmed Ashraf', 'Abd El-Rahman Mahrous', 
'Islam Sheta', 'Mohamed Medhat', 'Mahmoud Nasser']
dubai= ['Ahmed Alaa', 'Kareem Abd-Elmeged', 
'Osama Ashraf', 'Mohamed Mostafa', 'Ahmed Bedeir']

office = input('Enter the name of the office: ').lower()

match office:
  case "cairo" | 'egypt' | 'eg':
    employees = cairo
  case 'riyadh' | 'saudi arabia' |'ksa':
    employees = riyadh
  case 'casablanca' | 'morocoo':
    employees = casablanca
  case 'dubai' | 'uae':
    employees = dubai
  case _:
    employees = 0
    print('Office not found')
    
if employees:
  employee_str = ', '.join(employees[:-1]) + ' and '+ employees[-1]
  
  print(f'''The employees in {office.upper()} are {employee_str}.''')