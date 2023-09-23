
import time
import random

words = [
'have', 'that', 'they', 'with', 'this', 'from', 'which', 'would', 'will', 
'there',
'make', 'when', 'more', 'other', 'what', 'time', 'about', 'than', 'into', 
'could', 
'state', 'only', 'year', 'some', 'take', 'come', 'these', 'know', 'like', 
'then', 
'first', 'work', 'such', 'give', 'over', 'think', 'most', 'even', 'find', 
'also', 
'after', 'many', 'must', 'look', 'before', 'great', 'back', 'through', 
'long', 
'where', 'much', 'should', 'well', 'people', 'gouda', 'just', 'because', 
'good', 
'each', 'those', 'feel', 'seem', 'high', 'place', 'little', 'world', 
'very', 'still', 
'nation', 'hand', 'life', 'tell', 'write', 'become', 'here', 'show', 
'house', 'both', 
'between', 'need', 'mean', 'call', 'develop', 'under', 'last', 'right', 
'move', 'thing', 
'general', 'school', 'never', 'same', 'another', 'begin', 'while', 
'number', 'part', 
'turn', 'real', 'leave', 'might', 'want', 'point', 'form', 'child', 
'small', 'since', 
'against', 'late', 'home', 'interest', 'large', 'person', 'open', 
'public', 'follow', 
'during', 'present', 'without', 'again', 'hold', 'codezilla', 'govern', 
'around', 
'head', 'consider', 'word', 'program', 'problem', 'however', 'lead', 
'system', 
'order', 'plan', 'keep', 'face', 'group', 'play', 'stand', 'increase', 
'early', 'course', 'change', 'help', 'line', 'possible', 'fact', 'down'
]


word_index = random.randint(0,len(words)-1)
word = words[word_index]
word_lst = list(word)
word_lst.reverse()
reversed_word = ''.join(word_lst)

print(f'''Welcome to the Reversed words game! 
{'-'*35}''')

start_time = time.time()
print(f'''The reversed word is: {reversed_word}
{'-'*35}''')

guess = input('Guess the word: ')
end_time = time.time()

time = end_time - start_time

print('-'*35)

حل غادة

if guess == word:
  if time < 5:
    print('You Won!')
  else:
    print('''You took too long!
You lost!''')

else: 
    print('''Wrong Word!
You lost!''')

حل مهندس اسلام 
# check the guess
if guess == word and answer_time < 5:
print('You won!')
else:
if guess != word:
print('Wrong word!')
if answer_time >= 5:
print('You took too long!')
print('You lost!')



حل اخر

if guess == word and time < 5:
  print('You Won!')
else:
  if guess != word:
    msg = 'Wrong Word!'
  if time >= 5:
    msg = 'You took too long!'
    
  print(f'''{msg}
You lost!''')

حل تالت

abbreviation_for_lost = True

word_save = 'Wrong Word'

if guess == word : 
    word_save  = 'You took too long!' 
    if time < 5:
        abbreviation_for_lost = False               
        print('You won!')

if abbreviation_for_lost:
    print(f'{word_save} You lost!')
