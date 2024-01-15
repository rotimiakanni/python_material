# An abstract base class (ABC) is a class that can't be instantiated directly
# and serves as a template for other classes to inherit from.
# In Python, abstracts classes are created by subclassing the built-in ABC class in the abc module.
from abc import ABC, abstractmethod


class Product(ABC):
    # This is an abstract method.
    # It doesn't have a body and must be implemented in the child classes.
    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


# We can't create an instance of an abstract class.
# product = Product()  # This will raise a TypeError

# Let's create a class called Book that inherits from the Product class.
class Book(Product):
    def __init__(self, name, price, author):
        self.name = name
        self.price = price
        self.author = author

    def get_details(self):
        return f"{self.name} by {self.author}"

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


book1 = Book("Harry Potter", 20, "J. K. Rowling")
print(book1.get_details())
print(book1.get_price())
print(book1.get_name())
