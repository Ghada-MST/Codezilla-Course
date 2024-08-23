words = [
'each', 'those', 'feel', 'seem', 'high', 'place', 
'little', 'world', 'very', 'still', 
'nation', 'hand', 'life', 'tell', 'write', 'become', 
'here', 'show', 'house', 'both', 
'between', 'need', 'mean', 'call', 'develop', 'under', 
'last', 'right', 'move', 'thing', 
'general', 'school', 'never', 'same', 'another', 
'begin', 'while', 'number', 'part', 
'turn', 'real', 'leave', 'might', 'want', 'point', 
'form', 'child', 'small', 'since', 
'against', 'late', 'home', 'interest', 'large', 
'person', 'open', 'public', 'follow', 
'during', 'present', 'without', 'again', 'hold', 
'codezilla', 'govern', 'around', 
'head', 'consider', 'word', 'program', 'problem', 
'however', 'lead', 'system', 
'order', 'plan', 'keep', 'face', 'group', 'play', 
'stand', 'increase', 
'early', 'course', 'change', 'help', 'line', 
'possible', 'fact', 'down']

# user input
inp = input("Enter a word: ")
# a variable to check the word is in the list or not
check_word = True
# search for the word
for word in words:
# check if the word is in the list
  if word == inp.lower():
    print(f"The word ({inp}) is in the list")
    check_word = False
  break
# print the word is not in the list
if check_word:
   print(f"The word ({inp}) is not in the list")


###########################################################3
#Prime number is an integer number that is only divisible by 1 and itself

# 2. is prime number
# prime number is an integer number that is only divisible by 1 and itself
# user input
number = int(input("Enter an integer number: "))
# define a Boolean Expression Flag to check if the number is prime
is_prime = True
# loop through 2 to (number - 1)
for i in range(2, number):
# check if number is divisible by any number between 2 and itself
  if number % i == 0:
# change the flag
    is_prime = False
  break
# print the result
if is_prime:
  print(f"{number} is a prime number")
else:
  print(f"{number} is not a prime number")


########################################################################
# solution 1
# list of numbers
numbers = [-500, -694, -762, -445, -348, -361, -758, -594, -
954, -861, -610, -549, -336, 
-400, -600, -836, -671, -573, -555, -390, -450, -811, -
849, -870, -815, -694, 
-951, -588, -484, -609, -674, -411, -408, -498, -649, -
541, -441, -839, -567, -898]
# empty list to store positive numbers
positive_numbers = []
# loop through the list
for number in numbers:
# check if number is negative
  if number < 0:
    number *= -1
# add the number to the list
  positive_numbers.append(number)
print(positive_numbers)

# solution 2
# list of numbers
numbers = [-500, -694, -762, -445, -348, -361, -758, -594, -
954, -861, -610, -549, -336, -400, -600, -836, -671, -573, -
555, -
390, -450, -811, -849, -870, -815, -694, -951, -588, 
-484, -609, -674, -411, -408, -498, -649, -541, -441, -839, -
567, -898]
# empty list to store positive numbers
positive_numbers = []
# loop through the list
for number in numbers:
# add the absolute value of number to the list using abs() function
  positive_numbers.append(abs(number))
print(positive_numbers)

#################################################################

lst_words = [['have', 'that', 'they', 'with', 'this', 'from', 
'which', 'would', 'will', 'there', 'make', 'when', 'more', 
'other', 'what', 'time', 'about', 'than', 'into', 'could'], 
[ 'state', 'only', 'year', 'some', 'take', 'come', 'these', 
'know', 'like', 'then', 'first', 'work', 'such', 'give', 
'over', 'think', 'most', 'even', 'find', 'also', 'after', 
'many', 'must', 'look', 'before', 'great', 'back', 'through', 
'long'], 
[ 'where', 'much', 'should', 'well', 'people', 'gouda', 'just', 
'because', 'good', 'each', 'those', 'feel', 'seem', 'high', 
'place', 'little', 'world', 'very', 'still', 'nation', 'hand', 
'life', 'tell', 'write', 'become', 'here', 'show', 'house', 
'both', 'between', 'need', 'mean', 'call', 'develop', 'under', 
'last', 'right', 'move', 'thing'], 
['general', 'school', 'never', 'same', 'another', 'begin', 
'while', 'number', 'part', 'turn', 'real', 'leave', 'might', 
'want', 'point', 'form', 'child', 'small', 'since', 'against', 
'late', 'home', 'interest', 'large', 'person', 'open', 
'public', 'follow', 'during', 'present', 'without', 'again', 
'hold', 'codezilla', 'govern', 'around', 'head', 'consider', 
'word', 'program', 'problem', 'however', 'lead', 'system'],
['order', 'plan', 'keep', 'face', 'group', 'play', 'stand', 
'increase', 'early', 'course', 'change', 'help', 'line', 
'possible', 'fact', 'down']]
# define a counter
counter_a = 0
counter_e = 0
# loop through the list of words
for lst in lst_words:
# loop through the words in the list
  for word in lst:
# loop through the letters in the word
    for letter in word:
# check if letter is a or e
      if letter == 'a':
        counter_a += 1
      elif letter == 'e':
        counter_e += 1
# print the result
print(f"The number of letter 'a' in Words is {counter_a}")
print(f"The number of letter 'e' in Words is {counter_e}")