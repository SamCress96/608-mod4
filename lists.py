# Samantha Cress, Creating a list
c = [-45, 6, 0, 72, 1543]
print ('c: ', c)

# The first element in a list as an index of 0
print ('c[0]: ', c[0])
print ('c[4]: ', c[4])

# To get a list's length, use the built-in len function
len(c)
print ('list length: ', len(c))

# Lists can also be accessed from the end by using negative indices, from example in the list above 
# cont. c[4] can be accessed with c[-1]
c[-1]
print ('c[-1]: ', c[-1])
print ('c[-5]: ', c[-5])

# Trying to access an index longer than the list
# c[87]
# print ('c[87]: ', c[87])
# When trying to access a index longer than the list python returns the following error:
# Indexerror: list index out range

# Adding the the first 3 items in list [c]
print ('First three items= ', c[0] + c[1]+ c[2])

# Appending to a list +=
a_list = []
for number in range(1, 6):
    a_list += [number]
print ('a_list: ', a_list)
letters = []
letters += 'Python'
print ('Letters: ', letters)

# Concatenating Lists with + 
list1 = [10, 20, 30,]
list2 = [40 , 50]
concatenated_list = list1 + list2
print ('concatenated_list: ', list1 + list2)

# Usihng for and range to access list indices and values
for i in range(len(concatenated_list)):
    print (f'{i}: {concatenated_list[i]}')
# The function range(len(concatenated_list)) produces a sequence of integers representing the concatenated_list's indices

# Comparison Operators: you can compare enter lists element by element using comparision operators
a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3, 4]
print ('a == b: ', a == b) # True: correspinding eleemnts in both are equal
print ('a == c: ', a == c) # False: a and c have different elements and lengths
print ('a < c: ', a < c) # True: a has fewer elements than c 
print ('c >= b:' , c >= b) # True: elements 0 -2 are equal but c has more elements 

# Self Check 
def cube_list(values):
    for i in range(len(values)):
        values[i] **= 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cube_list(numbers)
print ('numbers: ', numbers)