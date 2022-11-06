# Exercise: Classes and object exploration:
#
# In this reading, you'll explore the behaviors of functions, objects and classes in
# Python and how the flow of execution of different program statment works for
# to enable better understanding.
#
# you will perform minor monditifcations in the given code to observe how it changes
# the output.
#
# First, set up a file called "class_explore.py" that contains the following pice of
# code. Alternatively, you can use the interactive environment here.  ##

class A:
    # The "init()" method simply initializes the variable 'self.c' to the input parameter
    # 'c'
    def __init__(self, c):
        print("---------Inside class A----------")
        self.c = c
    print("Print inside A.")

    # The "alpha()" method modfies the value of 'c' by incrementing it by 1 and
    # then it returns the updated "c" value.
    def alpha(self):
        c = self.c + 1
        return c


print(dir(A))
print("Instantiating A..")
# Creating an instance of the "A()" class named 'a'
a = A(1)
# calling the "alpha()" method of the "a" object.
print(a.alpha())


class B:
    # The "init()" method simply initializes the variable "self.a" to the input
    # parameter a
    def __init__(self, a):
        print("---------Inside class B----------")
        self.a = a

    print(a.alpha())
    d = 5
    print(d)
    print(a)


print("Instantiating B..")
b = B(a)
print(a)
