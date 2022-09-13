#6.2.1 Creating a Dictionary
country_codes = {'Finland': 'fi', 'South Africa': 'za', 'Nepal': 'np'}
print ('country codes dictionary:', country_codes)

#Determining if a Dictionary is Empty
#The built-in function len returns the number of key–value pairs in a dictionary:
print ('Key Value pair in country codes:', len(country_codes))
#You can use a dictionary as a condition to determine if it’s empty—a non-empty dictionary evaluates to True:
if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is not empty;')
#An empty dictionary evaluates to False. 
country_codes.clear()
if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is empty')

#Self Check
#Create a dictionary named states that maps three state abbreviations to their state names, then display the dictionary.
states = {'Nebraska': 'NE', 'Missouri': 'MO', 'Iowa': 'IA'}
print ('states dictionary:', states)

#6.2.2 Iterating through a Dictionary
#The following dictionary maps month-name strings to int values representing the numbers of days in the corresponding month.
days_per_month = {'January': 31, 'February': 28, 'March': 31}
print ('days per month:', days_per_month)
#The following for statement iterates through days_per_month’s key–value pairs:
for month, days in days_per_month.items():
    print(f'{month} has {days} days')

#6.2.3 Basic Dictionary Operations
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}
print('roman numerals dictionary:', roman_numerals)
#Accessing the Value Associated with a Key
print ('roman numberal V value:', roman_numerals['V'])
#Updating the Value of an Existing Key–Value Pair
roman_numerals['X'] = 10
print ('roman numerals updates:', roman_numerals)
#Adding a New Key-Value Pair
roman_numerals['L'] = 50
print ('roman numerals with new key value pair:', roman_numerals)
#Removing a Key-Value Pair
del roman_numerals['III']
print ('roman numerals del:', roman_numerals)
#You also can remove a key–value pair with the dictionary method pop, which returns the value for the removed key:
roman_numerals.pop('X')
print ('roman numerals pop:', roman_numerals)
#Attempting to Access a Nonexistent Key: accessing a nonexistent key results in a KeyError
#You can prevent this error by using dictionary method get, which normally returns its argument’s corresponding value
roman_numerals.get('III')
print (roman_numerals.get('III', 'III not in dictionary'))
print (roman_numerals.get('V')) 
#Testing Whether a Dictionary Contains a Specified Key
#Operators in and not in can determine whether a dictionary contains a specified key:
print ('V' in roman_numerals)
print ('III' in roman_numerals)
print ('III' not in roman_numerals)
#Self-Check
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}
roman_numerals['x'] = 10
print (roman_numerals)

#6.2.4 Dictionary Methods keys and values
#methods keys and values can be used to iterate through only a dictionary’s keys or values
months = {'January': 1, 'February': 2, 'March': 3}
for month_name in months.keys():
    print(month_name, end=' ')

for month_number in months.values():
    print(month_number, end=' ')

#Dictionary Views
#Dictionary methods items, keys and values each return a view of a dictionary’s data. When you iterate over a view, 
#it “sees” the dictionary’s current contents—it does not have its own copy of the data.
months_view = months.keys()
for key in months_view:
    print(key, end=' ')

#add a new key–value pair to months and display the updated dictionary:
months['December'] = 12
print ('Updated month_view dictionary:', months)

#iterate through months_view again. The key we added above is indeed displayed:
for key in months_view:
    print(key, end=' ')

#Converting Dictionary Keys, Values and Key–Value Pairs to Lists
print (list(months.keys()))
print (list(months.values()))
print (list(months.items()))

#Processing Keys in Sorted Order 
#To process keys in sorted order, you can use built-in function sorted as follows:
for month_name in sorted(months.keys()):
    print(month_name, end=' ')

#Self-Check 
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5}
print (list(roman_numerals.keys()))
print (list(roman_numerals.values()))
print (list(roman_numerals.items()))

