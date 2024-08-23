
name = input("Enter your name: ").strip().lower()

winners = ['mohamed','ahmed','mahmoud','esraa','islam','hassan','sedra','tamim']

if name in winners:
  print(f'Congratulation {name} is a winner!!!🥳🥳🥳')
else:
  print(f'Sorry {name} is not a winner!😔😔😔')