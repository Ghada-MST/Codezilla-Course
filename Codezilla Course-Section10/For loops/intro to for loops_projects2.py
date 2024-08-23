
#project1

numbers = [1, 2, 3, 4, 5]
# Initialize an empty list to store the squares of the numbers
squared_lst = []
for num in numbers:
  square = num**2
  squared_lst.append(square)
print(squared_lst)

#project2
scores = [75, 87, 93, 98, 82, 67, 91, 88]
lst = []                                                 
for score in scores:
  score = str(score) + '%'
  lst.append(score)
print(lst)

#project3
fruits = ["APPLE", "ORANGE", "BANANA", "PEAR", "MANGO"]
lst =[]
for fruit in fruits:
  lst.append(fruit.lower())
print(lst)

#project4
names = ["mohamed gouda", "islam mahfouz", "ayman hamed", "hassan ali", 
"mostafa mohamed"]
lst = []
for name in names:
  lst.append(name.title())
print(lst)

#project5

user_str = input('Enter the word: ')
lst = []
for char in user_str:
  lst.append(char.upper())

print(f'The list of the given name is {lst}')

#project6

prices = [10.99, 20.99, 30.99, 40.99, 50.99]
lst = []
for price in prices :          # for price in prices :
  price_str = str(price) +'$'     #lst.append(f"{price}$")
  lst.append(price_str)

print(f'The price list is {lst}')

#project7
# A list of prices
prices = [75, 153, 635, 144, 356, 712, 675, 234]
total_prices = 0
sum_elements = 0 #count
for price in prices:
  total_prices += price
  sum_elements += 1 #count
average = total_prices/sum_elements
print(f'the Total price is {total_prices}$ and the number of elements in the list are {sum_elements} and the average is {average:.2f}$')


#project8

nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 
25, 27, 29]
lst = []
for num in nums:
  lst.append(str(num))
  
join_nums = ', '.join(lst)
print(join_nums)

#حل مهندس اسلام
# Define the list of numbers
nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
# Initialize the string with the first number
string = str(nums[0])
# Use a for loop to iterate over the items in the list, starting from the second item
for num in nums[1:]:
# Add the current item to the string, separated by a comma
  string += ", " + str(num)
# Print the resulting string
print(string)