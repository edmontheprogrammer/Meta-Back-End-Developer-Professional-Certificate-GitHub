# Python has different types of scopes
# * Local Scope
# * Enclosing Scope
# * Global Scope
# * Built-in Scope ##

# Note 1: The way scoping works is that the inner most function has access to almost everything
# from the outside.
# The nested items have access to both the global and the enclosed, but from the outside,
# it can't be accessed from a nested or an enclosed scope, both for the local and enclosed
#
# Note 2: Built-in scope refers to what's called the reserve keywords such as
# "print" and "def". Built-in scope covers all the language of Python, which means you can
# access it from the outermost scopes or the innermost scopes in the function classes. ##

# global scope
my_global = 10


def fn1():
    enclosed_v = 8

    # example of enclosed scope by creating 'fn2()' function and call it
    def fn2():
        # example of local scope using 'local_v = 5' which is a variable declared
        # within the fn2 function
        local_v = 5
        print('Access to Global ', my_global)
        print('Access to enclosed', enclosed_v)
    fn2()


fn1()

# Returns "NameError: name 'local_v' is not defined. Did you mean: 'locals'?"
# print('Cant access local ', local_v)
