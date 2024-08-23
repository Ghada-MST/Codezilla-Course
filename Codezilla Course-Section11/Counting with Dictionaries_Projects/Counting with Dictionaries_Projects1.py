
#project1###############################################
txt = '''welcome to codezilla course
we are happy to have all you here
hope you enjoy the course'''

letter_counter = {}


for letter in txt:
  if letter in letter_counter:
    letter_counter[letter] += 1

  else:
    letter_counter[letter] = 1

print(letter_counter)  



#project2###############################################
txt = '''welcome to codezilla course
we are happy to have all you here
hope you enjoy the course'''


letter_counter = {}

for letter in txt:
  
  letter_counter[letter] = letter_counter.get(letter,0) +1

    
print(letter_counter)



#project3###############################################
txt = '''welcome to codezilla course
we are happy to have all you here
hope you enjoy the course'''


letter_counter = {}

for letter in txt:
  #another answer
  #letter_counter.setdefault(letter,0)
  #letter_counter[letter] +=1
  letter_counter[letter] = letter_counter.setdefault(letter,0) +1

print(letter_counter)