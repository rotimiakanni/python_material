# Operators include arithmetic operators (+, -, *, /),
# comparison operators (==, !=, <, >), and logical operators (and, or, not).
# These operators are used to manipulate variables and expressions.

# ARITHMETIC OPERATORS
# Addition
print(1 + 2)  # This will print 3
print(1.5 + 2.5)  # This will print 4.0
print(1 + 2.5)  # This will print 3.5

# Subtraction
print(1 - 2)  # This will print -1
print(1.5 - 2.5)  # This will print -1.0
print(1 - 2.5)  # This will print -1.5
print(300 - 200)  # This will print 100


# Multiplication
print(2 * 3)  # This will print 6
print(2.5 * 3.5)  # This will print 8.75
print(2 * 30)  # This will print 60

# Division
print(4 / 2)  # This will print 2.0
print(4.5 / 2.5)  # This will print 1.8
print(4 / 2.5)  # This will print 1.6
print(300 / 200)  # This will print 1.5

# COMPARISON OPERATORS
# Equal to
print(1 == 1)  # This will print True

# Not equal to
print(1 != 2)  # This will print True

# Greater than
print(2 > 1)  # This will print True

# Less than
print(1 < 2)  # This will print True

# Greater than or equal to
print(2 >= 1)  # This will print True

# Less than or equal to
print(1 <= 2)  # This will print True


# LOGICAL OPERATORS
# and
print(True and True)  # This will print True
print(True and False)  # This will print False
print(False and False)  # This will print False

# or
print(True or True)  # This will print True
print(True or False)  # This will print True
print(False or False)  # This will print False

# not
print(not True)  # This will print False
print(not False)  # This will print True

# OTHER OPERATORS
# Modulus: This will divide and return the remainder.
print(5 % 2)  # This will print 1

# Floor division: This will divide and return the integer value of the quotient.
print(5 // 2)  # This will print 2

# Exponentiation: This will raise the first number to the power of the second number.
print(2**3)  # This will print 8
print(2**0.5)  # This will print 1.4142135623730951


# ASSIGNMENT OPERATORS
# =: This assigns the value on the right to the variable on the left.
x = 1
print(x)  # This will print 1

# +=: This adds the value on the right to the variable on the left and assigns the result to the variable on the left.
x += 1  # This is equivalent to x = x + 1
print(x)  # This will print 2

# -=: This subtracts the value on the right from the variable on
# the left and assigns the result to the variable on the left.
x -= 1  # This is equivalent to x = x - 1
print(x)  # This will print 1

# *=: This multiplies the value on the right with the variable on
# the left and assigns the result to the variable on the left.
x *= 2  # This is equivalent to x = x * 2
print(x)  # This will print 2

# /=: This divides the variable on the left by the value on the right
# and assigns the result to the variable on the left.
x /= 2  # This is equivalent to x = x / 2
print(x)  # This will print 1.0

# You can also combine arithmetic operators with assignment operators
x += 1  # This is equivalent to x = x + 1


# OPERATOR PRECEDENCE
#  - Operator precedence determines the order in which operators are evaluated.
#  - Operators with higher precedence are evaluated first.
#  - Operators with the same precedence are evaluated from left to right.
#  - You can use parentheses to override the default precedence.
# The following list shows the precedence of operators in Python, from highest to lowest:
# 1. Parentheses: ()
# 2. Exponentiation: **
# 3. Multiplication, Division, Floor Division, Modulus: *, /, //, %
# 4. Addition, Subtraction: +, -
# 5. Comparison Operators: ==, !=, <, >, <=, >=
# 6. Logical Operators: not, and, or
# 7. Assignment Operators: =, +=, -=, *=, /=, //=, %=, **=

# Examples
print(2 + 3 * 4)  # This will print 14, not 20, because multiplication has higher precedence than addition
print((2 + 3) * 4)  # This will print 20, because parentheses have higher precedence than multiplication
print(2 + 3 * 4 ** 2)  # This will print 50, not 288, because exponentiation has higher precedence than multiplication
print((2 + 3 * 4) ** 2)  # This will print 400, because parentheses have higher precedence than exponentiation
print(2 + 3 * 4 == 14)  # This will print True, because comparison operators have higher precedence than logical operators
print(2 + 3 * 4 == 20 and 2 + 3 * 4 == 14)  # This will print False, because logical operators are evaluated from left to right
# We can do the evaluation of the expression above step by step

# OPERATORS ON VARIABLES
# You can use operators on variables
x = 1
y = 2
print(x + y)  # This will print 3
print(x == y)  # This will print False
print(x != y)  # This will print True
print(x > y)  # This will print False


# OPERATOR PRECEDENCE EXERCISE
# What is the result of this expression?
# 2 + 3 * 4 == 14 or 2 + 3 * 4 == 20
