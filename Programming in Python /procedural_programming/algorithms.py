# Algorithm for a Palindrome

# The word "racecar" is an example of palindrome because it can be
# spelled the same both reading it forward and backward.
str = 'racecar'

# Write an algorithm that checks if the word above is a palindrome.
# print(str[0])
# print(str[6])

# First check if the value at index 0 is equal to the value at the last
# index 6.
# [0] == [6]

# Second, check if the second character is equal to the value next to the
# second to last character.
# [1] == [5]

# Finally, I need to check if chracter at index 2 is equal to the
# character at index 4
# [2] == [4]

# What, I need to do is check if the results of these conditions equal
# to "true" or "false".


def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True


print(isPalindrome('racecar'))
