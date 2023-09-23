

input = input('Enter your input: ')



if input.isnumeric():
  print('You entered a number')
elif input.isalpha():
  print('You entered letters')
  if input.islower():
    print('All letters are lowercase')
  elif input.isupper():
    print('All letters are uppercase')
  else: 
    print('There are letters in uppercase and lowercase')
elif input.isalnum():
  print('There is a mix between letters and numbers')
else:
  print('There are other characters than letters and numbers')
  


