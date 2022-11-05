# Inheritance and Multiple Inheritance:
#
# Let's say there are two classes: namely class A and class B. If you have to perform
# simple inheritance, it can be done as follows ##
class A:
    pass


class B(A):
    pass

# If class A is the parent class and class B is inheriting from it, then class A is
# passed inside class B as a parameter. This will allow class B to directly access
# attributes and methods inside class A.
#
# Multiple Inheritance:
#
# You have learned about single inheritance so far, Python also gives us the ability to
# perform multiple inheritance between classes.
#
# Here's a simple example of how it can be done: ##

# Example 1:


class A:
    a = 1


class B:
    b = 2

# Class C is demonstrating multiple inheritance by inheriting both from class A and
# class B ##


class C(A, B):
    pass


# Creating an instance of the C class
c = C()
# Here, we are demonstrating the 'c' object has both attributes or inherits attributes
# from both the the "A" class and "B" class by printing the values of 'c.a' and c.b'
print(c.a, c.b)

# The Output is: 1 2 ##

# First, two classes called A and B re created and then variables 'a' and 'b'
# respectively are initialized with values. A new class C is then defined and classes
# A and B are passed to it. This is how multiple inheritance is done in Python.
# The order of classes is important, but not in this specific example. I then
# instantiate an object 'c' of class C. The values of the a and b variables are printed
# over the object c of class C even though a and b are not present inside class C
# The code above is an example of multiple inheritance. Let's examine an example.
#
# Multi-Level Inheritance: ##


class A:
    a = 1


class B(A):
    a = 2


class C(B):
    pass


c = C()
print(c.a)  # Outputs 2

# The output is 2 because C derives from the immediate super class of C, and that's B
#
# The case above is an example of multi-level inheritance where the derived class C
# inherits from base class B.
# The class B is in turn a derived class of the base class C. Class B here is an
# intermediary derived class. There are three levels of inheritance in this case,
# but it can be extneded as long as I want, through it may be impractical after a while.
#
#
# Built-in Functions:
#
# There are two built-in functions that can come in handy when trying to find
# relationships between difference classes and objects: issubclass() and isinstance().
#
# The first one, issubclass() is demonstrated ##
print(issubclass(A, B))

# The two classes are passed as arguments to this function and a boolean result is
# returned. The above example can be extended as follows: ##
print(issubclass(A, B))
print(issubclass(B, A))

# The output are
# False
# True ##

# This illustrates how the child class is passed as the first argument.
# To avoid confusion, this can be read as: "is B subclass of A?" You can see the result
# is "True" in the second case where child B is the subclass.
#
# Another built-in function similar to this one is isinstance() that determines if
# some object is an instance of some class.
#
# So if I write:  ##


class A:
    pass


class B(A):
    pass


b = B()
print(isinstance(b, B))
print(isinstance(b, B))
# Outputs: True for both print statments

# The output I will get is "True"
#
# Now that you know how classes can be extended from other classes, let's look at
# another useful built-in function called the "super()" function
#
# The super() function is a built-in function that can be called inside the derived
# class and gives access to the methods and variables of the parent classes or sibiling
# classes. Sibiling classes are the classes that share the same parent class.
# When you call he super() function, you get an object that repersents the parent class
# in return.
#
# The super() function plays an important role in multiple inheritance and helps
# drive the flow of code execution. It helps in managing or determining the control
# of from where I can draw the values of my desired functions and variables.
#
# If you change anything inside the parent class, there is direct retrieval of changes
# inside the derived class. This is mainly used in places where you need to initialize
# the functionalities present inside the parent class in the child class as well.
# You can then add additional code inside the child class. ##

# Here is an example


# Creating a class named "Fruit()" that's acting as a parent class
class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)

# Creating a class named "FruitFlavor" that's acting as a child class.
# The "FruitFlavor" class is inheriting from "Fruit"
# Note 1: Note that Python auto-completes the "super()" methods for you which
# initializes the attributes of the parent class, "Fruit".


class FruitFlavor(Fruit):
    def __init__(self):
        # super().__init__('Apple')
        print("Apple is sweet")


apple = FruitFlavor()
# Outputs:
# Fruit type: Apple
# Apple is sweet ##

# In the code above, if I had commented out the line for super() function,
# the output is
#
# Apple is sweet##

# This happens because when you initialize the child class, you don't initialze the
# base class with it. "super()" function helps you achieve this and add the
#  initialization of the base class with the derived class. ##
