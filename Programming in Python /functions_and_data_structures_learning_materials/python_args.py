# def sum_of(a, b):
#     return a + b


# print(sum_of(4, 5))  # Outputs 9

# print(sum_of(4, 5, 6))  # Outputs a type error
# TypeError: sum_of() takes 2 positional arguments but 3 were given
# So you cannot add more than 2 arugments, this is where args are useful


# creating a function with args. Instead of passing two arguments
# "*args" allow us to pass "n" number of arguments
# def sum_of2(*args):
#     sum = 0
#     for x in args:
#         sum += x
#     return sum


# print(sum_of2(4, 5, 6, 4, 5, 6))


#