students = {
  "Mohamed": {"grades": {
  "math": 100,
  "english": 90,
  "science": 80,
  "arabic": 100, 
  "history": 97},
  "school": "Codezilla"
},
  "Ahmed": {"grades": {
  "math": 100,
  "english": 95,
  "science": 93,
  "arabic": 100,
  "history": 94},
  "school": "Codezilla"
},
  "Ali": {"grades": {
  "math": 85,
  "english": 83,
  "science": 87,
  "arabic": 100,
  "history": 90},
  "school": "Al-Azhar"
}
}
total_ahmed_grades = 0
for student in students:
  if student == 'Ahmed':
    students_grades = students[student]['grades']
    for subject, grade in students_grades.items():
      total_ahmed_grades += grade
    break   

print(f'Ahmed got {total_ahmed_grades}')