
username = input('Enter your username: ').strip().lower()
password = input('Enter your password: ').strip().lower()

first_user = 'islam_hesham@codezilla.com'
first_pass = 'islam_hesham'

second_user = 'mohamed_gouda@codezilla.com'
second_pass = 'mohamed_gouda'
if (username == first_user and password == first_pass) or (username == second_user and password == second_pass):
  print('Access is allowed')

else:
  print('Access is denied')