# Creating a list name 'menu
menu = ['expresso', 'mocha', 'latte', 'cappuccino', 'cortado', 'americano']


# Creating a function named 'find_coffee()' that takes 'coffee' as input parameter
# Creating an if-statment that checks if "coffee[0]" equal to "c" then return "coffee"
# In other words, the if-statment checks if the items in the list that gets passed in
# start with the letter 'c' (coffee[0]) ... it's true return the item.
def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee


# The map() function:
# The map() function takes all objects in a list and applies a function to them ##

# Note 1: the map() function accepts a "function" and "list" as input paremters
# Note 2: the map() function returns an object.
# Note 3: Remember that we'e not calling the "find_cofee" function here, we are simply
# passing the "find_coffee" function as an argument into the "map()" function
map_coffee = map(find_coffee, menu)

# printing whatever the "map()" method returns
print(map_coffee)

for x in map_coffee:
    print(x)


# The filter() function:
# The filter() function also allows you to take in all objects in the list and runs
# through a function but it creates a new list and only returns values where the
# evaluated function return true. That's why there are no "None" values displated
# in the output for the filter function.

filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)
