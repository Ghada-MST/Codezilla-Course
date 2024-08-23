students = {
    "Mohamed Hassan": {
        "grades": {
            "math": 100,
            "english": 90,
            "science": 80,
            "arabic": 100,
            "history": 97
        },
        "school": "Codezilla"
    },
    "Ahmed Kamal": {
        "grades": {
            "math": 100,
            "english": 95,
            "science": 93,
            "arabic": 100,
            "history": 94
        },
        "school": "Codezilla"
    },
    "Ali Adel": {
        "grades": {
            "math": 85,
            "english": 83,
            "science": 87,
            "arabic": 100,
            "history": 90
        },
        "school": "Al-Azhar"
    },
    "Hossam Yehia": {
        "grades": {
            "math": 100,
            "english": 94,
            "science": 98,
            "arabic": 100,
            "history": 100
        },
        "school": "Al-Azhar"
    }
}

student_name = "name"
max_percentage = 0
for student, information in students.items():
  percentage = sum(information["grades"].values()) / len(information["grades"])
  if percentage > max_percentage:
    max_percentage = percentage
    student_name = student

print(
    f'{student_name} has the highest total percentage which is {max_percentage:.2f}%'
)
print('*' * 50)
for subject, grade in students[student_name]['grades'].items():
  print(f'{subject.title()} : {grade}')

#####another answer#################

students = {
    "Mohamed Hassan": {
        "grades": {
            "math": 100,
            "english": 90,
            "science": 80,
            "arabic": 100,
            "history": 97
        },
        "school": "Codezilla"
    },
    "Ahmed Kamal": {
        "grades": {
            "math": 100,
            "english": 95,
            "science": 93,
            "arabic": 100,
            "history": 94
        },
        "school": "Codezilla"
    },
    "Ali Adel": {
        "grades": {
            "math": 85,
            "english": 83,
            "science": 87,
            "arabic": 100,
            "history": 90
        },
        "school": "Al-Azhar"
    },
    "Hossam Yehia": {
        "grades": {
            "math": 100,
            "english": 94,
            "science": 98,
            "arabic": 100,
            "history": 100
        },
        "school": "Al-Azhar"
    }
}
all_percentages = {}

for student in students:
  student_grades = students[student]['grades']
  total_student_grades = sum(student_grades.values())
  len_subjects = len(students[student]['grades'])
  percentage = total_student_grades / len_subjects
  all_percentages[student] = percentage

max_percentage = max(all_percentages.values())
information_ranking = [student for student, percentage in all_percentages.items() if percentage == max_percentage]

print(
    f'{information_ranking[0]} has the highest total percentage which is {max_percentage:.2f}%'
)
print('*' * 50)
for subject, grade in students[information_ranking[0]]['grades'].items():
  print(f'{subject.title()} : {grade}')

#####another answer#################
students = {
    "Mohamed Hassan": {
        "grades": {
            "math": 100,
            "english": 90,
            "science": 80,
            "arabic": 100,
            "history": 97
        },
        "school": "Codezilla"
    },
    "Ahmed Kamal": {
        "grades": {
            "math": 100,
            "english": 95,
            "science": 93,
            "arabic": 100,
            "history": 94
        },
        "school": "Codezilla"
    },
    "Ali Adel": {
        "grades": {
            "math": 85,
            "english": 83,
            "science": 87,
            "arabic": 100,
            "history": 90
        },
        "school": "Al-Azhar"
    },
    "Hossam Yehia": {
        "grades": {
            "math": 100,
            "english": 94,
            "science": 98,
            "arabic": 100,
            "history": 100
        },
        "school": "Al-Azhar"
    }
}
all_percentages = {}

for student in students:
  student_grades = students[student]['grades']
  total_student_grades = sum(student_grades.values())
  len_subjects = len(students[student]['grades'])
  percentage = total_student_grades / len_subjects
  all_percentages[student] = percentage

max_percentage = max(all_percentages.values())
information_ranking = "student"
for student, percentage in all_percentages.items():
  if percentage == max_percentage:
    information_ranking = student
    break

print(
    f'{information_ranking} has the highest total percentage which is {max_percentage:.2f}%'
)
print('*' * 50)
for subject, grade in students[information_ranking]['grades'].items():
  print(f'{subject.title()} : {grade}')

#####another answer#################

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
    "Hossam Yehia": {"grades": { 
        "math": 100, 
        "english": 94, 
        "science": 98, 
        "arabic": 100, 
        "history": 100}, 
        "school": "Al-Azhar" 
    } 
} 
all_percentages = {}

for student in students:
  student_grades = students[student]['grades']
  total_student_grades = sum(student_grades.values())
  len_subjects = len(students[student]['grades'])
  percentage = total_student_grades/len_subjects
  all_percentages[student] = percentage


max_percentage = 0
information_ranking = "student"
for student, percentage in all_percentages.items():
  if percentage > max_percentage:
    max_percentage = percentage
    information_ranking = student
    
print(f'{information_ranking} has the highest total percentage which is {max_percentage:.2f}%')
print('*'*50)
for subject, grade in students[information_ranking]['grades'].items():
  print(f'{subject.title()} : {grade}')