import calendar
import sys

# Accessing modules: ##
locations = sys.path

for i in locations:
    print(i)

print(locations)

# Outputs first time: NameError: name 'sys' is not defined ... therefore you must import the
# 'sys' module

# Outputs Second time: no errors. All good.


leapdays = calendar.leapdays(2000, 2050)
print(leapdays)

isitleap = calendar.isleap(2036)
print(isitleap)
