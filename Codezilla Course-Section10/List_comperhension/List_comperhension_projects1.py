


fruits = ['apple','banana','kiwi','mango']

fruits_upper = [fruit.upper() for fruit in fruits]

print(fruits_upper)

#project1##########################################
nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]

negative_nums = [-num  for num in nums] 
print(negative_nums)

#project2##########################################
nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]

square_nums = [num**2 for num in nums]
print(square_nums)

#project3##########################################
scores = [75, 87, 93, 98, 82, 67, 91, 88]

percent_score = [str(score) +'%' for score in scores]
print(percent_score)

#project4##########################################
fruits = ["APPLE", "ORANGE", "BANANA", "PEAR", "MANGO"]

fruits_lower = [fruit.lower() for fruit in fruits]
print(fruits_lower)

#project5##########################################
nums = [2, 29, 4, 8, 42, 55, 70, 74, 78, 27]

even_nums = sum([num for num in nums if num%2==0])
print(even_nums)

#project6##########################################
prices = [10.99, 20.99, 30.99, 40.99, 50.99]

currency = ['$'+str(price) for price in prices]
print(currency)