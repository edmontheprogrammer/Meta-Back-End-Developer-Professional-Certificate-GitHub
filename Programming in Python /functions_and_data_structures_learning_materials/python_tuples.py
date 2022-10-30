my_tuple = (1, 'strings', 4.5, True)

# print(my_tuple[1])

# print(type(my_tuple))

my_tuple2 = 1, 'strings', 4.5, True

# print(my_tuple2.count('strings'))

# print(my_tuple.index(4.5))

# Iterating over a tuple

for x in my_tuple2:
    print(x)


# Unlike list, tuple values are immutable. Tuple values cannot be change
# Outputs TypeError: 'tuple' object does not support item assignment
# my_tuple2[0] = 5
