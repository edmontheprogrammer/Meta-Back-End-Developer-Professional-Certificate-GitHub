# sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
# print(sample_dict[1])  # Outputs Coffee
# sample_dict[2] = 'Mint Tea'

# # deleting an item from a dictionary
# # Deletes the key-value pair " 3: 'Juice' " from the dictionary
# del sample_dict[3]
# my_d = {1: 'Test', 'Name': 'Jim'}

# my_d[2] = 'Test 2'

# my_d[1] = 'Not a test!'

# print(my_d)


my_d = {1: 'Test', 'Name': 'Jim'}

# Iterating over a dictionary
# This only prints the keys of the dictionary
# for x in my_d:
#     print(x)

# This prints the key-value pairs
for key, value in my_d.items():
    print(str(key) + " : " + value)
