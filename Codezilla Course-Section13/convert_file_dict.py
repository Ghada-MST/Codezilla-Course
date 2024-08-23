###method1##################3
a_dictionary = {}
with open("data.txt") as a_file:
  for line in a_file:
    key, value = line.split()
    print(key, value)
    #Split line into a tuple

    a_dictionary[key] = value
  #Add tuple values to dictionary

print(a_dictionary)

####method2##########################
with open("data.txt") as a_file:
  a_dictionary = dict([line.split() for line in a_file])

print(a_dictionary)

####method3############################
with open('data.txt') as f:
  a_dictionary = dict(line.rstrip().split(None, 1) for line in f)

print(a_dictionary)
