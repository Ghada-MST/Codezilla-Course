
num = float(input('enter a number: '))
div_num = float(input('enter the number to divide by: '))

div_result = num/div_num
print(f"{'-'*30} \nThe division result is {div_result:.3f}")

if num % div_num == 0:
  print(f"{num} is divisible by {div_num}")

else:
  print(f"{num} is not divisible by {div_num}")
