

print(f'Please, Enter the Numbers you want to compare \n{"-"*20}')

num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))
num3 = float(input("enter the third number:"))

print("-"*20)

if num1 > num2 :
  if num1 > num3:
    print(f'{num1}is the greatest number')
  else:
    print(f'{num3}is the greatest number')
elif num2 > num3:
  print(f'{num2}is the greatest number')
else:
    print(f'{num3}is the greatest number')