#Section 6.2.5 Dictionary Comparisions
#The comparison operators == and != can be used to determine whether two dictionaries have identical or different contents.
country_capitals1 = {'Belgium': 'Brussels','Haiti': 'Port-au-Prince'}
country_capitals2 = {'Nepal': 'Kathmandu', 'Uruguay': 'Montevideo'}
country_capitals3 = {'Haiti': 'Port-au-Prince', 'Belgium': 'Brussels'}
print (country_capitals1 == country_capitals2)
print (country_capitals1 == country_capitals3)
print (country_capitals1 != country_capitals2)

#Section 6.2.6 
#Example: Dictionary of Student Grades
# fig06_01.py
"""Using a dictionary to represent an instructor's grade book."""
grade_book = {            
    'Susan': [92, 85, 100], 
    'Eduardo': [83, 95, 79],
    'Azizi': [91, 89, 82],  
    'Pantipa': [97, 91, 92] 
}

all_grades_total = 0
all_grades_count = 0

for name, grades in grade_book.items():
    total = sum(grades)
    print(f'Average for {name} is {total/len(grades):.2f}')
    all_grades_total += total
    all_grades_count += len(grades)
    
print(f"Class's average is: {all_grades_total / all_grades_count:.2f}")

#Section 6.2.7
#Example: Word Counts
# fig06_02.py Samantha Cress
"""Tokenizing a string and counting unique words."""

text = ('Cats sleep , anywhere, '
'Any table, any chair '
'Top of piano, window-ledge, '
'In the middle, on the edge, '
'Open drawer, empty shoe, Anybody’s lap will do, '
'Fitted in a cardboard box, '
'In the cupboard, with your frocks- '
'Anywhere! They don’t care! '
'Cats sleep anywhere.')

#Source: ‘Cats’ By Eleanor Farjeon

word_counts = {}

# count occurrences of each unique word
for word in text.split():
    if word in word_counts: 
        word_counts[word] += 1  # update existing key-value pair
    else:
        word_counts[word] = 1  # insert new key-value pair

print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique words:', len(word_counts))

#Python Standard Library Module collections
#The module collections contains the type Counter, which receives an iterable and summarizes its elements. 
from collections import Counter
from tkinter import N
text = ('this is sample text with several words ' 
'this is more sample text with some different words')
counter = Counter(text.split())
for word, count in sorted(counter.items()):
    print(f'{word:>12}{count}')
print('Number of unique keys:', len(counter.keys()))

#Self Check
import random
numbers = [random.randrange(1, 6) for i in range(50)]
from collections import Counter
counter = Counter(numbers)
for value, count in sorted(counter.items()):
    print(f'{value:<4}{count}')

#Section 6.2.8 
#Dictionary Method update
country_codes = {}
country_codes.update({'South Africa': 'za'})
print (country_codes)
country_codes.update(Australia='ar')
print (country_codes)
country_codes.update(Australia='au')
print (country_codes)

#Section 6.2.9 Dictionary Comphrehensions
#Dictionary comprehensions provide a convenient notation for quickly generating dictionaries, often by mapping one dictionary to another.
months = {'January': 1, 'February': 2, 'March': 3}
months2 = {number: name for name, number in months.items()}
print (months2)

grades = {'Sue': [98, 87, 94], 'Bob': [84, 95, 91]}
grades2 = {k: sum(v) / len(v) for k, v in grades.items()}
print (grades2)

#Self Check
#Use a dictionary comprehension to create a dictionary of the numbers 1–5 mapped to their cubes:
print ({number: number ** 3 for number in range(1, 6)})

#Section 6.3 Samantha Cress

#Creating a Set with Curly Braces The following code creates a set of strings named colors:
colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue'}
print ('Colors:', colors)

#Determining a Set’s Length
print ('Colors Length:', len(colors))

#Checking Whether a Value Is in a Set
#You can check whether a set contains a particular value using the in and not in operators:
print ('red' in colors)
print ('purple' in colors)
print ('purple' not in colors)

#Iterating Through a Set, Sets are iterable, so you can process each set element with a for loop:
for color in colors:
    print(color.upper(), end='\n') 

