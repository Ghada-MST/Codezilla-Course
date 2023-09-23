



#project1#######################################################

nums = [num for num in range(20,141) if num%3==0]
sum_nums = sum(nums)
print('The numbers are') 
print(*nums,sep=", ")
print(f'The sum of them is: {sum_nums}')

#project2#######################################################

from random import randint,choice

random_nums = [randint(100,1000) for _ in range(20)]
print(random_nums)

#project3#######################################################

nums_3_5 = [num for num in range(100,10_001) if (num%3==0 and num%5==0)]
random_nums = [choice(nums_3_5) for _ in range(100)]
print(random_nums)

#project4#######################################################

# list of words
words = [
'have', 'that', 'they', 'with', 'this', 'from',
'which', 'would', 'will', 'there',
'make', 'when', 'more', 'other', 'what', 'time',
'about', 'than', 'into', 'could',
'state', 'only', 'year', 'some', 'take', 'come',
'these', 'know', 'like', 'then',
'first', 'work', 'such', 'give', 'over', 'think',
'most', 'even', 'find', 'also',
'after', 'many', 'must', 'look', 'before', 'great',
'back', 'through', 'long',
'where', 'much', 'should', 'well', 'people', 'gouda',
'just', 'because', 'good',
'each', 'those', 'feel', 'seem', 'high', 'place',
'little', 'world', 'very', 'still',
'nation', 'hand', 'life', 'tell', 'write', 'become'
]

words_upper = [word.upper() for word in words]
print(words_upper)

#project5#######################################################
words = [["Hello", "from", "Codezilla"],
["Python", "Course", "is", "awesome"],
["I", "enjoy", "learning", "Python", "with", "Codezilla"]]

words_string = [' '.join(lst) for lst in words]
print(words_string)
words_modified = [word.upper().replace(' ','-') for word in words_string]
print(words_modified)


#project6#######################################################

nums = [44, 64, -12, 0, -5, 34, -55, 67, -88, -99]

nums_positive = [abs(num) for num in nums ]
print(nums_positive)




#project7#######################################################
nested_list = [["Hello", "from", "Codezilla"],
["Python", "Course", "is", "awesome"],
["I", "enjoy", "learning", "Python", "with", "Codezilla"]]

nested_list_modified = [word for lst in nested_list for word in lst]

print(nested_list_modified)

#project8#######################################################

words = ["Hello", "from", "Codezilla", "Python", "Course"]
# Output example: [('Hi', 2), ('Python', 6)]
words_lenght = [len(word)for word in words]
print(words_lenght)
words_tuple = [(len,word)for len,word in zip (words,words_lenght)]
print(words_tuple)