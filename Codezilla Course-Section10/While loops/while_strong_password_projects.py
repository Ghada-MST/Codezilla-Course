#project1

import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

password_lenght = int(input('Enter the number of the characters in the password: '))

password = ''

while len(password) < password_lenght:
  random_character = random.choice(characters)
  password += random_character #the last character already get out from the loop 10 when it return up to the beginig of the loop it will stop cause 10 <10 give false value

print('The generated password is : ',password)

#project2

import string
import random

characters = string.ascii_uppercase + string.digits + string.punctuation

password_lenght = int(input('Enter the number of the characters in the password: '))

password = ''

while len(password) < password_lenght:
  random_character = random.choice(characters)
  password += random_character

print('The generated password is : ',password)


#project3


import string
import random

password_lenght = int(input("Enter the number of the characters in the password:  "))

characters = string.ascii_letters + string.digits + string.punctuation



letters_count = (password_lenght//2) + (password_lenght%2)

i = 0
letter_lst = []
while i < letters_count:
  random_letters = random.choice(string.ascii_letters)
  letter_lst.append(random_letters) 
  i+=1


password_lst = []
while letters_count < password_lenght:
  random_characters = random.choice(characters)
  password_lst += random_characters
  letters_count += 1
  

password_lst.extend(letter_lst)


random.shuffle(password_lst)
password = ''.join(password_lst)

print('The generated password is : ',password)


random.shuffle(password_lst)
password = ''.join(password_lst)

print('The generated password is : ',password)



#project3 >>>>>>>>>>>>>> another way to import modules

from string import *
from random import  choice, shuffle

characters = ascii_letters + digits + punctuation

password_lenght = int(input("Enter the number of the characters in the password:  "))

letters_count = (password_lenght//2) + (password_lenght%2)

i = 0
letter_lst = []
while i < letters_count:
  random_letters = choice(ascii_letters)
  letter_lst.append(random_letters) 
  i+=1


half_password = []
while letters_count < password_lenght:
  random_characters = choice(characters)
  half_password += random_characters
  letters_count += 1
  

password_lst = letter_lst + half_password 


shuffle(password_lst)
password = ''.join(password_lst)

print('The generated password is : ',password)


#project3>>>>>>>>>>> حل مهندس اسلام

import random
import string
# Get the desired password length from the user
length = int(input("Enter the desired password length: "))
# Define the characters that can be used in the password
characters = string.ascii_letters + string.digits + string.punctuation
# Define the number of letters in the password
letter_count = length // 2 + length % 2 # we add 1 if the length is odd
# Generate the password
password = []
# Add the letters to the password
i = 0
while i < letter_count:
password.append(random.choice(string.ascii_letters))
i += 1
# Add the other characters to the password
while len(password) < length:
password.append(random.choice(characters))
# Shuffle the password
random.shuffle(password)
# Convert the password to a string
password = "".join(password)
# Print the generated password
print(f"Generated password: {(password)}")