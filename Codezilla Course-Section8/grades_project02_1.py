
#BMI = MASS/HEIGHT^2 = KG/M2


#BMI 35 to 40 extreme obese
#BMI 30 to 35 obese
#BMI 25 to 30 is overweight
#BMI 18.5 to 25 normal
#BMI < 18.5 underweight

height_cm = float(input('Enter height in cm: '))
weight = float(input('Enter weight in kg: '))

#calculate BMI

height_meter_square = (height_cm /100)**2
BMI = weight/height_meter_square

#classification

if BMI >= 35:
  classification = 'extreme obese'
elif BMI >=30:
  classification = 'obese'
elif BMI >= 25 :
  classification = 'overweight'
elif BMI >= 18.5 :
  classification = 'normal'
else: 
  classification = 'underweight'

print(f'{"-"*20} \nYour BMI is {BMI:.2f} which is considered as {classification.title()}')