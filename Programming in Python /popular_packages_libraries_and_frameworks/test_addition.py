
# Writing Tests with PyTest:
# PyTest is a testing framework allowing users to write test codes that use the Python
# programming language.
#
# Step 0: Install pytest in your project with: "pip install pytest"
#
# Step 1:
#   import the file that contains the functions that need to be tested.   ##
import addition

# Step 2:
#  import the pytest module ##
import pytest

# Step 3: Define a couple of test cases with the "adition" and "subtrction" functions
# Note 1: Each test case should be named "test_name_of_the_function_to_be_tested" ##

# Step 4: Use the "assert" keyword inside the test functions because pytest primarily
# rely on the "assert" for testing .
#  * assert keyword:
#      The assert keyword checks for conditions in your code and expect a boolean value
# of "true" or "false". When the return value is "true" the test passes, and when the
# return condition or value is "false" the test fails.  ##

# Example 1 of writing test case using pytest


def test_addition():
    assert addition.add(4, 5) == 9

# Example 2 of writing test case using pytest


def test_sub():
    assert addition.sub(4, 5) == -2

# Step 5: run pytest and specify the file over which you'll be doing the testing.
# for example run " python -m pytest test_addition.py "  ##

# Outputs: Collected 2 items ... 2 passed in 0.01s meaning both test cases were passed!
