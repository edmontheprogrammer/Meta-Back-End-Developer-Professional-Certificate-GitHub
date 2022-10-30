# sets are data structure that does not allow duplicate values.
# Set is a collection with no duplicate items and it's also a collection of unordered
# items. You cannot print items in the set by index because it's a collection of
# unordered items.
set_a = {1, 2, 3, 4, 5, 5}
set_b = {4, 5, 6, 7, 8}


# performing math calcuation on sets
#
# union:
# union() combines two sets into one and removes any duplicate values.
# print(set_a.union(set_b))
# The or '|' symbol has the same affect on sets like the union() method. That is the
# '|' combines two sets into one and removes any duplciate values from the set.
# print(set_a | set_b)

# Intersection:
# The intersection() method gives us items that are both in set_a and set_b.
# For example, '4' and '5' are both in set_a and set_b, therefore the print function
# outputs {4, 5} because both items exists in the two sets.
# print(set_a.intersection(set_b))
# The '&' symbol can be used to repersent the intersection of two sets too
# print(set_a & set_b)  # The output is the same {4, 5}

# difference:
# The difference() method gives us items that are in set_a but not in set_b
# print(set_a.difference(set_b))  # Outputs {1, 2, 3}
# You can also repersent difference or the difference method using the '-' minus symbol
# print(set_a - set_b)  # Outputs {1, 2, 3}

# symmetric difference function:
# Symmetric difference method gives us list of items that are unquie from both sets
# in other words, symmetric difference method returns all the elements that are present
# in set_a and in set_b but NOT present in both sets (set_a and set_b)
# Outputs: {1, 2, 3, 6, 7, 8}
print(set_a.symmetric_difference(set_b))
# Symmetric difference can also be repersented by the carrot operator
print(set_a ^ set_b)

# print(set_a)
# set_a.remove(2)

# discard() is another method that does the same thing as remove(). It removes
# an item from the set if found.
# set_a.discard(2)
