first_number = int(input ("enter first number: "))
second_number = int(input ("enter second number: "))
third_number = int(input ("enter third number: "))
if first_number > second_number:
  if first_number > third_number:
    print("the greatest number is " + str(first_number))
  else:
    print("the greatest number is " + str(third_number))
else:
   if second_number > third_number:
    print ("the greatest number is " + str(second_number))
   else:
    print("the greatest number is " + str(third_number))