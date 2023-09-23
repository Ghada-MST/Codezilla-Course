first_number = int(input ("enter first number: "))
second_number = int(input ("enter second number: "))
operator = input ("what is the opertation?")
statment = ""
result = 0
if operator == "+":
 result = first_number + second_number
 statment = "the addition result is "
elif operator == "-":
 result = first_number - second_number
 statment = "the subtraction result is "
elif operator == "*":
 result = first_number * second_number
 statment = "the multiplication result is "
elif operator == "/":
 result = first_number / second_number
 statment = "the division result is "
else:
 result = ""
 statment = "sorry i don't understand"

print (statment+ str(result))