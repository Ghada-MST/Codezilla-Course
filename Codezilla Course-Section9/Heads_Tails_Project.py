
import random

guess = int(input('''Guess the coin flip!
Enter
1 for Heads
2 for Tails
>>> '''))
print('-'*20)

heads_tails = ['Heads','Tails']

if guess == random.randint(1,2):
  print(f'''The coin is {heads_tails[guess-1]}
You Won!''')
else:
  print(f'''The coin is {heads_tails[guess-1]}
You Lost!''')


# import random

# guess = int(input('''Guess the coin flip!
# Enter
# 1 for Heads
# 2 for Tails
# > '''))
# print('-'*20)
 
# heads_tails = ['Heads','Tails']
# ch = random.randint(1,2) 
# print(ch)
# if guess == ch:
    
#     print(f'''The coin is {heads_tails[guess-1]}
#  You Won!''')
# else:
    
#     print(f'''The coin is {heads_tails[guess-1]}
#  You Lost!''')