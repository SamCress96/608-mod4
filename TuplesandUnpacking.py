# Tuples and Unpacking Samantha Cress
# Section 5.3 Tuples

# To create an empty tuple, use empty parentheses 
student_tuple1 = ()
print ('student_tuple1:', student_tuple1)
print ('student_tuple1_len:', len(student_tuple1))

# You can pack a tuple by separting its values with commas
student_tuple2 = 'John', 'Green', 3.3
print ('student_tuple2:', student_tuple2)
print ('student_tuple2_len:', len(student_tuple2))

# When ouputing a tuple, python always displays its contents in a parentheses. You may surround a tuples
# comma separated list of values with opitional parentheses. 
another_student_tuple = ('Mary', 'Red', 3.3)
print ('another_student_tuple:', another_student_tuple)

# The following code creates a one-element tuple
a_singleton_tuple = ('red',) # note the comma, it indentifies the singleton tuple as a tuple
print ('a_singleton_tuple:', a_singleton_tuple)

# Accessing Tuple elements 
time_tuple = (9, 16, 1)
print ('time_tuple:', time_tuple)
print ('Seconds since midnight:', time_tuple[0] * 3600 + time_tuple[1] * 60 + time_tuple[2])

# Adding items to a string or tuple. As with lists, the += augmented assignment statement can be used with strings and tuples, even though they’re immutable.
tuple1= (10, 20, 30)
tuple2 = tuple1
print ('tuple2:', tuple2)
# Concatenating the tuple (40, 50) to tuple1 creates a new tuple, then assigns a reference to it to the variable tuple1—tuple2 still refers to the original tuple:
tuple1 += (40, 50)
print ('tuple1:', tuple1)
print ('tuple2:', tuple2)

# Appending Tuples to lists, you can use += to append a tuple to a list 
numbers = [1, 2, 3, 4, 5,]
numbers += (6,7)
print ('numbers:', numbers)

# Tuples may contain mutable objects, the following is a student_tuple with first name, last name, and list of grades
student_tuple = ('Amanda', 'Blue', [98, 75, 87])
print ('student_tuple:', student_tuple)
# Even though the tuple is immutable, its list element (in this case grades) is mutable
student_tuple[2][1] = 85
print ('student_tuple:', student_tuple)
# In the double-subscripted name student_tuple[2][1], Python views student_tuple[2] as the element of the tuple containing the list [98, 75, 87], 
# then uses [1] to access the list element containing 75. The assignment in snippet [24] replaces that grade with 85.

# Self Check
# Create a single-element tuple containing 123.45, then display it.
singleton_tuple = (123.45,)
print ('singleton_tuple:', singleton_tuple)

# Show what happens when you attempt to concatenate sequences of different types
# list = [1, 2, 3]
# tuple = (4, 5, 6)
# print ('new:', list + tuple)
# python displays the following error: type error: can only concatenate list (not tuple) to list

# Section 5.4 Unpacking Sequences

# The previous chapter introduced tuple unpacking. You can unpack any sequence’s elements by assigning the sequence to a comma-separated list of variables.
# A ValueError occurs if the number of variables to the left of the assignment symbol is not identical to the number of elements in the sequence on the right:
student_tuple = ('Amanda', [98, 85, 87])
first_name, grades = student_tuple
print ('First name:', first_name)
print ('Grades:', grades)

# The following code unpacks a string, a list and a sequence produced by range:
first, second = 'hi'
print (f'{first} {second}')
number1, number2, number3 = [2, 3, 5]
print (f'{number1} {number2} {number3}')
number1, number2, number3 = range(10, 40, 10)
print (f'{number1} {number2} {number3}') 

# Swapping Values via packing and unpacking
number1 = 99
number2 = 22
number1, number2 = (number2, number1)
print (f'number1 = {number1}; number2 = {number2}')

# Accessing Indices and Values Safely with Built-in function enumerate 
# The preferred mechanism for accessing an element’s index and value is the built-in function enumerate.
colors = ['red', 'orange', 'yellow']
print ('color list:', list(enumerate(colors))) 

# Similarly the built-in function tuple creates a tuple from a sequence:
print ('color tuple:', tuple(enumerate(colors)))

# The following for loop unpacks each tuple returned by enumerate into the variables index and value and displays them:
for index, value in enumerate(colors):
    print (f'{index}: {value}')

# Creating a primitive bar chart 
# fig05_01.py
"""Displaying a bar chart"""
numbers = [19, 3, 15, 7, 11]

print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>8}   Bar')

for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8}   {"*" * value}')

# Self Check
# Create a tuple high_low representing a day of the week (a string) and its high and low temperatures (integers)
# Practice:
high_low = ('Wednesday', [68, 85])
print ('high_low_tuple:', high_low) 
day_of_week, high_and_low_temp = high_low
print (f'{day_of_week} {high_and_low_temp}')
print ('Day:', day_of_week)
print ('Temps:', high_and_low_temp)
print ('high_low:', list(enumerate(high_low))) 
# Corrected:
high_low = ('Wednesday', 68, 85)
print (high_low)
print(f' {high_low[0]}: high={high_low[2]}, low={high_low[1]}') 
# print (day, high = high_low) an occrus because you must unpack all the elements of a sequence.

# Create the list names containing three name strings. Use a for loop 
# and the enumerate function to iterate through the elements and display each element’s index and value.
names = ['Carly', 'Justin', 'Taylor']
for i, name in enumerate(names):
    print(f'{i}: {name}') 