class Payslips:
    # Creating an "init" method that initializes all the attributes of the "Payslips"
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    # Creating a method named "pay" that initializes the "self.payment" attribute to
    # "yes"
    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet "


# Creating an instance of the "Payslip"
nathan = Payslips("Nathan", "No", 1000)
# Creating another instance of the "Payslip" class named "Rodger"
rodger = Payslips("Rodger", "No", 3000)

# Note 1: the "status" method gives us information about the employees
# Note 2: the "status" method outputs information based on "yes" or "no" inputs
print(nathan.status(), "\n", rodger.status())

# Changing the status (calling the "status()" method on the object nathan).
nathan.pay()
print("After payment")
print(nathan.status(), "\n", rodger.status())
