
#list of available vegetables
vegetables = ['broccoli', 'eggplant', 'carrot', 'cabbage', 
'cucumber', 'potato', 'garlic', 'pepper']

vege_join = ', '.join(vegetables[:-1])
vege_str = vege_join + ' and ' + vegetables[-1]

print('Welcome at Codezilla vegetables!')

vege = input('Enter the vegetable you want to get: ')

print('-'*30)

if vege.lower() in vegetables:
  amount = input('Enter the amount in kg: ')
  print(f'We will get you {amount} kg of {vege} very soon.')
else:
  print(f'''Sorry we only have
{vege_str}''')

