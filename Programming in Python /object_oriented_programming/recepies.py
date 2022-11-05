# Instainticate a Custom Object

# Note 1: the '__new__()' method in Python is responsible for returning a new object
# in Python.
# class Recipe():
#     # Note 2: The 'cls' here is not a keyword, but a convention. It acts as a place
#     # holder for passing the class, "Recipe()", as its first argument, which will be
#     #  used for creating the new object.
#     def __new__(cls: type[Self]) -> Self:
#         pass

#     # Note 2: The 'cls' here is not a keyword, but a convention.
#     # It acts as a place holder
#     # for passing the class, "Recipe()", as its first argument, which will be used
#     # for creating the new object.
#     def __init__(self) -> None:
#         pass


class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The " + self.dish + " has " + str(self.items) +
              " and takes " + str(self.time) + " min to prepare")


# Creating an instance of the "Recipe" class
pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
# Creating another instance or an object of the "Recipe" class
pasta = Recipe("Pasta", ["penne", "sauce"], 55)

# printing the attributes of the "pizza" and "pasta" objects
print(pizza.items)
print(pasta.items)

# Calling the "content()" method of the "pizza" object
# The outputs should be all the arguments that got passed into the "pizza" object.
print(pizza.contents())
