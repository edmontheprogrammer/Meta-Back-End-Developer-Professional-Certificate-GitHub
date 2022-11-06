# Exercise: Working with Methods:
#
# 1. Guess the output for the following block of code and try running the code once you have a
# solution in mind: ##

# # Creating a class named "A" that returns a string "Function inside A"
# class A:
#     def b(self):
#         return "Function inside A"

# # Creaing a class named "B" that does nothing


# class B:
#     pass

# # Creating a class named "C" that returns the string "Function inside C"


# class C:
#     def b(self):
#         return "Function inside C"

# # Creating a class named "D" that inherits from "B", "C" and "A"
# # "D" class does nothing


# class D(B, C, A):
#     pass


# # creating an instance of "D" class named "d"
# d = D()
# print(d.b())

# Outputs: "Function inside C"

# Guess the output for the following block of code and try running the code once you have made
# a solution##
# class A:
#     def c(self):
#         return "Function inside A"


# class B(A):
#     def c(self):
#         return "Function inside B"


# class C(A, B):
#     pass


# class D(C):
#     pass


# d = D()
# print(d.a)

# Outputs: Error: TypeError: cannot create a consistent method resolution order (MRO) for bases
# A, B

# Guess the output for the following block of code and try running the code once you have a
# solution in mind: ##
class A:
    pass


class B(A):
    pass


class C(B):
    pass


c = C()
print(c.a())

# Output: AttributeError: 'C' object has no attribute 'a'
