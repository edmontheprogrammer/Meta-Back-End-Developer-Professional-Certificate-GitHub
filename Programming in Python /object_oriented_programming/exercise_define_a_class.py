# Exercise: Define a Class:
#
# Example 1: ##
class House:
    '''
    This is a stub for a class representing a hosue that can be used to create objects and 
    evaluate
    '''
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self):
        print(self.num_rooms)
        pass
    # Functionality to calculate the costs from the area of the house.


# Note 1: The code completely defines the class and functions present inside it, but it is
# effectively not useful unless you call or instantiate it. You can do this by one of the two ways:
# Calling the class directly or instanating an object of that class. ##
house = House()
# print(house.num_rooms)
# print(house.num_rooms)

house.num_rooms = 7
# print(house.num_rooms)
# print(House.num_rooms)

# This time, instead of an instance attribute, you will modify the class attribute by directly
# calling it over the class as follows:
House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)

# You will notice that the changes on a class attribute will affect even the instances that you
# will create over it. Also, note the use of the keyword "self" in this example. "self" is
# a convention in Python, and you may use any other word in its place, but as a practice, it is
# easy to recognize. "self" here is passed inside the method "cost_evaluation()" as it is an
# instance method and facilitates the method to point to any instance of the House when that
# method is called. It should be noted how any number of parameters can be passed to these
# instance methods but the first one is always the reference to the instance of that class.
