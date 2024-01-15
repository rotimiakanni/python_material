# Handling errors and exceptions is an important part of building robust and reliable programs.
# In Python, we can handle errors and exceptions using the try...except...else clause.
#   - The try clause is used to run code that may raise an exception.
#   - The except clause is used to handle exceptions.
#   - The else clause is used to run code if no exception is raised.
#   - The finally clause is used to run code regardless of whether an exception is raised.
#   - The raise statement is used to raise an exception.
#   - The assert statement is used to raise an AssertionError if a condition is False.

# Example: Handle an exception using the try...except clause.
try:
    # code that may raise an exception
    print(1 / 0)
except ZeroDivisionError:  # The type of exception to handle
    # code to handle the exception
    print("Cannot divide by zero")

# Example: Handle multiple exceptions using the try...except clause.
# To see a list of built-in exceptions, visit https://docs.python.org/3/library/exceptions.html
# It is important to handle specific exceptions rather than using a generic except clause.
try:
    # code that may raise an exception
    print(1 / 0)
except ZeroDivisionError:  # The type of exception to handle
    # code to handle the exception
    print("Cannot divide by zero")
except ValueError:  # The type of exception to handle
    # code to handle the exception
    print("Invalid value")


# Example: Handle an exception using the try...except...else clause.
try:
    # code that may raise an exception
    print(3 / 1)
except ZeroDivisionError:  # The type of exception to handle
    # code to handle the exception
    print("Cannot divide by zero")
else:
    # code to run if no exception is raised
    print("Division successful")

# Example: Handle an exception using the try...except...finally clause.
try:
    # code that may raise an exception
    print(1 / 1)
except ZeroDivisionError:  # The type of exception to handle
    # code to handle the exception
    print("Cannot divide by zero")
finally:
    # code to run regardless of whether an exception is raised
    print("Division attempt complete")


# Example: Raise an exception using the raise statement.
# The raise statement is used to raise an exception.
# The raise statement can be used with or without an exception type and a description.
#   - raise: raise the last exception
#   - raise <exception>: raise an exception of type <exception>
#   - raise <exception>(<description>): raise an exception of type <exception> with <description>

# Example: Raise an exception using the raise statement.
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError(
            "Cannot divide by zero"
        )  # raise an exception with a description
    return a / b


print(divide(1, 0))

# Assertions
# Assertions are used to check if a condition is True.
# If the condition is False, an AssertionError is raised.
# Assertions are used to check for programmer errors.
# Assertions can be disabled by passing the -O flag when running Python.
# Assertions should not be used to handle runtime errors.
# Assertions should not be used to handle user errors.
# Assertions should not be used to handle expected errors.


# Example: Raise an AssertionError if a condition is False.
def divide(a, b):
    assert b != 0, "Cannot divide by zero"  # raise an AssertionError if b is 0
    return a / b
