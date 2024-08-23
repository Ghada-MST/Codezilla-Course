
students={
  'Mohamed':{
    'grades':{
      'math':100,
      'science':80,
      'english':90,
      'arabic':100
    },
    'age':20
  },
'Ahmed':{
    'grades':{
      'math':90,
      'science':80,
      'english':80,
      'arabic':100
    },
    'age':20
  }
}
sum_mohamed_grades = students['Mohamed']['grades']['math'] + students['Mohamed']['grades']['science']+ students['Mohamed']['grades']['arabic']+ students['Mohamed']['grades']['english']

len_mohamed_grades = len(students['Mohamed']['grades'])

average_mohamed_grades = sum_mohamed_grades/len_mohamed_grades

print(average_mohamed_grades)

sum_ahmed_grades = students['Ahmed']['grades']['math'] + students['Ahmed']['grades']['science']+ students['Ahmed']['grades']['arabic']+ students['Ahmed']['grades']['english']

len_ahmed_grades = len(students['Ahmed']['grades'])

average_ahmed_grades = sum_ahmed_grades/len_ahmed_grades

print(average_ahmed_grades)   
