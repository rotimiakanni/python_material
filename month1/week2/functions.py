# A function is a block of code that performs a specific task and can be called by other parts of the program.
#  - Functions are used to avoid repetition of code.
#  - Functions can be called as many times as needed.

# 1. Defining a function
#  - A function is defined using the def keyword.
#  - The function name is followed by parentheses and a colon.
#  - The function body is indented.
#  - The function body can contain any number of statements.


def greet():
    print("Welcome to the world of functions!")


def add():
    print(2 + 3)


# 2. Calling a function
#  - A function is called by using its name followed by parentheses.
#  - The function call must be placed after the function definition.
#  - A function can be called as many times as needed.
greet()
add()

# Calling a function again
greet()
add()

# 3. Function parameters and arguments
#  - A function can have zero or more parameters.
#  - Parameters are variables that are used to receive values from the function call.
#  - Parameters are defined inside the parentheses of the function definition.
#  - Parameters are separated by commas.
#  - Parameters are optional. A function can have zero parameters.
#  - Parameters are used in the function body like any other variable.


def greet(name):  # name is a parameter
    print("Welcome to the world of functions, " + name + "!")


def add(a, b):  # a and b are parameters
    print(a + b)


#  - When a function is called, the values passed to the function are called arguments.
#  - Arguments are assigned to the parameters in the function definition.
#  - The number of arguments must match the number of parameters.
#  - The order of arguments must match the order of parameters.
#  - Arguments are passed to the function by position.
#  - Arguments can be passed by keyword.
#  - Arguments can be passed by position and keyword.

greet("John")  # "John" is an argument
add(2, 3)  # 2 and 3 are arguments. 2 is assigned to a and 3 is assigned to b
add(a=2, b=3)  # keyword arguments - 2 is assigned to a and 3 is assigned to b

add(3)  # TypeError: add() missing 1 required positional argument: 'b'


# 4. Return values
#  - A function can return a value to the caller.
#  - The return keyword is used to return a value.
#  - The return keyword can be used anywhere in the function body.
#  - A function can return any type of value.
#  - A function can return multiple values. The values are returned as a tuple.
#  - A function can return None. This is the default return value.


def add(a, b):
    return a + b


def full_name(first_name, last_name):
    return first_name + " " + last_name


def velocity(distance, time):
    result = distance / time
    return result


def early_return():
    for i in range(10):
        if i == 5:
            return i  # returns 5 and exits the function
        print(i)


def user_details(name, age):
    return name, age  # returns a tuple containing name and age
