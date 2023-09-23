#Project1
sum = 0
num = 1

while num <=100:
  sum += num
  num += 1

print(sum)

#Project2

total = 0
nux = 70

while nux <=160:
  sum += nux
  nux += 1

print(sum)


#Project3

summ = 0
even_num = 30

while even_num <= 470:
  if even_num % 2 == 0:
    sum += even_num
  even_num += 1

print(sum)

#Project4

summation = 0
nums = 1

while nums <=1000:
  if nums % 3 == 0:
    summation += nums
  nums += 1
print(summation)

#Project5

sum = 0
num = 1

while num <= 2000:
  if num % 3 == 0 and num % 7 == 0:
    sum += num
  num += 1
print(sum)

#Project6

##output "1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29"

nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 
25, 27, 29]

s = "1"
idx = 1

while idx < len(nums):
  str_nums = str(nums[idx])
  s += ','+ str_nums 
  idx += 1
  
print(s)

