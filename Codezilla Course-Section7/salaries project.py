#employee name
employee_name = input("enter employee name: ").strip().title()
#currency
currency = input("currency: ").strip().title()
#enter employee hours
employee_hours = float(input("enter hours of employee : "))
#enter employee rate 
rate = float(input("enter Hourly rate: "))
#calculate salary
total_salary = employee_hours * rate
print("-"*30)
print(f"{employee_name}'s salary is {total_salary:,} {currency}")