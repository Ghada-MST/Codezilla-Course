# 90 - 100   A      امتياز
# 80-90       B      جيد جدا
# 70-80       C     جيد
# 60-70       D       مقبول
# 0-60        F      راسب

score = float(input('Enter your score from 0 to 100: '))

if not (0<=score<=100):
  grade = None
  print('Please enter your score from 0 to 100')
elif score >= 90:
  grade = 'A'
elif score >= 80:
  grade = 'B'
elif score >= 70:
  grade = 'C'
elif score >= 60:
  grade = 'D'
else:
  grade = 'F'

if grade is not None:
  print(f'Your score is {score} and your grade is {grade}')