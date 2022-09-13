# Section 5.5 Sequence Slicing Samantha Cress

# You can slice sequences to create new sequences of the same type containing subsets of the original elements. 
# Specifying a slice with starting and ending indices
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
print ('numbers[2:6]:', numbers[2:6])
# The slice copies elements from the starting index to the left of the colon (2) up to, 
# but not including, the ending index to the right of the colon (6). The original list is not modified.

# Specifying a slice with only an ending index
# If you omit the starting index, 0 is assumed. So, the slice numbers[:6] is equivalent to the slice numbers[0:6]:
print ('numbers[:6]:', numbers[:6])
print ('numbers[0:6]:', numbers[0:6])

# Specifying a slice with only a starting index
# If you omit the ending index, Python assumes the sequence’s length (8 here), 
# so snippet [5]’s slice contains the elements of numbers at indices 6 and 7:
print ('numbers[6:]:', numbers[6:])
print ('numbers[6:len(numbers)]:', numbers[6:len(numbers)])

# Specifying a slice with no indices
print ('numbers[:]:', numbers[:])
#in the snippet above, the new list’s elements refer to the same objects as the original list’s elements, 
#rather than to separate copies

# Slicing with Steps
# The following code uses a step of 2 to create a slice with every other element of numbers:
print ('numbers[::2]:', numbers[::2]) #We omitted the start and end indices, so 0 and len(numbers) are assumed, respectively.

# Slicing with negatice indices and steps
# You can use a negative step to select slices in reverse order. The following code concisely creates a new list in reverse order:
print ('numbers[::-1]:', numbers[::-1])
# The code above is equivalent to the following:
numbers[-1:-9:-1]
print ('numbers[-1:-9:-1]:', numbers[-1:-9:-1])

# Modifying lists via slices
# You can modify a list by assigning to a slice of it—the rest of the list is unchanged. 
# The following code replaces numbers’ first three elements, leaving the rest unchanged:
numbers[0:3] = ['two', 'three', 'five']
print ('numbers:', numbers)
# The following deletes only the first three elements of numbers by assigning an empty list to the three-element slice:
numbers[0:3] = []
print ('numbers:', numbers)
# The following assigns a list’s elements to a slice of every other element of numbers:
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
numbers[::2] = [100, 100, 100, 100]
print ('numbers:', numbers)
print ('ID:', id(numbers)) # this value changes each time the code is ran
# The following deletes all elements in numbers leaving the list empty
numbers [:] = []
print ('numbers:', numbers)
print ('ID:', id(numbers))
# Deleting numbers’ contents (snippet [19]) is different from assigning numbers a new empty list [] (snippet [22]). 
# To prove this, we display numbers’ identity after each operation. The identities are different, so they represent separate objects in memory.

# Section 5.5 Self Check
# Create a list called numbers containing the values from 1 through 15, then use slices to perform the following operations consecutively:
numbers = list(range(1, 16))
print ('numbers:', numbers)
# Select numbers even integers
print ('Even Integers:', numbers[1:len(numbers):2])
# Replace the elements at indices 5 through 9 with 0s, then show the resulting list
numbers[5:10] = [0] * len(numbers[5:10])
print ('numbers:', numbers)
# Keep only the first five elements, then show the resulting list.
numbers[5:] = []
print ('first five elements:', numbers)
# Keep only the first five elements, then show the resulting list.
numbers[:] = []
print ('Empty:', numbers)

# Section 5.6 del Statement 

# Deleting the element at a specific list index
numbers = list(range(0, 10))
print (numbers)
del numbers[-1]
print ('del number[-1]:', numbers)

# Deleting a Slice from a list 
# The following deletes the list's first two elements 
del numbers[0:2]
print ('del numbers[0:2]:', numbers)
# The following uses a step in the slice to delete every other element from the entire list:
del numbers[::2]
print ('Delete every other element:', numbers)

# Deleting a Slice Representing the entire list 
# The following code delets all of the lists elements 
del numbers[:]
print ('Delete all elements in list:', numbers)

