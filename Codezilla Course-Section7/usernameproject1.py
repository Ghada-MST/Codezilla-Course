#get name form the user
name = input("enter your name: ").strip().title()

#remove extra spaces around name
#replace spaces with under scores
#make all letters small
#replace a with aaa
#add '@codezilla.com'at the end of the user name
user_name = name.replace("a","aaa").lower().replace(" ","_")
#greet user
print(f"Hello, {name}")
#print user name
print(f'Your user name is \n{user_name}@codezilla.com')