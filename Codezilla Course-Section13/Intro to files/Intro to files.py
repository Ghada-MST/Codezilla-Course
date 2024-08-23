with open("Codezilla Course-Section13/Intro to files/employees_data.txt") as f:
  employees_data = f.readlines()

print(employees_data)

with open("Codezilla Course-Section13/employee_new_data", 'w') as f:
  for employee in employees_data:
    emp = employee.strip().split('-')
    salary = float(emp[-1]) * 2
    f.write(f'{emp[0]}-{emp[1]}-{emp[2]}-{salary}\n')
