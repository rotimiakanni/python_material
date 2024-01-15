# My simple math module
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        # raise an exception
        raise Exception("Cannot divide by zero!")
    return a / b
