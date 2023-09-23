#Juniors 3 months bonus
#mid-levels 6 months bonus
#Seniors 9 months bonus


juniors = ['1111', '1113', '1115', '1117','1119', '1121']
mid_level = ['1311', '1313', '1315', '1317','1319', '1321', '1323', '1325']
seniors = ['1519', '1521', '1523', '1525']


employee_id = input('Enter employee id: ')
hourly_rate = float(input('Enter hourly rate: '))
worked_hours = float(input('Enter hours worked this month: '))

salary = worked_hours * hourly_rate 

print('-'*20)

# if employee_id not in [juniors, mid_level, seniors]:
#   print('Not an employee')
#   bonus = None
if employee_id in juniors:
  bonus = 3 * salary
elif employee_id in mid_level:
  bonus = 6 * salary
elif employee_id in seniors:
  bonus = 9 * salary
else:
  bonus = None
  print('Not an employee')
  
if bonus is not None:
  print(f'Employee id: {employee_id} gets a bonus of {bonus:,.2f} EGP')

