import csv


def read_csv_data(data_file):
  with open(data_file) as f:
    csv_data = csv.reader(f)
    data_lst = list(csv_data)
    return data_lst


def update_salary(employees_lst):
  for employee in employees_lst:
    employee[-1] = employee[-1].replace(',', '')
    employee[-1] = float(employee[-1]) * 2
  return employees_lst


def sorted_employees(updated_employees_data):
  sorted_employees_data = sorted(updated_employees_data, key=lambda employee: (employee[-1],employee[0]))
  return sorted_employees_data

def write_csv_data(new_data,file_name):
  with open(file_name,"w",newline="") as new_file:
    csv_writer=csv.writer(new_file)
    csv_writer.writerows(new_data)



employees_lst = read_csv_data("employees_data.csv")

updated_employees_data = update_salary(employees_lst)

sorted_employees_data = sorted_employees(updated_employees_data)



print(sorted_employees_data)
