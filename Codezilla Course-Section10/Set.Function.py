

#lesson_project#######################################################

name = 'iiiiisssslllaaammmm'
unique_set = set(name)
print(unique_set)
unique_lst = list(unique_set)
print(tuple(unique_lst))
print(unique_lst)
print(*unique_lst, sep=',')

print(set(name))

for i in set(name):
  print(i)


#project1#################################################

from random import randint

random_lst = []

for _ in range(1000): # _ means we don't need a return from it
  random_lst.append(randint(1,1000))  
#print(random_lst)

unique_set = set(random_lst)

sum_unique_set = sum(unique_set)
lenght_unique_set = len(unique_set)
average_unique_set = sum_unique_set/lenght_unique_set
print(f'The sum of the unique numbers is: ({sum_unique_set}) and the average is: ({average_unique_set:,.2f})')
print('--------------------------------------------------------')
sum_random_lst = sum(random_lst)
lenght_random_lst = len(random_lst)
average_random_lst = sum_random_lst/lenght_random_lst
print(f'The sum of the random list is: ({sum_random_lst}) and the average of the random list is: ({average_random_lst:,.2f})')


