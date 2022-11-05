# Creating a base class named "Employee()" with two attributes "name" and "last"
class Employees():
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last


# Creating a subclass or child class named "Supervisor" that inherits all the properties
# of the "Employee" class or parent class.
class Supervisor(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        # "password" is a new attributes that is specific to the "Supervsior" class
        # It's an additional "attribute" that is access only from the Supervsior's
        # base class or an instance of the "Supervisor()" class
        self.password = password

# Creating a new class named "Chefs" that also "inherits" from the "Employees" class
# Note 1: The "Chef()" class creates a new method named "leave_request()" that's
# specific only to the "Chefs" class. The "leave_request()" method is not accessiable
# from the "Employees" or "Supervisor" class.


class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days"


# Note 2: Creating instances of the classes we created above.
adrian = Supervisor("Adrian", "A", "apple")

emily = Chefs("Emily", "A")
Juno = Employees("Juno", "A")

print(emily.leave_request(3))
print(adrian.password)
print(emily.name)
