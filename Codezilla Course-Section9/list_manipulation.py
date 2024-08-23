names = ['mohamed','hany','ramez','soso','timo','ramy']
name = ['Salem']
x = [names]+ [name]
names.pop(2)
print(names)
print(names[0][4])

nums = [1,2,3,4,5,6]
#nums += [2] 
print(nums[1:4])

lst = names[-2:] + nums[-3:]
print(lst)

fruits = ['Apple', 'Orange', 'Mango']
y = nums + fruits
print(y)


print(nums[2:3])
print(nums[2])

num = [1,2,3,4]
num[1:3] = [25]
print(num)

num = 4
nums = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]]

print(num in nums[0])

print('5' in '15')