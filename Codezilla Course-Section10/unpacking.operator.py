#project1#######################################
student_names = ["Mohamed", "Ahmed", "Ali", "Sara"]
student_grades = [[96, 78, 82, 80], [86, 92, 98, 90], 
[76, 88, 90, 72], [78, 86, 98, 88]]


for name, grade in zip(student_names,student_grades):
  average_grade = sum(grade)/len(grade)
  print("Student:", name)
  print("Grades:")
  print(*grade, sep=', ')
  print(name, "has an average grade of", average_grade)
  print("-"*40)


#project2#######################################
# make these lists into one list using unpacking operator
grades1 = [96, 78, 82, 80]
grades2 = [86, 92, 98, 90]
grades3 = [76, 88, 90, 72]
grades4 = [78, 86, 98, 88]

total_grades=[*grades1,*grades2,*grades3,*grades4]
print(total_grades)
