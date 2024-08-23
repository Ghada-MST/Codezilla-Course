
# def adding_num(a):
#   #Base
#   if a==1:
#     return 1
#   #body
#   return a + adding_num(a-1)

# print(adding_num(5))
# ############################################
# def sub(a,b):

#   if b==0:
#     return a
#   return sub(a-1,b-1)

# print(sub(20,10))
# ##############################################

# def add_num(a):
#   if a==1:
#     return 1
#   return a + add_num(a-1)

# print(add_num(5)

# #####################################################
      
# def reverse(number):
#   remainder = 0
#   if number%10==0:
#     return 0
#   remainder *=10
#   remainder += number%10
#   return remainder+reverse (number//10)

# print(reverse(123))

#################################################
# lst = [1,2,3]
# result = 0
# for i in lst:
#   result += i**2
# print(result)

# def flatten(lst):
#   flat_list = []
#   for item in lst:
#       if isinstance(item, list):
#           flat_list.extend(flatten(item))
#       else:
#           flat_list.append(item)
#   return flat_list

# nested_list = [1, [2, [3, 4], 5], 6, [7, 8, [9, 10]]]
# flat_list = flatten(nested_list)
# print(flat_list)

# def sumsquares(lst):
#   flat_list = []
#   for item in lst:
#     if isinstance(item,list):
#       flat_list.extend(sumsquares(item))

#     else :
#       flat_list.append(item)
  
#   return sum( [item**2 for item in flat_list])

# nested_list = [1, [2, [3, 4], 5], 6, [7, 8, [9, 10]]]
# print(sumsquares(nested_list))


# def sumsquares(lst):
#   total = 0  # Initialize total sum of squares
#   for item in lst:
#       if isinstance(item, list):
#           total += sumsquares(item)  # Recursively calculate the sum of squares
#       else:
#           total += item ** 2  # Square the number and add to total
#   return total

# nested_list = [1, [2, [3, 4], 5], 6, [7, 8, [9, 10]]]
# print(sumsquares(nested_list))  # Output: 385


x=12
y=12

if x==y:
    print("yay")
else:
    print('loser')


