#project1#################################################
nums = [6, 4, 8, 2, 9, 1, 5, 10, 3, 7]


def special_sum(numbers,
                only_even=False,
                only_odd=False,
                only_positive=False,
                only_negative=False):
  total = 0
  for num in numbers:
    if only_even:
      if num % 2 == 0:
        total += num
    elif only_odd:
      if num % 2 != 0:
        total += num
    elif only_positive:
      if num > 0:
        total += num
    elif only_negative:
      if num < 0:
        total += num
    else:
      total += num
  return total


print(f'The sum of all numbers is: {special_sum(nums)}')
print(f'The sum of even numbers is: {special_sum(nums, only_even=True)}')
print(f'The sum of odd numbers is: {special_sum(nums, only_odd=True)}')
print(
  f'The sum of positive numbers is: {special_sum(nums, only_positive=True)}')
print(
  f'The sum of negative numbers is: {special_sum(nums, only_negative=True)}')

#project2#################################################
#Make a function that converts a list containing numbers as string or float to a list containing numbers as integers with an option to convert to float and an option to convert to string.

str_lst = ['1.5', '2', '3.5', '4', '5']
float_lst = [1.5, 2.5, 3.5, 4.5, 5.5]


def convert_to_integer(num_lst,
                       convert_to_float=False,
                       convert_to_string=False):
  conversion_list = []
  for num in num_lst:
    if convert_to_float:
      conversion_list.append(float(num))
    elif convert_to_string:
      conversion_list.append(str(num))
    else:
      conversion_list.append(int(float(num)))

  return conversion_list


#convert to integers
numbers_int = convert_to_integer(str_lst)
print(numbers_int)

#convert to float
numbers_float = convert_to_integer(str_lst, convert_to_float=True)
print(numbers_float)

#convert to string
numbers_string = convert_to_integer(float_lst, convert_to_string=True)
print(numbers_string)


#another answer مهندس محمد
def convert_list_to_integers(numbers,
                             convert_to_float=False,
                             convert_to_string=False):
  if convert_to_string:
    return [str(number) for number in numbers]
  if convert_to_float:
    return [float(number) for number in numbers]
  return [int(float(number)) for number in numbers]


#project3#################################################
# Make a function that the maximum even number from a list of arguments allowing the user to get, if he chooses, the second maximum even number till the nth maximum even number.


def max_even_number(*numbers, nth_max_even=None):

  even_num_list = [num for num in numbers if num % 2 == 0]
  even_num_list.sort(reverse=True)
  if nth_max_even:
    max_num = numbers[nth_max_even - 1]

  elif len(even_num_list) == 0:
    return 'There is no even number in the given list'

  else:
    max_num = numbers[0]

  return max_num


max_even = max_even_number(64, 52, 84, 76, 45, 36, 88)

third_max_even = max_even_number(64, 52, 84, 76, 45, 36, 88, nth_max_even=3)

print(f'Max even number: {max_even}')
print(f'Third max even number: {third_max_even}')

#another answer مهندس محمد


def max_even_number(*args, nth_max_even_number=1):
  lst_even_num = [num for num in args if num % 2 == 0]
  lst_even_num.sort(reverse=True)
  return lst_even_num[nth_max_even_number - 1]


print(max_even_number(1, 2, 3, -4, -5, -6, -7, 8, 9, 10))  #output : 10
print(max_even_number(1, 2, 3, -4, -5, -6, -7, 8, 9, 10,
                      nth_max_even_number=3))  #output : 2

#project4#################################################

# Make a function that calculates the average of a list of arguments allowing the user to pass a list of numbers as a single argument or pass a list of numbers as multiple arguments.


def average(*numbers):

  if len(numbers) > 1:
    average = sum(numbers) / len(numbers)
  else:
    average = sum(*numbers) / len(*numbers)

  return average


average1 = average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
average2 = average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
average3 = average((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
average4 = average({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})

print(f'Average1: {average1}')
print(f'Average2: {average2}')
print(f'Average3: {average3}')
print(f'Average4: {average4}')

#another answer مهندس محمد


def average(*args):
  # if the first argument is a list, tuple or set
  if type(args[0]) in (list, tuple, set):
    # unpack the list, tuple or set to get the numbers
    args = args[0]

  return sum(args) / len(args)


print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))  #output : 5.0
print(average([1, 2, 3, 4, 5, 6, 7, 8, 9]))  #output : 5.0
print(average((1, 2, 3, 4, 5, 6, 7, 8, 9)))  #output : 5.0
print(average({1, 2, 3, 4, 5, 6, 7, 8, 9}))  #output : 5.0


#another answer مهندس محمد
def average(*args):

  # Another Solution using isinstance function
  if isinstance(args[0], (list, tuple, set)):
    args = args[0]

  return sum(args) / len(args)


print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))  #output : 5.0
print(average([1, 2, 3, 4, 5, 6, 7, 8, 9]))  #output : 5.0
print(average((1, 2, 3, 4, 5, 6, 7, 8, 9)))  #output : 5.0
print(average({1, 2, 3, 4, 5, 6, 7, 8, 9}))  #output : 5.0
