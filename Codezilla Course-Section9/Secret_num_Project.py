
import random

guess = int(input('Enter the number between 1 to 20: '))

print('-'*20)

secret_num1 = random.randint(1,20)
secret_num2 = random.randint(1,20)
secret_num3 = random.randint(1,20)
secret_num4 = random.randint(1,20)
secret_num = [secret_num1, secret_num2, secret_num3, secret_num4]


if guess in secret_num:
  print('You Won!!')

else:
  print('You Lost')