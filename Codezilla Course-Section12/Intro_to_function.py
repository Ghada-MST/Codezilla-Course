

#project1################################################################
def greet(name):
  print(f"Welcome {name} at Codezilla Python Course Enjoy your Learning Journey")

username = input("Please enter your name: ").title()
#Please enter your name: mohamed gouda 
#Welcome Mohamed Gouda at Codezilla Python Course Enjoy your Learning Journey 
greet(username)


#project2################################################################
# Make a function that takes text and print it in reverse order and lower case

def reverso(word):
  print(word[::-1].lower())

user_input = input("Enter your text: ")
reverso(user_input)

