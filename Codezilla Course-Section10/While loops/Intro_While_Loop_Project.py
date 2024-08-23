#project1
num = 1

while num <= 100:
  print(num)
  num +=1


#project2
even_num = 2

while even_num <= 1000:
  print(even_num)
  even_num += 2
  
#project2
even_num = 2
lst = []
while even_num <= 1000 and even_num % 2 == 0 :
  even_num += 2
  lst.append(even_num)
print(lst)

#project3

odd_num = -1

while  odd_num > -100:
  print(odd_num)
  odd_num += -2

#project3

odd_num = -99
while odd_num < 0 and odd_num % 2 != 0:
  print(odd_num)
  odd_num += 2
  
#project4

nums = 12
t = []
while nums <= 99:
  t.append(nums)
  nums +=1

print(t)
  


#project5
# loop through the list items by using a while loop
fruits = ['apple', 'banana', 'orange', 'grape', 
'kiwi', 'mango', 'strawberry', 'pineapple']

i = 0
while i < len(fruits):
  print(fruits[i])
  i += 1