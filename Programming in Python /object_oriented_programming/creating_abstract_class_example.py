# Step 1 Import the "ABC" class
from abc import ABC, abstractmethod

# Step 2: Create a class such as "someAbstractClass"


class SomeAbstractClass(ABC):
    @abstractmethod
    def someabstractmethod(self):
        pass

# Step 3: Pass in the ABC Module so that it inherits that class.

# Step 3B: Import the abstract method decorator inside the same module
# A doecorator is s a function that takes another function as its arugment and gives
# a new function as its output. decorator is denoated by the @ sign ##

# Step 4: Call the abstract method ##
