# Python Classes and Instances:
#
# Note 1: Everything in Python is an object or derived from the object class.
# ##

class MyClass:
    a = 5

    def hello(self):
        print("Hello, world!")


myc = MyClass()
print(myc.a)
print(myc.hello())
