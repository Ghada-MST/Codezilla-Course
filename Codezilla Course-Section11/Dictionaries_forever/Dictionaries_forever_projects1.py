#Project1######################################################
students = {
"Mohamed Hassan": {"grades": {
"math": 100,
"english": 90,
"science": 80,
"arabic": 100, 
"history": 97},
"school": "Codezilla"
},
"Ahmed Kamal": {"grades": {
"math": 100,
"english": 95,
"science": 93,
"arabic": 100,
"history": 94},
"school": "Codezilla"
},
"Ali Adel": {"grades": {
"math": 85,
"english": 83,
"science": 87,
"arabic": 100,
"history": 90},
"school": "Al-Azhar"
},
"Sara Ahmed": {"grades": {
"math": 100,
"english": 94,
"science": 98,
"arabic": 100,
"history": 100},
"school": "Al-Azhar"
}
}
for student in students:
  student_grades = students[student]['grades']
  student_school = students[student]["school"]
  print(f'''Student name: {student}
School: {student_school}
Grades: ''')
  for subject, grade in student_grades.items():
    print(f'{subject.title()} : {grade}')
    
  print("-"*30) 





#Project2######################################################

students2 = {
    "Mohamed Hassan": {"grades": {
    "math": 100,
    "english": 90,
    "science": 80,
    "arabic": 100, 
    "history": 97},
    "school": "Codezilla"
    },
    "Ahmed Kamal": {"grades": {
    "math": 100,
    "english": 95,
    "science": 93,
    "arabic": 100,
    "history": 94},
    "school": "Codezilla"
    },
    "Ali Adel": {"grades": {
    "math": 85,
    "english": 83,
    "science": 87,
    "arabic": 100,
    "history": 90},
    "school": "Al-Azhar"
    },
    "Sara Islam": {"grades": {
    "math": 100,
    "english": 94,
    "science": 98,
    "arabic": 100,
    "history": 100},
    "school": "Al-Azhar"
}
}

for student in students2:
  student_grades = students2[student]['grades']
  total_grade_student = 0
  num_of_subjects = 0
  for subject, grade in student_grades.items():
    total_grade_student += grade
    num_of_subjects += 1
  percentage = total_grade_student/num_of_subjects
  print(f'{student}\'s total percentage is {percentage:.2f}% ')
  print('*'*30)


#another answerمهندس اسلام  

for student in students2:
  student_grades = students2[student]['grades']
  total_grades = sum(student_grades.values())
  len_subjects = len(student_grades)
  percentage = total_grades/len_subjects
  print(f'{student}\'s total percentage is {percentage:.2f}%')
  print('*'*30)



  
#Project3######################################################

students = {
"Mohamed Hassan": {"grades": {
"math": 100,
"english": 90,
"science": 80,
"arabic": 100, 
"history": 97}
},
"Ahmed Kamal": {"grades": {
"math": 100,
"english": 95,
"science": 93,
"arabic": 100,
"history": 94}
},
"Ali Adel": {"grades": {
"math": 85,
"english": 83,
"science": 87,
"arabic": 100,
"history": 90}
},
"Israa Ali": {"grades": {
"math": 100,
"english": 94,
"science": 98,
"arabic": 100,
"history": 100}
}
}

student_name = input("Please, Enter the name of the student: ").title()
not_found = True


for student in students:
  if student == student_name:
    student_grades = students[student]['grades']
    total_student_grades = sum(student_grades.values())
    len_student_grades = len(student_grades)
    percentage = total_student_grades/len_student_grades
    not_found = False
    
    print(f'\n{student} got the following grades: ')
    
    for subject, grade in student_grades.items():
      print(f'{subject.title()}: {grade}')
    print('*'*30)
    print(f"\n{student}'s total percentage is {percentage:.2f}%")

if not_found:
  print("\nSorry, we don't have info about this student.")
      

#another answer مهندس اسلام

student_name = input("Please, Enter the name of the student: ").title()

if student_name not in students:
  print("Sorry, we don't have info about this student.")
  exit()

student_grades = students[student_name]['grades']
total_grades = sum(student_grades.values())
len_subjects = len(student_grades)
percentage = total_grades/len_subjects

print(f'\n{student_name} got the following grades: ')

for subject, grade in student_grades.items():
  print(f'{subject.title()}: {grade}')

print('*'*30)
print(f"\n{student_name}'s total percentage is {percentage:.2f}%")