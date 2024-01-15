# First, we need to import the module we want to use.
# We do this by using the import keyword followed by the name of the module.
# In this case, we want to import the my_math_lib module.
import my_math_lib as math_lib  # math_lib is an alias for my_math_lib

num1 = 10
num2 = 5

# Now we can use the functions in the my_math_lib module.
print(math_lib.add(num1, num2))
print(math_lib.subtract(num1, num2))
print(math_lib.multiply(num1, num2))
print(math_lib.divide(num1, num2))
