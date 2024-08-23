#90-100---A
#80-90----B
#70-80----C
#60-70----D
#0-60----F

print(f"Please enter scores between 0 and 100 \n{'-'*20}")

arabic_score = float(input('Enter Arabic score: '))
english_score = float(input('Enter English score: '))
math_score = float(input('Enter Math score: '))
physics_score = float(input('Enter Physics score: '))
chemistry_score = float( input('Enter Chemistry score: '))
biology_score = float(input('Enter biology score: '))


total_score = (arabic_score + english_score + math_score + physics_score + chemistry_score + biology_score)/6
#score_percent = (total_score/600)*100 = total_score/6   الحل بتاعي

if not (0 <=total_score<=100):
  grade = None
  print('Please Enter scores again from 0 to 100')
elif total_score >=90:
  grade = 'A'
elif total_score >=80:
  grade = 'B'
elif total_score >=70:
  grade = 'C'
elif total_score >=60:
  grade = 'D'
else:
  grade = 'F'

if grade != None:
  print(f"{'-'*20} \nYour score is {total_score:.2f}% \nYour grade is {grade}")

