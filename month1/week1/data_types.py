# Data types essential building blocks of Python programming.

# A data type is a classification of data which tells the compiler or interpreter
# how the programmer intends to use the data. Most programming languages support
# basic data types of:
# - Integer numbers (of varying sizes),
# - Floating-point numbers (which approximate real numbers)
# - Characters
# - Booleans.
# A data type constrains the operations that can be done on the data, the meaning of the
# data, and the way values of that type can be stored.


# Python has the following data types built-in by default:
# Text Type: str
first_name = "John"
last_name = "Adeyemi"  # This is a string
print(type(last_name))  # This will print <class 'str'>

# Because first_name and last_name are strings, the operator + will concatenate them (join them together)
# instead of adding them together like it did for the numbers.
full_name = first_name + " " + last_name
print(type(full_name))  # This will print <class 'str'>


# Numeric Types: int, float, complex
#  - Integers, or int, are whole numbers, positive or negative, without decimals, of unlimited length.
age = 30  # This is an integer
planet_distance = 149600000  # This is also an integer
a_big_number = 123456789012345678901234567890  # This is also an integer
temperature = -10  # This is also an integer
print(type(temperature))  # This will print <class 'int'>

# - Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# - Float can also be scientific numbers with an "e" to indicate the power of 10.
height = 1.8  # This is a float
pi = 3.14  # This is also a float
c = 3 * 10**8  # This is also a float
plank_constant = 6.62607004e-34  # This is also a float in scientific notation
print(type(plank_constant))  # This will print <class 'float'>

# - Complex numbers are written with a "j" as the imaginary part.
# - Complex numbers are not used much in Python programming.
complex_number = 3 + 5j  # This is a complex number
print(type(complex_number))  # This will print <class 'complex'>


# Boolean Type: bool
#  - Booleans represent one of two values: True or False.
is_married = False  # This is a boolean
is_single = True  # This is also a boolean
print(type(is_married))  # This will print <class 'bool'>

# Some advanced data types which we will cover later in the course include:
#    - Sequence Types: list, tuple, range
#    - Mapping Type: dict
#    - Set Types: set, frozenset

# You can convert from one type to another using the following built-in functions:

#  - int() constructs an integer number from an integer literal,
#    a float literal (by rounding down to the previous whole number),
#    or a string literal (providing the string represents a whole number)
age = "30"
print(type(age))  # This will print <class 'str'>
age = int(age)  # This will convert the string '30' to an integer 30
print(type(age))  # This will print <class 'int'>

height = 1.8
print(type(height))  # This will print <class 'float'>
height = int(height)  # This will convert the float 1.8 to an integer 1
print(type(height))  # This will print <class 'int'>

# This will fail because the string 'John' cannot be converted to an integer
# name = "John"
# name = int(name)


# - float() constructs a float number from an integer literal, a float literal
#   or a string literal (providing the string represents a float or an integer)
temperature = "30"
print(type(temperature))  # This will print <class 'str'>
temperature = float(temperature)  # This will convert the string '30' to a float 30.0
print(type(temperature))  # This will print <class 'float'>

price = 30
print(type(age))  # This will print <class 'int'>
age = float(age)  # This will convert the integer 30 to a float 30.0
print(type(age))  # This will print <class 'float'>

# This will fail because the string 'John' cannot be converted to a float
# name = "john3:16"
# name = float(name)


# - str() constructs a string from a wide variety of data types,
#   including strings, integer literals and float literals
age = 30
print(type(age))  # This will print <class 'int'>
age = str(age)  # This will convert the integer 30 to a string '30'
print(type(age))  # This will print <class 'str'>

height = 1.8
print(type(height))  # This will print <class 'float'>
height = str(height)  # This will convert the float 1.8 to a string '1.8'
print(type(height))  # This will print <class 'str'>

is_male = True
print(is_male)  # This will print True
is_male = str(is_male)  # This will convert the boolean True to a string 'True'
print(type(is_male))  # This will print <class 'str'>
