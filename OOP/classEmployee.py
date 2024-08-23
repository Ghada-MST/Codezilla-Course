import csv


class Employee:
  COMPANY = "Codezilla"
  PHONE_PREFIX = "+20"
  PHONE_LENGHT = 12

  def __init__(self,
               name,
               age,
               job,
               id,
               phone,
               bank_account,
               hours_worked=160,
               hour_rate=30,
               from_file=False):
    self.name = name
    self.age = age
    self.job = job
    self.__hours_worked = hours_worked
    self.__hour_rate = hour_rate
    self.__id = id
    self.__phone = phone
    self.__bank_account = bank_account
    if not from_file:
      AllEmployees.add_employee(self)

  def __str__(self):
    return f"{self.name} is {self.age} years old and works as {self.job}"

  def __repr__(self):
    return f"Employee: name = {self.name}, age = {self.age}, job = {self.job}"

  def get_phone(self):
    return self.__phone

  def set_phone(self, new_phone, id):
    if self.__id == id and Employee.is_valid_phone(new_phone):
      self.__phone = new_phone
    else:
      print(
        'you are not allowed to change the phone number or invalid phone number format'
      )

  def calculate_gross_salary(self):
    gross_salary = self.__hours_worked * self.__hour_rate
    return gross_salary

  def calculate_net_salary(self):
    gross_salary = self.calculate_gross_salary()
    net_salary = Finance.calculate_net_salary(gross_salary)
    return net_salary

  @property
  def hours_worked(self):
    return self.__hours_worked

  @hours_worked.setter
  def hours_worked(self, new_hours_worked):
    if isinstance(new_hours_worked, int) and new_hours_worked > 0:
      self.__hours_worked = new_hours_worked
    else:
      raise ValueError("Hours worked should be positive string value")

  @property
  def hour_rate(self):
    return self.__hour_rate

  @hour_rate.setter
  def hour_rate(self, new_hour_rate):
    if isinstance(new_hour_rate, int) and new_hour_rate > 0:
      self.__hour_rate = new_hour_rate
    else:
      raise ValueError("Hourly rate should be positive string value")

  @property
  def id(self):
    return self.__id

  @id.setter
  def id(self, value):
    if isinstance(value, str) and value.isdigit() and value.strip():
      self.__id = value
    else:
      raise ValueError("ID should be non-empty string composed only of digits")

  @staticmethod
  def is_valid_phone(phone):
    return phone.startswith(
      Employee.PHONE_PREFIX) and len(phone) == Employee.PHONE_LENGHT

  def __add__(self, other):
    return int(self.age) + int(other.age)

  def __gt__(self, other):
    return self.calculate_net_salary() > other.calculate_net_salary()

  def __len__(self):
    return len(self.name.replace(" ", ""))

  def __eq__(self, other):
    return self.__hours_worked == other.__hours_worked


class AllEmployees:
  __employees = []

  @classmethod
  def show_employees(cls):
    return cls.__employees

  @classmethod
  def add_employee(cls, employee):
    cls.__employees.append(employee)

  @classmethod
  def get_employee_by_id(cls, id):
    for emp in cls.__employees:
      if emp.id == id:
        return emp
    return None

  @classmethod
  def remove_employee_by_id(cls, id):
    cls.__employees = [emp for emp in cls.__employees if emp.id != id]


class Manager(Employee):
  MANAGER_BONUS = 500

  def __init__(self, *args, authority=1, **kwargs):
    super().__init__(*args, **kwargs)
    self.authority = authority

  def __str__(self):
    base_info = super().__str__()
    return base_info + f" He has authority level of {self.authority}"

  def promote_employee(self, id, raise_amount):
    employee = AllEmployees.get_employee_by_id(id)
    if employee:
      employee.hour_rate += raise_amount
      print(
        f"{employee.name} hourly rate has increased to {employee.hour_rate}")
    else:
      print(f"ُEmployee with id {id} not found")

  def demote_employee(self, id, reduce_amount):
    if self.authority >= 2:
      employee = AllEmployees.get_employee_by_id(id)
      if employee:
        employee.hour_rate = max(employee.hour_rate - reduce_amount, 3)
        print(
          f"{employee.name} hourly rate has been reduced to {employee.hour_rate}"
        )
      else:
        print(f"ُEmployee with id {id} not found")
    else:
      print("You don't have the authority to demote employees")

  def fire_employee(self, id):
    if self.authority >= 3:
      employee = AllEmployees.get_employee_by_id(id)
      if employee:
        AllEmployees.remove_employee_by_id(id)
        print(f"{employee.name} has been fired")
      else:
        print(f"ُEmployee with id {id} not found")
    else:
      print("You don't have the authority to fire employees")

  def calculate_gross_salary(self):
    base_gross_salary = super().calculate_gross_salary()
    return base_gross_salary + Manager.MANAGER_BONUS


class EmployeeFileHandler:

  @staticmethod
  def read_csv_data(file_name):
    employees = []
    with open(file_name, "r") as file:
      csv_reader = csv.DictReader(file)
      for row in csv_reader:
        name = row["name"]
        age = row["age"]
        job = row["job_title"]
        id = row["id"]
        phone = row["phone"]
        bank_account = row["bank_account"]
        hours_worked = int(row["hours_worked"])
        hour_rate = int(row["hour_rate"])
        employee = Employee(name,
                            age,
                            job,
                            id,
                            phone,
                            bank_account,
                            hours_worked,
                            hour_rate,
                            from_file=True)
        employees.append(employee)
    return employees

  @staticmethod
  def read_and_add_file_to_AllEmployees(file_name):
    employees = EmployeeFileHandler.read_csv_data(file_name)
    for emp in employees:
      AllEmployees.add_employee(emp)


class Finance:
  HEALTH_INSURANCE_COST = 100
  RETIREMENT_CONTRIBUTION_RATE = 0.05
  TAX_THRESHOLD = 5000
  TAX_LOW = 0.1
  TAX_HIGH = 0.3

  @staticmethod
  def calculate_net_salary(gross_salary):
    tax = Finance.calculate_tax(gross_salary)
    retirement_contribution = Finance.RETIREMENT_CONTRIBUTION_RATE * gross_salary
    deduction = tax + retirement_contribution + Finance.HEALTH_INSURANCE_COST
    net_salary = gross_salary - deduction
    return net_salary

  @staticmethod
  def calculate_tax(salary):
    if salary < Finance.TAX_THRESHOLD:
      return salary * Finance.TAX_LOW
    else:
      return salary * Finance.TAX_HIGH


emp1 = Employee("hany", "30", "developer", "1234", "+20122345678", "9fg6d")
emp2 = Employee("zein", "30", "IT", "6574", "+2012222278", "ki746d")

manager = Manager("one",
                  "50",
                  "manager",
                  "0987",
                  "+201036278487",
                  "hfyd765",
                  authority=3)

print(AllEmployees.show_employees())

manager.fire_employee("1234")

print(AllEmployees.show_employees())

print(manager)