# Section 5.6 Self Check 
# Create a list called numbers containing the values from 1 through 15
numbers = list(range(1, 16))
print (numbers)
# Delete a slice containing the first four elements, then show the resulting list.
del numbers[0:4]
print (numbers)
# Delete a slice containing the first four elements, then show the resulting list.
del numbers[::2]
print (numbers)

# 5.7 Passing Lists to Functions

# Passing an entire list to a function
# Consider the function modify_elements, which receives a reference to a list
# and multiplies each of the list’s element values by 2:
def modify_elements(items):
    """Multiplies all element values in items by 2."""
    for i in range(len(items)):
        items[i] *= 2
numbers = [10, 3, 7, 1, 9]
modify_elements(numbers)
print ('modify_elements(numbers):', numbers)

# Passing a Tuple to a function 
# When you pass a tuple to a function, attempting to modify the tuple’s immutable elements results in a 
# TypeError: 'tuple' object does not support item assignment

# Section 5.8 Sorting Lists 

# Sorting a list in ascending order
# List method sort modifies a list to arrange its elements in ascending order:
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
numbers.sort()
print ('Ascending order:', numbers)

# Sorting a list in descending order
# To sort a list in descending order, call list method sort
# with the optional keyword argument reverse set to True (False is the default):
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
numbers.sort(reverse=True)
print('Descending order:', numbers)

# Built-In Function sorted
# Built-in function sorted returns a new list containing the sorted elements of its argument sequence—the original sequence is unmodified
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
ascending_numbers = sorted(numbers)
print ('ascending_numbers:', ascending_numbers)
print (numbers)
letters = 'fadgchjebi'
ascending_letters = sorted(letters)
print ('ascending letters:', ascending_letters)
print ('Letters:', letters)
colors = ('red', 'orange', 'yellow', 'green', 'blue')
ascending_colors = sorted(colors)
print ('Ascending Colors:', ascending_colors)
print ('colors:', colors)
# Use the optional keyword argument reverse with the value True to sort the elements in descending order.

# Section 5.8 Self-Check
# Create a foods list containing 'Cookies', 'pizza', 'Grapes', 'apples', 'steak' and 'Bacon'. Use list method sort to sort the list in ascending order.
foods = ['cookies', 'pizza', 'grapes', 'apples', 'steak', 'bacon']
foods.sort()
print ('Foods:', foods)
# They are in order as defined by the underlying character set—known as lexicographical order

# Section 5.9 Searching Sequences

# List method index
# List method index takes as an argument a search key—the value to locate in the list—then searches through the list 
# from index 0 and returns the index of the first element that matches the search key:
numbers = [3, 7, 1, 4, 2, 8, 5, 6]
print ('numbers.index(5):', numbers.index(5)) #A ValueError occurs if the value you’re searching for is not in the list.

# Specifying the starting index of a search 
# Using method index’s optional arguments, you can search a subset of a list’s elements. You can use *= to multiply a sequence
numbers *= 2
print ('numbers*2:', numbers)
# The following code searches the updated list for the value 5 starting from index 7 and continuing through the end of the list:
numbers.index(5, 7)
print ('numbers.index(5, 7):', numbers.index(5, 7))

# Specifying the starting and ending indices of a search
# Specifying the starting and ending indices causes index to search from the starting index up to but not including the ending index location. 
# The call to index in snippet [5]:
numbers.index(5,7)
# assumes the length of numbers as its optional third argument and is equivalent to:
numbers.index(5, 7, len(numbers))
# The following looks for the value 7 in the range of elements with indices 0 through 3:
print ('numbers.index(7, 0, 4):', numbers.index(7, 0, 4))

# Operators in and not in 
# Operator in tests whether its right operand’s iterable contains the left operand’s value:
print (1000 in numbers)
print (5 in numbers)
# Similarly, operator not in tests whether its right operand’s iterable does not contain the left operand’s value:
print (1000 not in numbers)
print (5 not in numbers)

