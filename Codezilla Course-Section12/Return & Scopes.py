#project1################################################################
#Make a function that sums only the odd numbers in a list of numbers.
def sum_odd_numbers(numbers):
  # Complete this function
  total = 0
  for number in numbers:
    if number % 2 == 1:
      total += number
  return total


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total_odd = sum_odd_numbers(numbers)
print(total_odd)


#another answer
def sum_odd_numbers(numbers):
  return sum([number for number in numbers if number % 2 == 1])


#project2################################################################
# Make a function that returns the maximum even number in a list.
def max_even_num(num_list):
  max_num = num_list[0]
  for num in num_list:
    if num % 2 == 0 and num > max_num:
      max_num = num
  return max_num


numbers2 = [1, 2, 3, 4, 5, 6, 24, 7, 8, 9, 10, 11, 12]
max_even_num2 = max_even_num(numbers2)
print(max_even_num2)

#another answer


def max_even_num(num_list):
  even_nums = []
  for num in num_list:
    if num % 2 == 0:
      even_nums.append(num)
  max_even_num = max(even_nums)
  return max_even_num


numbers3 = [1, 2, 3, 4, 5, 6, 24, 7, 8, 9, 10, 11, 12]
max_even_num3 = max_even_num(numbers3)
print(max_even_num3)


#another answer
def max_even_num(num_list):
  even_nums_list = [num for num in num_list if num % 2 == 0]
  return max(even_nums_list)


#project3################################################################
#Make a function that returns the minimum odd number in a list.
def min_odd_num(num_list):
  min_odd_num = num_list[0]
  for num in num_list:
    if num % 2 == 1 and num < min_odd_num:
      min_odd_num = num
  return min_odd_num


#another answer
def min_odd_num(num_list):
  min_num_list = []
  for num in num_list:
    if num % 2 == 1:
      min_num_list.append(num)
  min_odd_num = min(min_num_list)
  return min_odd_num


numbers4 = [2, 3, 4, 5, 6, 24, 7, 8, 23, 9, 10, 11, 12]
min_odd_num4 = min_odd_num(numbers4)
print(min_odd_num4)


#another answer
def min_odd_num(num_list):
  odd_list = []
  for num in num_list:
    if num % 2 != 0:
      odd_list.append(num)
  odd_list.sort()
  return odd_list[0]


numbers5 = [2, 3, 4, 5, 6, 24, 7, 8, 23, 9, 10, 11, 12]
min_odd_num5 = min_odd_num(numbers5)
print(min_odd_num5)


#project4################################################################
# Make a function that returns the number of (enumeration of) even numbers in a list.
def len_even_nums(num_list):
  even_num_list = []
  for num in num_list:
    if num % 2 == 0:
      even_num_list.append(num)
  return len(even_num_list)


numbers6 = [2, 3, 4, 5, 6, 24, 7, 8, 23, 9, 10, 11, 12]
print(len_even_nums(numbers6))


#another answer
def len_even_nums(num_list):
  enumeration = 0
  for num in num_list:
    if num % 2 == 0:
      enumeration += 1
  return enumeration


#project5################################################################
#Make a function that returns the number of negative odd numbers in a list.
def len_negative_odd_num(num_list):
  negative_odd_num_list = []
  for num in num_list:
    if num % 2 == 1 and num < 0:
      negative_odd_num_list.append(num)
  return len(negative_odd_num_list)


numbers7 = [2, 35, 4, -50, 6, 24, -7, 8, -23, -9, -10, -11, 12]
print(len_negative_odd_num(numbers7))


#another answer
def count_negative_odd_numbers(numbers):
  return len(
    [number for number in numbers if (number < 0) and (number % 2 != 0)])


#another answer
def len_negative_odd_num(num_list):
  enumeration = 0
  for num in num_list:
    if num % 2 != 0 and num < 0:
      enumeration += 1
  return enumeration


#project6################################################################
#Make a function that returns the string while making vowels and the first letter of each word capital.

text = "returns the result (value of the expression following the return keyword) to the caller. The statements after the return statements are not executed. If the return statement is without any expression, then the special value "


def capitalize_char(text):
  vowels = "aieou"
  modified_text = ""
  text_list = text.split()
  for word in text_list:
    #title() convert for example "HAPPY" to "Happy"
    word_title = word.title()
    for letter in word_title:
      if letter in vowels:
        modified_text += letter.capitalize()
      else:
        modified_text += letter

    modified_text += " "
  return modified_text


modified_text = capitalize_char(text)
print(modified_text)


#another answer
def capitalize_char(text):
  vowels = "aieou"
  modified_text = ""
  text_list = text.split()
  for word in text_list:
    #title() convert for example "HAPPY" to "Happy"
    word_upper = word.title()
    for letter in word_upper:
      if letter in vowels:
        modified_text += letter.capitalize()
        continue
      modified_text += letter
    modified_text += " "
  return modified_text


print(capitalize_char(text))
modified_text = capitalize_char(text)
print(modified_text)

#another answer


def title_cpital_vowels(text):
  #title() convert for example "HAPPY" to "Happy"
  modified_text = text.title()
  vowels = 'aieou'
  vowels_upper = "AIEOU"
  table = str.maketrans(vowels, vowels_upper)
  print(modified_text.translate(table))
  # or return modified_text.translate(mapping_table)


title_cpital_vowels(text)


#another answer
def title_cpital_vowels(text):
  #title() convert for example "HAPPY" to "Happy"
  modified_text = text.title()
  vowels = 'aieou'
  mapping_table = str.maketrans(vowels, vowels.upper())
  print(modified_text.translate(mapping_table))
  # or return modified_text.translate(mapping_table)


title_cpital_vowels(text)

#another answer


def title_cpital_vowels(text):
  #title() convert for example "HAPPY" to "Happy"
  modified_text = text.title()
  vowels = 'aieou'
  modified_text = "".join(
    [char.upper() if char in vowels else char for char in modified_text])
  print(modified_text)


title_cpital_vowels(text)


#another answer
def title_cpital_vowels(text):
  vowels = 'aieou'
  #title() convert for example "HAPPY" to "Happy"
  modified_text = text.title()
  for vowel in vowels:
                                                #or vowel.upper()
    modified_text = modified_text.replace(vowel, vowel.capitalize())
  print(modified_text)


title_cpital_vowels(text)
