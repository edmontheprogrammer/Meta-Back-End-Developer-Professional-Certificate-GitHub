
# # Example of calculating tax amount without using a
# # function ##

# # this is a float data type
# bill = 175.00

# # tax_rate is 15, the number 15 is the percentage of the
# # tax amount we will be deducting from the bill
# tax_rate = 15

# # this is how you calcuate the tax rate for the bill you have
# total_tax = (bill * tax_rate) / 100.00

# # printing the total tax for the bill
# print('Total tax ', total_tax)


# Example of writing a function that will calcuate a
# tax amount for a customer based on the total value
# of the bill ##
def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100, 2)


print('Total tax: ',  calculate_tax(175.00, 15))

print('Total tax: ',  calculate_tax(164.33, 22))
