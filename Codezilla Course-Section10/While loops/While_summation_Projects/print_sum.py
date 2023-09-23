
total = 0

while True:
  num = input('Enter a number: ')
  if num == 'done' or num == '':
    break
  if int(num) % 2 == 0:
    continue
  total += int(num)
print(total)