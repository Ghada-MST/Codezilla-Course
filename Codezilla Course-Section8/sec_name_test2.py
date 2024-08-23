
print('It is the time to see if we could do better 😀')

print('-'*30)

num = float(input('Enter the number: '))
num_div = float(input('Enter the number to divide by: '))

answer = input(f'{num} is divisible by {num_div} yes or no? 🤔🤔\n').lower()

if (num % num_div==0 and answer=='yes') or (num % num_div!=0 and answer=='no'):
  print(f'{"-"*30} \nBravoooo!!! 🥳🥳🥳')

else:
  print(f"{'-'*30} \nNo problem, let's try again😀")
