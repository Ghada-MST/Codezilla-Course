
nested_nums = [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [21, 22, 23, 24, 25],
                18, 19, 20]

num = float(22)
if num in nested_nums:
    print('hello')

names = ['timo', 'soso', 'fofo', 'rery' ,'samy']
name = 'islam'

if name in names:
  print('yes')
else:
  print('no')


print(22.0 == 22)

# lst = []
# print(lst[0])

nested_nums = [
    0, 
    [1, [2, 3], 4, 5],
    [6, 7, [8, 9], 10],
    [11, 12, 13, 14, 15],
    16, [17, 18], 19, 20
]
print(nested_nums[-3][-2])
print(nested_nums[2][2][0])
print(nested_nums[0])
print(nested_nums[3][1])
print(nested_nums[-4])
print(nested_nums[1][-1])
print(nested_nums[-5][2])
print(nested_nums[1][1][1])