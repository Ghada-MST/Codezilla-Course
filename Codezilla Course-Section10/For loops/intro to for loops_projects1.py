#project1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for num in numbers:
  sum += num
print('the sum of the numbers is',sum)

#project2
numbers = [1, 2, 3, 4, 5]

for num in numbers:
  square = num**2
  print(f'The square of {num} is {square}')

#project3>>>>>space considered as a character
string = "Codezilla Python Course"

for character in string:
  print(character)

#project4
#A list of prices for different items in dollars
prices = [10.99, 9.99, 15.99, 7.99, 12.99]
total = 0
for price in prices:
  total += price
print(f'the total cost is {total} $')

#project5
numbers = [1, 2, 3, 4, 5]
product = 1
for num in numbers:
  product *= num

print(f'the product of the numbers is {product}')



#project6
#1حل 
product = 1
numbers = []

while True:
  num = input('Enter a number (0 to stop): ')
  if num == 0:
    break
  numbers.append(num)

for num in numbers:
  product *= num
  
print(f'the product of the numbers {numbers} is {product:,.2f}')

#حل 2 
user_range = float(input("enter the number: "))
product = 1
for _ in range(user_range):
    user_massege = int(input("enter number: "))
    product *= user_massege
print(product)