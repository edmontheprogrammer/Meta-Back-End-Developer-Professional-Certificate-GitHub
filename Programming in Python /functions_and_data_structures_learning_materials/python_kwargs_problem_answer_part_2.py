# Problem: Let's say  you want to calculate a total bill for a restaurant.
# A user got a cup of coffee that was 2.99, then they got a cake for 4.55
# and also a juice for 2.99.
# (coffee=2.99, cake=4.55, juice=2.99)
# Write a function that will calculate the total bill for the order of items
# and print the bill ##

def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)


print(sum_of(coffee=2.99, cake=4.55, juice=2.99))

# Summary: 
#   To summarize, with "args", you could pass in any amount of 
#   non-keyword variables. With "kwargs" you can pass in any amount 
#   of keyword arguments. ##