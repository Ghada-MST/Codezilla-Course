#employee name
employee_name = input("enter employee name: ").strip().title()
#currency
currency = input("currency: ").strip().title()
#enter employee hours
employee_hours = float(input("enter the number of employee hours per month : "))
#enter employee rate 
rate = float(input("enter Hourly rate: "))
#calculate salary
total_salary = employee_hours * rate 
base_hours = 100
basic_salary = base_hours * rate
over_time = (employee_hours - base_hours) * rate*2
print("-"*30)
if employee_hours > base_hours :
  print(f'{employee_name} has worked {employee_hours} hours this month, the total salary is {basic_salary + over_time:,.2f}{currency}')
else:
  print(f"{employee_name} has worked {employee_hours} hours this month, the total salary is {total_salary:,.2f}{currency}")


#حل بطريقة المهندس اسلام#

total_hours = float(input('enter your hours per month: '))
rate = float(input('enter your hourly rate: '))

#calculate basic hours
base_hours = 100
over_time = total_hours - base_hours
bonus = 2

if total_hours > base_hours:
  salary = (base_hours * rate) + (over_time * rate * bonus)
  
else:
  salary = total_hours * rate

print(f"{'-'*20} \nYou have worked {total_hours} hours this month, your salary is {salary:,.2f}$")