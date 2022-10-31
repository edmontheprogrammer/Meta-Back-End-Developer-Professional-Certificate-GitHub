# In Python we can create new files using the open function and enabling the
# write mode. Let's start with a short example. I'll use the "with" statment with the
# "open" function and pass in the following parameters. Out file will be "newfile.txt"
#  and we'll set the mode by passing mode equal to "w". Now, I assign this file to a
# variable by typing "as file".
# Now I can add contents to the file using the "write()" function.
# newfile.txt has been generated as a new file. ##

with open('newfile2.txt', mode='w') as file:
    file.write("This is a new file created!")
