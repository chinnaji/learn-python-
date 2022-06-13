# print('Hello world')

# show in the termnal
# print('hello world')

# get the length 
# print(len('hello again'))

# get the data type 
# print(type('hello again'))

# get the data type 
# print(10 == "10")
# list --- equivalent to array in javascript
# skills = [1,2,'king']

# dictionary --- equivalent to object in javascript
# things = {'name': 'king', 'age': '20', 'skills': ['python', 'java', 'c++']}

# firstName = 'John'

# a,b,c = 1

# area of a square
# l = input('whats the length of the square: ')
# print('the area of the square is: ' + str(int(l) ** 2))

# st = {'a':1,' b':2, 'c':3}
# aa = {"a":4,"e":5,"f":6}
# print( st is aa)          
# print('1 is not 2', 1 is not 2)          
 # True - because 1 is not 2


# multiline string
# print('''
# lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
# lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
# lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
# lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
# lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
# ''')

# escape character
# print('hello\tworld\:')


# formatting strings 
# string formating is kinda equivalent to js string interpolation
# OLD METHOD!
# f_name = 'John'
# l_name= 'Doe'
# age= 20
# formated = 'My name is %s %s. I am %s' %(f_name, l_name,age )
# integar
# radius = 22.2

# formated = 'The radius of the circle is %.2f' %(radius) # .2f refers to 2 significant figures after the decimal
# python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
# formated = "I love %s"%(python_libraries[0])

# New school!!!😋😊 
# formated = ' I love {} {}'.format(python_libraries)



# NEWEST SCHOOL !!!!😂😁 -----------  f-Strings  
# formated = f' I love {python_libraries[0]} '
# print(formated)


# Unpacking -------- similar to destructuring in js
name = 'Python'
# a,b,c,d =name
# print(a)

# Slicing Python Strings
# from the front
# sliced_string = name[0:3]
# from behind
# sliced_string_from_behind = name[-3:]

# skipping characters while slicing
# skip 2 strings
# language = 'Pythonisawesome'
# pto = language[0:len(language):4] #
# print(pto) # Pto



# DAY 4 CHALLENGE
# 1 
strings = ['Thirty','Days','Of','Python']
joined_strings = " ".join(strings)
# print(joined_strings)

company = "Coding For All"
# print(company.upper())
# print(company.swapcase())


# print(company.index('C'))


# -------------------------------------------------------------------------------------------------------------#
# Lists
# A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

# list = list([1,22])
new_list = [1,2,3,4,5,6,7,8,9,10]
list_length = len(new_list)

# unpacking list items
# Unpacking is equivalent to destructuring in JS
one,*rest,ten= new_list
#   👆   *rest denotes the  rest parameter

# Slicing Items from a List
sliced = new_list[2:-1]
# sliced = new_list[2:list_length + 1]
# sliced = new_list[0:]
sliced = new_list[::2] #It will take every 2cnd item 

# negative indexing
sliced = new_list[-5:-2]
# sliced = new_list[::-2]

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
# print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']

# checking an item in a list
check_list = 12 in new_list


# Adding items to a list 
# new_list.append([11,12,13,1,2,3])
# print(new_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# new_list.insert(-5,'take over')
# print(new_list) # [1, 2, 3, 4, 5, 'take over', 6, 7, 8, 9, 10, 11]

# remove items
# new_list.remove(1)
# print(new_list) # [2, 3, 4, 5, 'take over', 6, 7, 8, 9, 10, 11]

# using pop to remove items
# The pop() method removes the specified index, (or the last item if index is not specified):

# abc = new_list.pop(2)

# using del
# del new_list[2]
# del new_list[2:8]
# del new_list #total anhilation of the list🩸🩸

# The clear() method empties the list:
# new_list.clear()
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
# find minimum and maximum
# print(ages.index(min(ages)))
min_age = min(ages)
max_age = max(ages)
ages.append(min_age)
ages.append(max_age)

total = sum(ages)
average = total / len(ages)
range = max_age - min_age
print(ages)


