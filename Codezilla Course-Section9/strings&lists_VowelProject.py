
word = input('enter a word: ')

answer = input(f'''Does the word start with a vowel? 🤔🤔🤔
''').lower()

print('-'*30)

vowels = 'aeiou'

first_letter = word[0].lower()

if (answer == 'yes') and (first_letter in vowels):
  print(f'''Bravo!🎉🎉🎉
{word} starts with a vowel🥳🥳🥳''')


elif (answer == 'no') and (first_letter not in vowels):
  print(f'''Bravo!🎉🎉🎉
{word} doesn't start with a vowel🥳🥳🥳''')


else:
  print("let's try again😃😃😃")