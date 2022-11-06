# Working with Methods: Examples
#
# You have learned how to use objects, classes and the methods inside them. You have covered these both in cases where
# there is only one class, as well as when there are multiple classes. You also explored how multiple inheritance works
# in Python and the role Method Resolution Order (MRO) plays in determining call for the method.
#
# The following examples demonsrate how the function call is resolved in cases of multiple inheritance in different
# scenarios. Note that all the functions have the same names in all of the examples
#
# Example 1##

# Example 1
class A:
    def a(self):
        return "Function inside A"


class B:
    def a(self):
        return "Function inside B"


class C(B, A):
    pass


# Driver code
c = C()
print(c.a())
# Outputs: Function inside B


# Class C inherits from classes B and A. When I don't find any function a() insdie class C, I should search for classes B
# and A and its important that I do it in that order.

# I will now add one more level of this and note the output.
class A:
    def b(self):
        return "Function inside A"


class B:
    def b(self):
        return "Function inside B"


class C(A, B):
    pass
    # def b(self):
    #     return "Function inside C"


class D(C):
    pass


d = D()
print(d.b())

# Class D inherits from class C, which in turn inherits from classes A and B. Class D accesses the immedidate superclass
# of class D, which is class C and resolves the value of the variable once it's found in that superclass
#
# Now let's say I commnet out the declaration inside class C
#
#   # def b(self):
#   #        return "Function inside C"##
#
#
# And replace it with the "pass" keyword to keep the code functional
#
# Since there was no value present inside class C either, the function call above would go to A. That is because class C
# point to class A as having higher precedence while inheriting.
#
# Now let's take another example of a similar scenario
#
# Example 3: ##


class A:
    def c(self):
        return "Function inside A"


class B:
    def c(self):
        return "Function inside B"


class C(A, B):
    def c(self):
        return "Function inside C"


class D(A, C):
    pass


d = D()
print(d.a)

# Outputs error: Cannot create a consistant method resolution order (MRO) for base A, C

# Note that this throws an error. In the code above, class D inherits from both class A and class D.
#
# Class C is its immedidate superclass, but since this is multiple inheritance, the rules are more complicated and it also
# has to check the classes passed to it for precedence.
#
# In this particular case, class D is unable to resolve the order that should be followed, while resolving the value for
# the variable in cases where the variable is not present in the class of the given object.
#
# It results in a TypeError because it's unable to create method resolution order (MRO). MRO is Pyhton's way of resolving
# the order of precedence of classes while dealing with inheritance.
#
# Let's examine one final example
#
# Example 4: ##


class A:
    def d(self):
        return "Function inside A"


class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E, D, C):
    pass


f = F()
print(f.d())
print(F.mro())

# The code here is simple. class F directly inherits from its immedidate superclass and the first class that is passed
# to it. The second line then demonstrates the return from the mro() function.
#
# The examples in this reading demonsrtate how to code in which multiple inheritance is used, can get complicated and
# very messy, very fast. Multiple inheritance, with all the advantages and flexibility that it can provides, should only
# be used once you have a strong command of Python as a language to avoid creating 'spaghetti code' that's difficult to
# understand and update. ##
