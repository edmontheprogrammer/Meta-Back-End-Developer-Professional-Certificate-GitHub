def divide_by(a, b):
    return a / b


# print(divide_by(40, 4))  # Outputs: 10.0
# divide_by(40, 0) # Outputs: ZeroDivisionError: division by zero because you cannot
# divide by zero. Therefore, this code outputs an error to the users
# Now to prevent this error from happening, we can wrap it around the "try-except block"

# How can you handle errors in a more user friendly way? How can you prevent the user
# from seeing the actual exception being printed out?  You do this with Python's
# "try and except" statments. You add the code you want to run within the "try" statment
# "ans = divide_by(40, 0)". Now in the "except" you add your own error statment such
# as "print('something went wrong')"
#
# The "try" statment will try and execute the code that you added inside it.
#  If an exception occurs, it will trigger th except line and execute any code added
# underneath the "except" statment. But Python allows you to make the except statment
# more specific. If you want to trap the exception itself you could add the base class
# exception right after except. The base class exception is used for all exceptions that
# are written within Python. you can gain access to the exception information by using
# "as e" after "exception". The "e" variable acts as an alias for the "exception"
# You can use "e" to print "exception" in the statment ##
# try:
#     ans = divide_by(40, 0)
# except Exception as e:
#     print("Something went wrong! ", e)
#     print(e.__class__)

try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
except Exception as e:
    print(e, "something went wrong")

# Outputs: Something went wrong!  division by zero
