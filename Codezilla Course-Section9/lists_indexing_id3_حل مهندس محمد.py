#a list of students’ ids
students = [
# Codezilla school
['1100', '1101', '1102', '1103', '1104',
'1105', '1106', '1107', '1108', '1109'],
# Al Dorra school
['2100', '2101', '2102', '2103', '2104',
'2105', '2106', '2107', '2108', '2109'],
# Mostafa Kamel school
['3100', '3101', '3102', '3103', '3104',
'3105', '3106', '3107', '3108', '3109']
]
schools = ['Codezilla school','Al Dorra school','Mostafa Kamel school']

student_id = input('Enter student id: ')

print('-'*50)

if student_id in students[0]:
  school_name = schools[0]
elif student_id in students[1]:
  school_name = schools[1]
elif student_id in students[2]:
  school_name = schools[2]
else:
  school_name = None
  print('Sorry, student is not in our records')
  
if school_name != None:
  print(f'Student is in {school_name}')