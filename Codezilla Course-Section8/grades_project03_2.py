
first_num = float(input('Enter the first number: '))
second_num = float(input('Enter the second number: '))

operator = input('Enter the operator from * + - / ** : ')

  
if operator == '*':
  result = first_num * second_num
  operation = 'Multipication'
elif operator == '+':
  result = first_num + second_num
  operation = "Addition"
elif operator == '/':
  result = first_num / second_num
  operation = 'Division'
elif operator == '-':
  result = first_num - second_num 
  operation = 'Subtraction'
elif operator == '**':
  result = first_num **second_num
  operation = 'Exponential'
else:
  operation = None
  print("Sorry, please enter valid inputs")
        
if operation != None:  
  print(f'{operation} result is {result:,.1f}')