# Using Operator in to Prevent a ValueError
key = 1000
if key in numbers:
    print(f'found{key} at index {numbers.index(search_key)}')
else:
    print (f'{key} not found')

# Built-In Functions any and all
# The built-in function any returns True if any item in its iterable argument is True.
# The built-in function all returns True if all items in its iterable argument are True.

# Section 5.9 Self Check
# Create a five-element list containing 67, 12, 46, 43 and 13, then use list method index to search for a 43 and 44. 
# Ensure that no ValueError occurs when searching for 44.
numbers2 = [67, 12, 46, 43, 13]
key = 44
if key in numbers2:
    print(f'found{key} at index {numbers2.index(search_key)}')
else:
    print (f'{key} not found')
numbers2.index(43)
print ('43 placement:', numbers2.index(43))

# Section 5.10 Other List Methods 

# Inserting an Element at a Specific List Index
color_names = ['orange', 'yellow', 'green']
color_names.insert(0, 'red')
print ('color_names_insert:', color_names)

# Adding an element to the end of a list
color_names.append('blue')
print ('color names append:', color_names)

# Adding All the Elements of a Sequence to the End of a List
color_names.extend(['indingo', 'violet'])
print ('color names extend:', color_names)
# This is the equivalent of using +=. The following code adds all the characters of a string then all the elements of a tuple to a list:
sample_list = []
s = 'abc'
sample_list.extend(s)
print ('sample list:', sample_list)
t = (1, 2, 3)
sample_list.extend(t)
print ('sample list extend:', sample_list)
# Rather than creating a temporary variable, like t, to store a tuple before appending it to a list
# you might want to pass a tuple directly to extend. 
sample_list.extend((4, 5, 6)) #note the extra parentheses, a type error occurs if you omit the parentheses
print ('sample list direct extend:', sample_list)

# Removing the First Occurrence of an Element in a List
# Method remove deletes the first element with a specified value—
# a ValueError occurs if remove’s argument is not in the list:
color_names.remove ('green')
print ('color names remove:', color_names)

# Emptying a list, to delete all the elements in a list, call method clear
color_names.clear()
print('color names clear:', color_names) #This is the equivalent of the slice assignment 

# Counting the Number of Occurrences of an Item
# List method count searches for its argument and returns the number of times it is found:
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 2]
for i in range(1, 6):
    print (f'{i} appears {responses.count (i)} times in responses')

# Reversing a list's elements, list method reverse reverses the contents of a list in place
color_names = ['red', 'orange', 'yellow', 'green', 'blue']
color_names.reverse()
print ('color names reverse:', color_names)

# Copying a list, List method copy returns a new list containing a shallow copy of the original list:
copied_list = color_names.copy()
print ('copied list:', copied_list) #This is equivalent to the previously demonstrated slice operation

# Section 5.10 Self-Check
rainbow = ['green', 'orange', 'voilet']
print ('voilet index:', rainbow.index('voilet'))
rainbow.insert(2, 'red')
print ('rainbow insert:', rainbow)
rainbow.append('yellow')
print ('rainbow append:', rainbow)
rainbow.reverse()
print ('rainbow reverse:', rainbow)
rainbow.remove('orange')
print ('rainbow remove:', rainbow)

# Section 5.11 Simulating Stacks with Lists 

# Python does not have a built-in stack type, but you can think of a stack as a constrained list
# You push using list method append, which adds a new element to the end of the list
# You pop using list method pop with no arguments, which removes and returns the item at the end of the list.

stack = []
stack.append('red')
print ('stack:', stack)
stack.append('green')
print ('stack:', stack)
print ('stack pop green:', stack.pop())
print ('stack pop red:', stack)
stack.pop()
print ('stack pop empty:', stack)
# Popping from an empty stack causes an IndexError, To prevent an IndexError, ensure that len(stack) is greater than 0 before calling pop.

# Section 5.12 List Comphrehensions

# list comprehensions are an concise and convenient notation for creating new lists
list1 = []
for item in range(1, 6):
    list1.append(item)
