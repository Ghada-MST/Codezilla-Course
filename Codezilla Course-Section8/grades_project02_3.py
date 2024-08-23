extremely_hot = 'When the degree is 40 or more \nWe could say that the weather is etremely hot \nWe should avoid the direct exposure to the sun'

very_hot = 'when the degree is 30 or more \nWe could say that the weather is very hot \nWe should be careful about the direct exposure to the sun'

moderate = 'When the degree is between 20 and 30 \nWe could say that we have good weather'

cold = 'When the degree is between 10 and 20 \nWe could say that we have cold weather'

very_cold = 'When the degree is between 0 and 10 \nWe could say that we have very cold weather \nWe should go with pretty heavy clothes'

extremely_cold = 'When the dgree is less than 0 \nWe could say that we have extremely cold weather \nWe should avoid getting out as possible'


print(f'Let\'s see how we could deal with the weather😃 \n{"-"*20}')

degree = float(input('Enter the degree in Celsius: '))

print(f'{"-"*20}')

if degree >= 40:
  print(extremely_hot)
elif degree >= 30:
  print(very_hot)
elif degree >= 20:
  print(moderate)
elif degree >= 10:
  print(cold)
elif degree >= 0:
  print(very_cold)
else:
  print(extremely_cold)