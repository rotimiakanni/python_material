# Python has many built-in functions that can be used without defining them:
#   - See the list of built-in functions here: https://docs.python.org/3/library/functions.html
#   - Built-in functions are functions that are built into Python.
#   - Built-in functions are available for use without defining them.
#   - Built-in functions are called by using their name followed by parentheses.
#   - Built-in functions can have zero or more arguments.

# 1. abs()
#  - The abs() function returns the absolute value of a number.

print(abs(-5))  # 5
print(abs(5))  # 5

# 2. all()
#  - The all() function returns True if all elements in an iterable are true.
#  - An iterable is a sequence of elements that can be iterated over.

print(all([True, True, True]))  # True
print(all([True, False, True]))  # False


# 3. any()
#  - The any() function returns True if any element in an iterable is true.

print(any([True, True, True]))  # True
print(any([True, False, True]))  # True
print(any([False, False, False]))  # False

# 4. range()
#  - The range() function returns a sequence of numbers.
#  - The range() function can take one, two, or three arguments.

print(range(5))  # range(0, 5)
print(range(1, 5))  # range(1, 5)
print(range(1, 5, 2))  # range(1, 5, 2)
print(list(range(5)))  # [0, 1, 2, 3, 4]
