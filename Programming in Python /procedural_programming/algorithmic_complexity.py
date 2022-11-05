# Algorithmic Complexity:

# Code is measured by time and space. Time is measured by how long it
# takes and space is about how much memory it uses.
#
# Big O notation:
#   Big O has different complexities or categories ranging from horrible
# to excellent. It's used to measure an algorithm's efficiency in terms
# of time and space.
#
# Constant time:
#  This is an algorithm that will always run under the same time and space
# regardless of the size. Take a dictionary for example, to get the value
# of an item, you need to have the key, the key is a direct pointer to the
# value and does not require any iteration is to find it.
# It's considered constant.
#
#    Dictionary
#       Drinks = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
#       print(Drinks[2])
#       Outputs: Tea
#
# Linear time:
#   Second is a linear time algorithm. This will grow depending on the
#  size of the input. For example, if I have an array of numbers with
#  a range of 100, it will run very fast. But it it's increased to a
# million, it will take a lot longer to complete. The size in this case
# affects the running time of the code.
#
#  # the bigger the range, the bigger the running time!
#   for x in range(100):
#         print(x)
#
# Logarithmic Time:
#   Third, a logarithmic time refers to the running time of the inputs
# against the number of operations. I can take a linear approach to try
# to find a number out of 100. Let's say the number is 97.
# In a linear equation, it will take 96 iterations before it's found.
# This is because it must iterate through each item one by one until
# it finds the target value. The binary search works by splitting the list
# into two parts each time to check if a target is less than or greater
# than one
#
# def find_num(num):
#     count = 0
#     for x in range(100):
#         if x == num:
#             print("Total Iterations: " + str(count))
#             return x
#         count += 1


# find_num(97)
# Outputs: "Total Iterations: 96"

# # Using a binary search, I can cut down the iterations and find it on the
# # seven iterations. This is measured by logarithmic time.


# def find_number_log(target):
#     iterations = 0
#     x = range(100)
#     left = 0
#     right = len(x) - 1

#     while left <= right:
#         iterations += 1
#         middle = (left + right) // 2
#         isNumber = x[middle]

#     if target == isNumber:
#         print("Iterations", iterations)
#         return middle
#     elif target < isNumber:
#         right = middle - 1
#     else:
#         left = middle + 1

#         return -1


# print(find_number_log(97))


# Quadratic Time:
#   Fourth, quadratic time refers to to a linear operation of each value
# of the input data squared. This is often a nested list, as in this
# for-loop. This for-loop is considered quadratic time as the outter loop
# will need to iterate in a linear way 10 times. But it also has to iterate
# the inner loop the same 10 times for each single outer loop. This means
# it's total iterations are 100 iterations
#
# for x in range(10):
#     for y in range(10):
#         print(x, y)

# Exponential Time:
#  Fifth and last is exponential time, which is an algorithm that doubles
# with each iteration. The Fibonacci sequence is a prime example of this.
#  ##
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