print ('list1:', list1)

# Using a List Comprehension to Create a List of Integers
list2 = [item for item in range(1, 6)]
print ('list2:', list2)
# for clause iterates over the sequence produced by range(1, 6). For each item, the list comprehension evaluates the expression to the left of the for clause 
# and places the expression’s value (in this case, the item itself) in the new list.
# This particular comprehension could have been expressed more concisely using the function list.

# Mapping: Performing Operations in a List Comprehension’s Expression
# Mapping is a common functional-style programming operation that produces 
# a result with the same number of elements as the original data being mapped. 
list3 = [item ** 3 for item in range(1, 6)]
print ('list3:', list3)

# Filtering: List Comprehensions with if Clauses
# filtering elements to select only those that match a condition. 
# This typically produces a list with fewer elements than the data being filtered.
list4 = [item for item in range(1, 11,) if item % 2 == 0] 
print ('list4:', list4)

# List Comprehension That Processes Another List’s Elements
# The for clause can process any iterable. Let’s create a list of lowercase strings and use a list comprehension to create a new list containing their uppercase versions:
colors = ['red', 'orange', 'yellow', 'green', 'blue']
colors2 = [item.upper () for item in colors]
print ('colors:', colors)
print ('colors2:', colors2)

# Section 5.12 Self Check 
list5 = [(x, x **3) for x in range(1, 6)]
print ('list5:', list5)

list6 = [x for x in range(3, 30, 3)]
print ('list6:', list6)

# 5.14 Filter, Map, and Reduce

# Filtering a Sequence’s Values with the Built-In filter Function
# Using built-in function filter to obtain the odd values in numbers:
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
def is_odd(x):
    """Returns True only if x is odd"""
    return x % 2 != 0
print ('is odd filter:', list(filter(is_odd, numbers)))
print ('is odd:', [item for item in numbers if is_odd(item )])

# Using a lambda Rather than a Function
print ('is odd lambda:', list(filter(lambda x: x % 2 != 0, numbers)))

# Mapping a Sequence’s Values to New Values
# Using built-in function map with a lambda to square each value in numbers:
print ('numbers squared:', list(map(lambda x: x ** 2, numbers)))

# Combining filter and map
# You can combine the preceding filter and map operations as follows
print ('odd numbers squared:', list(map(lambda x: x **2 , filter(lambda x: x % 2 != 0, numbers))))

# Section 5.14 Self Check
numbers = list(range(1, 16))
print ('numbers:', numbers)
print ('even numbers:', list(filter(lambda x: x % 2 == 0, numbers)))
print ('numbers squared:', list(map(lambda x: x ** 2, numbers)))
print ('even numbers squared:', list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))))

fahrenheit = [41, 32, 212]
print ('temperatures:', list(map(lambda x: (x, (x - 32) * 5 / 9), fahrenheit)))

# Section 5.16 Two Dimemsional Lists
# Creating a two-dimensional list 
a = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]
a = [[77, 68, 86, 73], # first student's grades
     [96, 87, 89, 81], # second student's grades
     [70, 90, 86, 81]] # third student's grades
for row in a:
    for item in row:
        print(item, end = ' ')
    print ()

# How the Nested Loops Execute
# modify the nested loop to display the list’s name and the row and column indices and value of each element:
for i, row in enumerate(a):
    for j, item in enumerate(row):
        print(f'a[{i}] [{j}]={item} ', end=' ')
    print ()

# Section 5.16 Self Check
t = [[10, 7, 3], [20, 4, 17]]
# Determine and display the average of t’s elements using nested for statements to iterate through the elements
total = 0
items = 0
for row in t:
    for item in row:
        total += item
        items += 1
print (total/ items)
# Write a for statement that determines and displays the average of t’s elements using the reductions sum and len 
# to calculate the sum of each row’s elements and the number of elements in each row.
total = 0
items = 0 
for row in t:
    total += sum(row)
    items += len(row)
print(total/items)

