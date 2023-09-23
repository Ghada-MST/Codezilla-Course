
first_num,operator,second_num = input('Enter the operation: ').split()

#operators = '*','/','+','-','**'

first_num = float(first_num)
second_num = float(second_num)


if operator == "*":
  result = first_num * second_num
  operation = 'Multiplication'
elif operator == "+":
  result = first_num + second_num
  operation = 'Addition'
elif operator == "-":
  result = first_num - second_num
  operation = 'Subtraction'
elif operator == "/":
  result = first_num / second_num
  operation = 'Division'
elif operator == "**":
  result = first_num ** second_num
  operation = 'Power'
else:
  operation = None
  print('Sorry invalid operation')

if operation != None:
  print(f'{operation} result is {result:,.2f}')
  






