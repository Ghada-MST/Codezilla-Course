#project1
sum = 0

while True:
  user_input = input('Enter a number: ')
  if user_input.lower() == 'done' or user_input == '':
    break
  else:
    sum += float(user_input)
print(f"The total is: {sum}")

#project2

total = 0
while True:
  user_input = input("Enter the number: ")
  if user_input.lower() == 'done' or len(user_input) == 0 :
    break
  num = float(user_input)
  if num % 2 != 0:
    continue
  total += num
print(f"The total of the even numbers is: {total}")

#project3

sum = 0
while True:
  user_input = input('Enter the number: ')
  if user_input.lower() == 'done' or user_input == "":
    break
  num = float(user_input)
  if num  > 0 and num % 2 == 1:
    sum += num
  else:
    print(f'Error, {num} is not a positive odd number!!')
    
print(f"The total of the positive odd numbers is: {sum}")

#project4

multiply = 1
while True:
  num = input('Enter the number: ')
  if num.lower() == 'done' or len(num) == 0:
    break
  num = float(num)
  if num != 0 :
    multiply *= num
  else:
    print('Error: 0 is ignored')
print(f"The product of the numbers is: {multiply}")

#project5

num = 452
lst = []
while num < 983:
  if num % 5 == 0 and num % 7 == 0:
     lst.append(num) 
  num += 1
print(lst)   

average = (lst[1] + lst[-2]) / 2

print (f'the average number is {average}')




#project6

# A)
# initialize the total to 0
total = 0
while True:
# Ask for a number
  number = input("Enter a number: ")
# If the user enters "done", or pressed Enter key then break out of the loop
  if number.lower() == "done" or len(number) < 1 : 
    break
# SUM ODD NUMBERS
  number = float(number)
  if number%2 == 0: 
    continue
  total += number
print(f"The total is: {total}")


# B)
total = 0
# Always ask for a number
while True:
# Ask for a number
  number = input("Enter a number: ")
# If the user enters "done", or pressed Enter key then break out of the loop
  if number.lower() == "done" or len(number) < 1: 
    break
# SUM NUMBERS DIVISIBLE BY 3
  number = float(number)
  if number%3 != 0: 
    continue
  total += number
# Print the total
print(f"The total is: {total}")