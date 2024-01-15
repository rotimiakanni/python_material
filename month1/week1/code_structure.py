# Proper code structure in Python requires correct indentation, whitespace, and comments.
# Let's look at each of these in detail.

# INDENTATION
if 5 > 2:
    print("Five is greater than two!")

# This code will fail because the print statement is not indented
# if 5 > 2:
# print("Five is greater than two!")

# The following code will fail because there is no indentation between the print statements
# print("Hello")print("World")

# WHITESPACE
# Use whitespace to make your code more readable. e.g. The following code is more readable


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


# This code is less readable because there is no whitespace between the functions
# def multiply(x, y):
#     return x*y
# def divide(x, y):
#     return x/y


# COMMENTS
# Comments are used to explain what the code does. Comments are ignored by the Python interpreter.
# Comments start with a # symbol.

# You can write comments on a separate line or on the same line as the code.
# This is a comment
print("Hello World")  # This is also a comment

# You can also write multi-line comments using triple quotes. For example:
"""
This is a multi-line comment
This is a multi-line comment
This is a multi-line comment
"""

# You can also use comments to disable code. For example:
# print("Hello World")
# print("This will not print")
