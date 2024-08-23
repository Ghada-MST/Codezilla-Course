


#project1
while True:
  answer = input('Please enter input: ').strip()
  if answer.lower() == 'done':
    print('Done!')
    break
  elif answer=='' or answer.startswith('#'):
    continue 
  else:
    print(answer)
#حل مهندس اسلام 
while True:
# Read the input
  line = input('> ')
# ignoring blank lines and lines that start with #
  if line.startswith('#') or len(line) < 1:
    continue
# Check if the input is "done" 
  if line == 'done':
    break
# Print the input
  print(line)
# End of the program
print('Done!')

#project2

from random import randint

random_num = randint(1, 100)
attempts = 0

while True:
  user_guess = int(input('Guess the number from 1 to 100: '))
  attempts +=1
  if user_guess >100 or user_guess < 1:
    print('Error in entry!!')
    continue
  if user_guess < random_num:
    print('Too low, try again')
  elif user_guess > random_num:
    print('Too high, try again')
  else:
    print(f'You guessed the number in {attempts} attempts')
    break
#حل مهندس اسلام
import random
# generate a random number between 1 and 100
random_number = random.randint(1, 100)
guess = 0
attempts = 0
while guess != random_number:
  guess = int(input("Guess the number: "))
  attempts += 1
  if guess > random_number:
    print("Too high, try again")
  elif guess < random_number:
    print("Too low, try again")
    
print(f"You guessed the number in {attempts} attempts")
      
#project3

# find the first multiple of 7 in a list of numbers
numbers = [953, 776, 532, 665, 973, 683, 484, 499, 741, 980]
idx = 0
while idx < len(numbers):
  if numbers[idx]%7 == 0:
    print(f'the first multiple of 7 is: {numbers[idx]}')
    break
  idx +=1

#project4
score_lst = []
while True:
  user_input = input("Enter a score (or type 'done' to exit): ")
  if user_input == '' or user_input.lower() == 'done':
    break
  score = float(user_input)
  score_lst.append(score)

total_score = sum(score_lst)/len(score_lst)
print(f'The average of the scores is: {total_score:.1f}')

#project5

products_lst = []

while True:
  product_name = input('Enter product name: ')
  
  if product_name == "" or product_name.lower() == 'quit':
    break
    
  product_quantity = float(input('Enter quantity: '))
  product_price = float(input('Enter price: '))
  
    
  print('-'*15)
  
  total_item_cost = product_quantity * product_price#.2f
  products_lst.append(total_item_cost)
  
  print(f'Total item cost {total_item_cost}')
  print('-'*30)

products_lst.sort(reverse=True)
total_cost = sum(products_lst)

if len(products_lst) > 0:
  print('''Thank you for shopping with Codezilla. Have a great day!
Prices in descending order:''')

  idx = 0
  while idx < len(products_lst):
    print(f'''
  Price {idx+1}: {products_lst[idx]}''')
    idx+=1
  
  print(f"""{'-'*30}
  Total cost: {total_cost}""")
else:
  print('Thank you for shopping with Codezilla. Have a great day!')

#project6

initial_balance = 1000 


while True:
  print('''Welcome to the ATM. Please select an option:
1. Check balance
2. Withdraw
3. Deposit
4. Exit''')
  user_input = input('Enter option number: ')
  if user_input == "1":
    print(f'Your balance is ${initial_balance}')
    continue
  elif user_input == "2":  
      withdraw_amount = float(input('Enter withdraw amount: '))
      operation = 'Withdrawal'
      if withdraw_amount <= initial_balance :
         
        initial_balance -= withdraw_amount
      else:
        print('Insufficient balance.')
        continue
    
  elif user_input == "3":
      deposit_amount = float(input('Enter deposit amount: '))
      operation = 'Deposit'
     
      initial_balance += deposit_amount
  else:
    print('Thanks for banking with us. Have a great day.')
    break
  print(f'{operation} Successful. Your new balance is: ${initial_balance}')