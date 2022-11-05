# Exercise: Instantiate a custom Object
# This is your first experince creating classes and objects in Python. You will be
# following a sequential process where you will be create a class, define its state
# by creating variables and functions to define its attributes and behavior, and then
# instanitate it using some variable. Finally, you will use the class members to get
# the desired output.
#
# Follow the steps to build nd run your program in the environment provided at the
# bottom of the reading ##

class MyFirstClass:
    print("Who wrote this?")
    index = "Author-Book"

    def hand_list(self, philospher, book):
        self.philosher = philospher
        self.book = book
        print(MyFirstClass.index)
        print(self.philosher + " wrote the book: " + self.book)


MyFirstClass_object_1 = MyFirstClass()
philosher_info_1 = MyFirstClass_object_1.hand_list("Plato", "Republic")

whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")
