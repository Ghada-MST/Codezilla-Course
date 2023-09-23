
print('It is the time to see height differently 😃')

height = float(input('Enter the height in cm: '))

if height >= 200:
  classification = ('very tall')
elif 180 <= height < 200:
  classification = ('tall')
elif height >= 160 and height < 180:
  classification = ('normal')
elif 150 <= height < 160:
  classification = ('short')
else:
  classification = ('very short')
print(f'{"-"*30} \n{height} cm is considered {classification}')