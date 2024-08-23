

#project1###############################################
txt = """One of the most effective ways to reduce the friction 
associated with
your habits is to practice environment design
In a previous chapter we discussed environment design as a 
method for making cues more
obvious but you can also optimize your environment to make 
actions
easier
For example when deciding where to practice a new habit it is
best to choose a place that is already along the path of your 
daily
routine
Habits are easier to build when they fit into the flow of your
life 
You are more likely to go to the gym if it is on your way to 
work
because stopping does not add much friction to your lifestyle
"""
txt_counter = {}

for letter in txt.lower():
  if letter !=' ' and letter !="\n":
    if letter not in txt_counter: 
      txt_counter[letter] = 1

    else:
      txt_counter[letter]+=1

for letter,count in txt_counter.items():
  print(f'{letter.upper()} : {count}')

#another answer مهندس اسلام############
txt = """One of the most effective ways to reduce the friction 
associated with
your habits is to practice environment design
In a previous chapter we discussed environment design as a 
method for making cues more
obvious but you can also optimize your environment to make 
actions
easier
For example when deciding where to practice a new habit it is
best to choose a place that is already along the path of your 
daily
routine
Habits are easier to build when they fit into the flow of your
life 
You are more likely to go to the gym if it is on your way to 
work
because stopping does not add much friction to your lifestyle
"""
# make the string lower case and remove the new line and spaces
txt = txt.lower().replace("\n","").replace(" ","")
# create an empty dictionary to store the letters
letter_count = {}
# loop through the string
for letter in txt:
# check if the letter is not in the dictionary
  if letter not in letter_count:
# if the letter is not in the dictionary add it and set the value to 1
    letter_count[letter] = 1
  else:
# if the letter is in the dictionary add 1 to the value
    letter_count[letter] += 1
# print the dictionary
for letter, count in letter_count.items():
  print(f"{letter.title()}: {count}")


#project2#######by get method########################################
txt = """One of the most effective ways to reduce the friction 
associated with
your habits is to practice environment design
In a previous chapter we discussed environment design as a 
method for making cues more
obvious but you can also optimize your environment to make 
actions
easier
For example when deciding where to practice a new habit it is
best to choose a place that is already along the path of your 
daily
routine
Habits are easier to build when they fit into the flow of your
life 
You are more likely to go to the gym if it is on your way to 
work
because stopping does not add much friction to your lifestyle
"""
txt = txt.lower().replace(' ','').replace('\n','')
txt_counter = {}

for letter in txt:
  txt_counter[letter] = txt_counter.get(letter,0) +1

print(txt_counter)


#project3##########by setdefault method#####################################
txt = """One of the most effective ways to reduce the friction 
associated with
your habits is to practice environment design
In a previous chapter we discussed environment design as a 
method for making cues more
obvious but you can also optimize your environment to make 
actions
easier
For example when deciding where to practice a new habit it is
best to choose a place that is already along the path of your 
daily
routine
Habits are easier to build when they fit into the flow of your
life 
You are more likely to go to the gym if it is on your way to 
work
because stopping does not add much friction to your lifestyle
"""
txt = txt.lower().replace(' ','').replace('\n','')
txt_counter = {}

for letter in txt:
  txt_counter.setdefault(letter,0)
  txt_counter[letter]+=1
print(txt_counter)


#project4##############by get method#################################
txt = """One of the most effective ways to reduce the friction 
associated with
your habits is to practice environment design
In a previous chapter we discussed environment design as a 
method for making cues more
obvious but you can also optimize your environment to make 
actions
easier
For example when deciding where to practice a new habit it is
best to choose a place that is already along the path of your 
daily
routine
Habits are easier to build when they fit into the flow of your
life 
You are more likely to go to the gym if it is on your way to 
work
because stopping does not add much friction to your lifestyle
"""

word_counter={}

txt_lst = txt.lower().split()

for word in txt_lst:
  word_counter[word] = word_counter.get(word,0)+1

for word,count in word_counter.items():
  print(f'{word.title()}:{count}')

#project4###################by setdefault method#############################
txt = """One of the most effective ways to reduce the friction 
associated with
your habits is to practice environment design
In a previous chapter we discussed environment design as a 
method for making cues more
obvious but you can also optimize your environment to make 
actions
easier
For example when deciding where to practice a new habit it is
best to choose a place that is already along the path of your 
daily
routine
Habits are easier to build when they fit into the flow of your
life 
You are more likely to go to the gym if it is on your way to 
work
because stopping does not add much friction to your lifestyle
"""

word_counter={}

txt_lst = txt.lower().split()

for word in txt_lst:
  word_counter[word] = word_counter.setdefault(word,0)+1
  #word_counter.setdefault(word,0)
  #word_counter[word] +=1
for word,count in word_counter.items():
  print(f'{word.title()}:{count}')



#project 5 and 6 ###############################################
february_shopping_list = {
1: ['meat', 'chicken', 'chicken', 
 'chicken', 'bread', 'chocolate', 'meat'], 
2: ['bread', 'milks', 'butter', 'butter', 'chocolate'], 
3: ['butter', 'meat', 'milks'], 
4: ['butter', 'bread', 'nuts'], 
5: ['butter', 'bread', 'chocolate', 'chocolate'], 
6: ['nuts', 'butter', 'butter', 
 'butter', 'chocolate', 'butter'], 
7: ['cheese', 'milks', 'butter', 'nuts'], 
8: ['cheese', 'meat', 'nuts', 'yoghurt', 'cheese'], 
9: ['chocolate', 'milks', 'milks', 
 'chocolate', 'milks', 'eggs', 'meat'], 
10: ['yoghurt', 'butter', 'chocolate', 'cheese', 'butter'], 
11: ['cheese', 'meat', 'yoghurt'], 
12: ['eggs', 'chocolate', 'meat', 'eggs', 'butter'], 
13: ['bread', 'eggs', 'yoghurt', 
 'yoghurt', 'chicken', 'chocolate'], 
14: ['milks', 'meat', 'meat'], 
15: ['meat', 'chicken', 'butter', 'nuts', 'nuts'], 
16: ['meat', 'meat', 'chicken']
}

items_prices = {
'meat': 250,
'chicken': 140,
'bread': 10,
'chocolate': 20,
'milks': 42,
'butter': 75,
'nuts': 90,
'cheese': 65,
'yoghurt': 25,
'eggs': 120
}

shopping_dict = {}
total_price = 0
for day,products in february_shopping_list.items():
  for item in products:
    #shopping_dict[item] = shopping_dict.get(item,0)+1
    shopping_dict.setdefault(item,0)
    shopping_dict[item] +=1
    
for item,quantity in shopping_dict.items():

  total_price_item = items_prices.get(item)*quantity
  total_price += total_price_item
  print(f'{item.title()} : Quantity is {quantity} and Total price is {total_price_item:,}')
  print('-----------------------------------------------')
print(f'The total money spent this month is {total_price:,}')

#another answer مهندس اسلام

# create an empty dictionary to store the items and their count
items_count = {}
# loop through the dictionary
for day, items in february_shopping_list.items():
# loop through the list of items
  for item in items:
# get the value and add 1 to it
    items_count[item] = items_count.get(item, 0) + 1
# create an empty dictionary to store the items and their cost
item_cost = {}
# loop through the dictionary
for item, count in items_count.items():
# add the item and its cost to the dictionary
  item_cost[item] = count * items_prices[item]
# print the total cost of the items
for item, cost in item_cost.items():
  print(f'{item.title()}: {cost:,} EGP')
# print the total cost of the items
total_cost = sum(item_cost.values())
print(f'The Total Cost: {total_cost:,} EGP')