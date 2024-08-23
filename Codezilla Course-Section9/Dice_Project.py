
import random

dice = random.randint(1,6)

guess = int(input('''Guess the Roll Dice!
Enter a number between 1 and 6
>>> '''))
print('-'*20)

if guess == dice:
  print(f'''The Dice is {dice}
You Won!''')
else:
  print(f'''The Dice is {dice}
You Lost!''')