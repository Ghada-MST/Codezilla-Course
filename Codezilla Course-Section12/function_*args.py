def average(*args):
  return sum(args) / len(args)


average = average(10, 20, 30)
print(average)


#Project1##################################
#Complete the following function to count the positive even numbers.
def count_positive_even_numbers(*nums):
  count = 0
  for num in nums:
    if num > 0 and num % 2 == 0:
      count += 1
  return count


count_positive_even = count_positive_even_numbers(1, 2, 3, -4, -5, -6, -7, 8,
                                                  9, 10)

print(count_positive_even)


#another answer
def count_positive_even_numbers(*nums):
  count = len([num for num in nums if num > 0 and num % 2 == 0])
  return count


count_positive_even = count_positive_even_numbers(1, 2, 3, -4, -5, -6, -7, 8,
                                                  9, 10)

print(count_positive_even)

#Project2##################################
# Make a function that generates random even numbers allowing the user to specify the number of even numbers to generate and the range of the numbers.
import random


def random_even_nums(numbers_even_num, *range_nums):
  num = 0
  rand_list = []
  while num < numbers_even_num:
    rand_num = random.randint(*range_nums)
    if rand_num % 2 == 0:
      rand_list.append(str(rand_num))
      num += 1

  str_rand_list = ', '.join(rand_list)
  return str_rand_list


numbers_even_num = int(
  input("Enter the numbers of the even numbers to generate: "))
start = int(input("Enter the start range : "))
stop = int(input("Enter the end range : "))
generated_nums = random_even_nums(numbers_even_num, start, stop)
print(f'''\nThe generated random numbers are
-------------------------------
{generated_nums}''')


#another answer حل مهندس محمد
def random_even_num(numbers_even_num, start_range, stop_range):
  rand_even_num = [
    num for num in range(start_range, stop_range) if num % 2 == 0
  ]
  return random.sample(rand_even_num, numbers_even_num)


random_20_even_numbers = random_even_num(numbers_even_num=20,
                                         start_range=1,
                                         stop_range=100)
print(random_20_even_numbers)


#another answer
def random_even_nums(numbers_even_num, start, stop):
  rand_list = []
  while len(rand_list) < numbers_even_num:
    rand_num = random.randint(start, stop)
    if rand_num % 2 == 0:
      rand_list.append(str(rand_num))
  str_rand_list = ", ".join(rand_list)
  return str_rand_list


random_20_even_numbers = random_even_nums(numbers_even_num=20,
                                          start=1,
                                          stop=100)
print(random_20_even_numbers)

#Project3####################################
# Make a function that converts a list containing numbers as string to a list containing numbers as integers.


def convert_list_to_int(num_str_list):

  num_int = [int(float(num)) for num in num_str_list]
  print(num_int)


num_str_list = ["23", "55", "21.5", "9.5", "70"]
convert_list_to_int(num_str_list)