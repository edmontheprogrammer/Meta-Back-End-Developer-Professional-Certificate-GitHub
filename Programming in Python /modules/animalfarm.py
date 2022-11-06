# Creating a function named "d" with a variable called "animal"
def d():
    animal = 'elephant'

    # Creating a nested function named "e" that has a "nonlocal animal"
    # "animal = 'giraffe' " and prints animal
    def e():
        nonlocal animal
        animal = "giraffe"
        print("Inside the nested function: " + animal)

    # printing the 'animal' variable
    print("Before calling functions: " + animal)


animal = "camel"
d()
print("Global animal: " + animal)
