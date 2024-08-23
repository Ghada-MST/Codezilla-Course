
#project1############################################
#method1
for i in range(1,11):
  for x in range(1,11):
    product = i*x
    print(f'{i} x {x} = {product}')
  print('-'*20)

#method1
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
  for x in lst:
    print(f'{i} x {x} = {i*x}')
  print('-'*20)


  
#project2############################################

words = ['have', 'that', 'they', 'with', 'this', 'from', 
'which', 'would', 'will', 'there', 'make', 'when', 'more', 
'other', 'what', 'time', 'about', 'than', 'into', 'could', 
'state', 'only', 'year', 'some', 'take', 'come', 'these', 
'know', 'like', 'then', 'first', 'work', 'such', 'give', 
'over', 'think', 'most', 'even', 'find', 'also', 'after', 
'many', 'must', 'look', 
'before', 'great', 'back', 'through', 'long', 'where', 'much', 
'should', 'well', 'people', 'gouda', 'just', 'because', 'good', 
'each', 'those', 'feel', 'seem', 'high', 'place', 'little', 
'world', 'very', 'still', 'nation', 'hand', 'life', 'tell', 
'write', 'become', 'here', 'show', 'house', 'both', 'between', 
'need', 'mean', 'call', 'develop', 'under', 'last', 'right', 
'move', 'thing', 'general', 'school', 'never', 'same', 
'another', 'begin', 'while', 'number', 'part', 'turn', 'real', 
'leave', 'might', 'want', 'point', 'form', 'child', 'small', 
'since', 'against', 'late', 'home', 'interest', 'large', 
'person', 'open', 'public', 'follow', 'during', 'present', 
'without', 'again', 'hold', 'codezilla', 'govern', 'around', 
'head', 'consider', 'word', 'program', 'problem', 'however', 
'lead', 'system', 'order', 'plan', 'keep', 'face', 'group', 
'play', 'stand', 'increase', 'early', 'course', 'change', 
'help', 'line', 'possible', 'fact', 'down']

#method1
words_upper=[]
for word in words:
  word_upper = word.upper()
  words_upper.append(word_upper)
print(words_upper)

#method2حل مهندس اسلام 
for i in range(len(words)):
  words[i] = words[i].upper()
  
print(words)

#project3############################################
#convert each inner list to a string

#join them with a space

#add them to a list named sentences

#Make another list replace spaces with dashes -

#convert each word to uppercase

words = [["Hello", "from", "Codezilla"], 
["Python", "Course", "is", "awesome"], 
["I", "enjoy", "learning", "Python", "with", "Codezilla"]]

#method1
x = ''
for lst in words:
    word_str1 = ' '.join(lst)
    print(word_str1)
    x += word_str1 + '.'
   
print('-'*20)

print(x)

print('-'*20)

x = x.strip('.')
sentences = x.split('.')
print(sentences)

print('-'*20)

lst2=[]
for sentence in sentences:
  y = sentence.upper().replace(' ','-')
  lst2.append(y)
print(lst2)


#method2حل مهندس اسلام 

sentences = []
for lst in words:
   sentences.append(' '.join(lst))

modified_sentences = []
for i in range(len(sentences)):
  modified_sentences.append(sentences[i].upper().replace(' ','-'))

# Print the sentences and modified_sentences
print(f"The list of sentences is: {sentences}")
print(f"The modified list of sentences is: {modified_sentences}")


#project4############################################
numbers = [-588, -479, -713, -701, -885, -578, -835, -466, -
935, -665, -360, -837, -389, -367, -454, -668, -907, -822, -
541, -680, -405, -330, -625, -916, -331, -876, -689, -753, -
810, -648, -787, -952, -718, -401, -502, -699, -533, -450, -
580, -725]

smallest_num = numbers[0]

for num in numbers:
  if num < smallest_num:
    smallest_num = num

print(f'the smallest num is :{smallest_num}')



#project5############################################
numbers = [-500, -694, -762, -445, -348, -361, -758, -594, -
954, -861, -610, -549, -336, -400, -600, -836, -671, -573, -
555, -390, -450, -811, -849, -870, -815, -694, -951, -588, -
484, -609, -674, -411, -408, -498, -649, -541, -441, -839, -
567, -898]

#method1
smallest_num = numbers[0]

for num in numbers:
  if num < smallest_num and num%2 == 1:
    smallest_num = num

print(f'the smallest odd num is :{smallest_num}')

#method2 حل مهندس اسلام
#assume the first odd number is the smallest
for number in numbers:
# check if the current number is odd
  if number % 2 != 0:
# if so, make the current number the smallest
    smallest_odd = number
# break the loop to avoid checking the rest of the numbers, since we already get the first odd number
    break
# loop through the list of numbers
for number in numbers:
# check if the current number is smaller than the smallest and odd
  if number % 2 != 0 and number < smallest_odd:
# if so, make the current number the smallest
    smallest_odd = number
print(f"The smallest odd number is {smallest_odd}")


      
#project6############################################
sentence = """Python is a widely used high-level 
general-purpose interpreted dynamic programming language
Its design philosophy emphasizes code readability and its 
syntax allows programmers to express concepts in fewer lines of 
code 
than possible in many other languages
The language provides constructs intended to enable clear 
programs on both a small and large scale
"""

lst = sentence.replace('-',' ').split()
print(lst)

word_lenght = 0
word_count = 0
for word in lst:
  word_lenght += len(word)
  word_count += 1
  
average =  word_lenght//word_count

print(word_lenght)
print(word_count)
print(f'the average word length in the sentence is {average}')
#method2 حل مهندس اسلام

# split the sentence into a list of words
words_list = sentence.split()
# initialize the total length
total_length = 0
# loop through the list of words
for word in words_list:
# increment the total length
  total_length += len(word)
# calculate the average word length
average_length = total_length / len(words_list)
# print the average word length
print(f"The average word length is {average_length:.2f} characters.")





#project7############################################
#method1
nested_list = [["Hello", "from", "Codezilla"], 
["Python", "Course", "is", "awesome"], 
["I", "enjoy", "learning", "Python"]]
for lst in nested_list:
  print(lst) # You can not remove this line
  for word in lst:
    print(word) # You can not remove this line
    if word == "Codezilla":
      print("Found Codezilla!") # This should be the last line to be printed
  break

#method2
found = False
nested_list = [["Hello", "from", "Codezilla"], 
["Python", "Course", "is", "awesome"], 
["I", "enjoy", "learning", "Python"]]
for lst in nested_list:
  print(lst) # You can not remove this line
  for word in lst:
    print(word) # You can not remove this line
    if word == "Codezilla":
      found = True
       # This should be the last line to be printed

if found:
  print("Found Codezilla!")


#method3 حل مهندس اسلام



#Solution 1: comparing words and exit the program with exit() function
for lst in nested_list:
  print(lst)
  for word in lst:
    print(word)
    if word == "Codezilla":
      print("Found Codezilla!")
      exit() # EXIT THE WHOLE PROGRAM
#########
#Solution 2: comparing words and exit the program with continue and exit() function 
for lst in nested_list:
  print(lst)
  for word in lst:
    print(word)
    if word != "Codezilla":
      continue
    else:
      print("Found Codezilla!")
      exit() # EXIT THE WHOLE PROGRAM

# Solution 3: checking for words with in and exit the loop with break (the best solution)
for lst in nested_list:
  print(lst)
  if "Codezilla" in lst:
    print("Found Codezilla!")
    break # EXIT THE LOOP ONLY