# Comprehensions:
#  Comprehensions in Python are a way to create a new sequence from an already existing
# sequence.
#
# There are four main types of comprehensions in Python:
#   * List Comprehensions
#   * Dictionary Comprehensions
#   * Set Comprehensions
#   * Generator Comprehensions
#
# You will now explore each of these to learn how to use them.
#
# * List Comprehensions:
#   The syntax for list comprehensions is:
#   [ <expression> for x in <sequence> if <condition> ]
#
# The same can be illustrated with the example below ##

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# Example 1: List comprehension: Updating the same list
data = [x+3 for x in data]
# print("Updating the list: ", data)

# Example 2: List comprehension: Creating a different list with updated values
new_data = [x*2 for x in data]
# print("Creating new list: ", new_data)

# Example 3: List comprehension with an if-condition: Multiplies of four:
fourx = [x for x in new_data if x % 4 == 0]
# print("Divible by four: ", fourx)

# Example 4: Alternatively, we can update the list with the if condition as well
fourxsub = [x - 1 for x in new_data if x % 4 == 0]
# print("Divisable by four minus one: ", fourxsub)

# Example 5: Using the range function:
# Creating a list comprehension with a for-loop that runs over numbers from 0 to 100
# if the remainder of the number "x" is 0, then print the number "x" .
nines = [x for x in range(100) if x % 9 == 0]
# print("Nines ", nines)

# The given examples provides different ways in which the list comprehension can be
# used to update the list or generate a new list. Comprehensions can provide a shorthand
# and elegant way of updating sequences. As may be evident, the same code can be written
# using the conventional for-loop and if else conditions##

# For instance, in the case of example 1:
# List comprehension:
data = [x + 3 for x in data]

# Regular for-loop
for x in range(len(data)):
    data[x] = data[x] + 3

# List comprehension can be a better option once you get the hang out it. It must be
# noted how the same concept can be extended to include multiple if else conditions
# as necessary.
#
# List comprehensions are the most commonly used, but there are other types that can also
# make code pragmatic and simple. The structure and syntax for them are very similar
# to that of list comprehensions except for the data types that are used.
#
# Dictionary Comprehension:
#
#   The syntax for dictionary comprehension is:
#
# dict = {key:value for key, value in <sequence> if <condition>}
#
# Dictionary comprehension takes one or two lists as input and creates a dictionary
# out of it. I will now demonsrate how this can be done using one list and using two
# lists. ##

# Dictionary comprehension: Using the range() function and no input list
# Note 1: In this example, "x" is the key and "x*2" is the value of the "usingrange"
# dictionary. Togther "x" and "x*2" form the key-value pairs of the dictionary
# Note 2: Basically, we are looping over the numbers in the range 0 to 12 and generating
# keys of the "usingrange" dictionary through iteration and values for the keys by
# performing "x*2".
usingrange = {x: x*2 for x in range(12)}
# print("using range(): ", usingrange)

# Lists
# A list named "months" with strings as list "items"
months = ["Jan", "Feb", "Mar", "Apr", "May", "June",
          "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
# A list named "number" with integers as list "items"
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Creating a dictionary comprehension using one input list
# Here, we use the looping variable "x" to generate the keys for the "numdict"
# and "x**2" to create the values
numdict = {x: x**2 for x in number}
# print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key: value for (key, value) in zip(number, months)}
# print("Using two lists: ", months_dict)


# Note how in use case of using two lists, the format if follows is:
#
# * new_dict = { key:value for (key, value) in zip(list1, list2) } ##
#
# Here I used the "zip()" function that combines two lists. When two lists are of
# unequal length, the the length of the shorter list is the lenght of the dictionary.
#
#
# Set Comprehension:
#
#   The set comprehension deals with the set data type and it's very similar to the
# list comprehension. The only difference is the use of the curly brackets instead of
# square brackets as in lists. For example, ##
# Out putting a list of values in the range 10 to 20 excluding the values 12, 14 and 16
set_a = {x for x in range(10, 20) if x not in [12, 14, 16]}
# print(set_a)

# You can see the code format is similar to what I used in list comprehensions.
# For the sake of showing versatility, I used the "not in" keywords to check the values
# in the list.The output is the values in the range 10 to 20 that are not present in
# the list.
#
# Generator Comprehension:
#
# Generator comprehension are very similar to lists with the varation of using curved
# brackets instead of square brackets. They are also more memory efficent as compared
# to list comprehensions. For example ##

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end=" ")

# In the code above, I created a generator object of the class generator instead of 
# a list element. The elements in this iterator cannot be directly accessed and need 
# help of a for loop and as such, I iterate over these elements and print them .
# 
# ##