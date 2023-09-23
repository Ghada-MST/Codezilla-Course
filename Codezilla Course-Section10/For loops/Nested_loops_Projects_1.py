#project1#############################################################
  
nested_list = [
["Hello", "from", "Codezilla"], 
["Python", "Course", "is", "awesome"], 
["I", "enjoy", "learning", "Python", "with", "Codezilla"]
]
#method1
i=0
lst=[]
while i < len(nested_list):
  lst.extend(nested_list[i])
  i+=1  
print(lst)

  #method2
x=[]
i = 0
for lst in nested_list:
  for word in lst:
    x.append(word)
print(x)

  #method3
x=[]
for lst in nested_list:
  x.extend(lst)
print(x)




#project2###############################################################################
numbers = [511, 260, 261, 912, 362, 473, 893, 277, 351, 494, 
486, 885, 341, 484, 598, 950, 859, 716, 488, 584]
num_9 = []
for num in numbers:
  if num%9 == 0:
    num_9.append(num)
print(num_9)
smallest_num = min(num_9)
print(f'the smallest num is {smallest_num}')

# تعديل وحل مهندس اسلام
numbers = [511, 260, 261, 912, 362, 473, 893, 277, 351, 494, 
486, 885, 341, 484, 598, 950, 859, 716, 488, 584]
numbers.sort()

for num in numbers:
  if num%9==0:
    print(f'The smallest multiple of 9 is: {num}')
    break








#project3##############################################################################
numbers = [-588, -479, -713, -701, -885, -578, -835, -466,
-935, -665, -360, -837, -389, -367, -454, -668, -907, -822,
-541, -680, -405, -330, -625, -916, -331, -876, -689, -753,
-810, -648, -787, -952, -718, -401, -502, -699, -533, -450,
-580, -725]

#حل بعد البحث علي النت
largest_number = None

for number in numbers:
    if  largest_number is None or largest_number < number:
        largest_number = number

# ✅ get the largest number
print(largest_number)  

# ✅ get the index of the largest number
print(numbers.index(largest_number))  

# حل مهندس اسلام
largest_num = numbers[0]
for num in numbers:
  if num > largest_num:
    largest_num = num
print(f'the largest number is {largest_num}')







#project4######################################################################################
numbers = [-500, -694, -762, -445, -348, -361, -758,
-594, -954, -861, -610, -549, -336, -400, -600, -836,
-671, -573, -555, -390, -450, -811, -849, -870, -815, -694,
-951, -588, -484, -609, -674, -411, -408, -498, -649,
-541, -441, -839, -567, -898]

largest_even_num = -500
for num in numbers:
  if num %2 == 0 and num > largest_even_num:
    largest_even_num = num
print(f'the largest even number is {largest_even_num}')


#حل مهندس اسلام 

numbers = [-500, -694, -762, -445, -348, -361, -758, -594, -
954, -861, -610, -549, -336, -400, -600, -836, -671, -573, -
555, -
390, -450, -811, -849, -870, -815, -694, -951, -588,
-484, -609, -674, -411, -408, -498, -649, -541, -441, -839, -
567, -898]
# initialize the largest even number
for number in numbers:
# check if the number is even
  if number % 2 == 0:
# update the largest even number
    largest_even = number
    break
# loop through the list
for number in numbers:
# check if the number is even and larger than the largest even number
  if number % 2 == 0 and number > largest_even:
# update the largest even number
    largest_even = number
print(f"The largest even number is {largest_even}")