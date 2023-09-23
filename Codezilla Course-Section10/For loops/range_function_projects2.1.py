
#project1
sum = 0
for i in range(1,101):
  sum+=i
print(sum)

#project2
total = 0
for i in range(70, 161):
  total+=i
print(total)

#project3
sum_even = 0

for even_num in range(30,471,2):
  sum_even += even_num

print(sum_even)

#project4
total = 0

for num in range(1, 1001):
  if num % 3==0:
    total+=num
print(total)

#project5

lst = []
for num in range(452, 984):
  if num%5==0 and num%7==0:
    lst.append(num)
average = (lst[1]+lst[-2])/2 
print(average)