#recursion
def EvenNums(num):
  print(num)
  if num % 2 ==1 :
    print("please enter an even num")
  elif num == 2:
    return num
  else:
    return EvenNums(num-2)


EvenNums(15)