#Creating a Set with the Built-In set Function
numbers = list(range(10)) + list(range(5))
print (numbers)
set(numbers)
print (set(numbers))

#Self Check
text = 'to be or not to be that is the question'
unique_words = set(text.split())
for word in sorted(unique_words):
    print(word, end='\n')

#Comparing Sets
print ({1, 3, 5} == {3, 5, 1})
print ({1, 3, 5} != {3, 5, 1})
print ({1, 3, 5} > {3, 5, 1})
print ({1, 3, 5} > {7, 3, 5, 1})
print ({1, 3, 5}.issubset({3, 5, 1}))
print ({1, 3, 5}.issubset({3, 5, 1}))
print ({1, 2}.issubset({3, 5, 1}))
print ({1, 3, 5} > {3, 5, 1})
print ( {1, 3, 5, 7} > {3, 5, 1})
print ({1, 3, 5} >= {3, 5, 1})
print ({1, 3, 5} >= {3, 1})
print ({1, 3} >= {3, 1, 7})
print ({1, 3, 5}.issuperset({3, 5, 1}))
print ({1, 3, 5}.issuperset({3, 2}))

#Self Check
#use sets and issuperset to determine whether the characters of the string 'abc def ghi jkl mno' are a superset of the characters in the string 'hi mom'.
print ('self check:', set('abc def ghi jkl mno').issuperset('hi mom')) 

#6.3.2 Mathematical Set Operations
#Union The union of two sets is a set consisting of all the unique elements from both sets.
print ({1, 3, 5} | {2, 3, 4})
print ({1, 3, 5}.union([20, 20, 3, 40, 40]))

#Intersection, The intersection of two sets is a set consisting of all the unique elements that the two sets have in common
print ({1, 3, 5} & {2, 3, 4})
print ('intersection:', {1, 3, 5}.intersection([1, 2, 2, 3, 3, 4, 4]))

#Difference, The difference between two sets is a set consisting of the elements in the left operand that are not in the right operand.
print ({1, 3, 5} - {2, 3, 4})
print ('difference:', {1, 3, 5, 7}.difference([2, 2, 3, 3, 4, 4]))

#Symmetric Difference
#The symmetric difference between two sets is a set consisting of the elements of both sets that are not in common with one another. 
print ({1, 3, 5} ^ {2, 3, 4})
print ('symmetric difference:', {1, 3, 5, 7}.symmetric_difference([2, 2, 3, 3, 4, 4]))

#Disjoint
#Two sets are disjoint if they do not have any common elements. You can determine this with the set type’s isdisjoint method:
print ({1, 3, 5}.isdisjoint({2, 4, 6}))
print ({1, 3, 5}.isdisjoint({4, 6, 1}))

#Self Check
#Given the sets {10, 20, 30} and {5, 10, 15, 20}, use the mathematical set operators to produce the following sets:
print ('Set A:', {10, 20, 30} - {5, 10, 15, 20})
print ('Set B:', {10, 20, 30} ^ {5, 10, 15, 20})
print ('Set C:', {10, 20, 30} | {5, 10, 15, 20})
print ('Set D:', {10, 20, 30} & {5, 10, 15, 20})

#6.3.3 Mutable Set Operators and Methods
#Mutable Mathematical Set Operations
numbers = {1, 3, 5}
numbers |= {2, 3, 4}
print (numbers)
numbers.update(range(10))
print (numbers)

#Methods for Adding and Removing Elements
numbers.add(17)
numbers.add(3)
print (numbers)
#Set method remove removes its argument from the set—a KeyError occurs if the value is not in the set:
numbers.remove(3)
print (numbers)
#You also can remove an arbitrary set element and return it with pop, but sets are unordered, so you do not know which element will be returned:
print (numbers.pop())
print (numbers)
#Finally, method clear empties the set on which it’s called:
numbers.clear()
print (numbers)

#6.3.4 Set Comprehensions
#Like dictionary comprehensions, you define set comprehensions in curly braces.
numbers = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10]
evens = {item for item in numbers if item % 2 == 0}
print ('evens:', evens)