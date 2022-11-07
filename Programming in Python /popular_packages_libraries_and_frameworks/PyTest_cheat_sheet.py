# Installation:
#
# Run the following on the Terminal
#
# "pip3 install pytest"
#
#  # Nomenclature
#   * Add suffix 'test_' to the file that needs to be tested.
#   * Add suffix 'test_' to the functions to be tested
#
# Running pytest:
#
#   This is the command that has to be executed on the Terminal prompt:
#
#  "python3 -m pytest test_file.py"
#
# Alternative method:
#   "py.test" will look for the keyword test and run the tests over those files and functions
# automatically.
#
# "py.test test_file.py"
#
# When you run pytest for a specific function add :: to run a specific function in a given file.
#
# Flags used:
#
# For example, -v s the flag:
#
#   "python3 -m pytest abc.py -v"
#
# some other flag options are:
#
#   "--maxfail n specifies maximum number of test fails allowed"
#
# Tips:
#
#   * The rule of thumb is that the "assert" statment looks for a boolean result. You can use
# in, not in, is, <, > other than == to check boolean values
#
# * You can add multiple assert statments inside a single test function.  ##
