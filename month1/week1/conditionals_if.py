# Conditional statements, such as if, elif, and else, are used to execute
# different blocks of code based on different conditions.
# Control flow statements are essential for creating dynamic and efficient Python programs.

# IF STATEMENTS
# An if statement is a conditional statement that runs or skips code based on whether a condition is true or false.
# Here is a simple example:
if 8 < 9:
    print("Eight is less than nine!")  # This will print Eight is less than nine!

# In the example above, 8 < 9 is the condition being evaluated.
# Since it is true, the indented code runs.
# If it were not true, the indented code would not execute.
# Notice that the indented code begins on the next line after the colon.
# This is how Python knows that the indented code is what should be executed if the condition is true.

# Here is another example where the condition is false:
if 8 > 9:
    print("Eight is greater than nine!")  # This will not print anything

# In the example above, 8 > 9 is the condition being evaluated.
# Since it is false, the indented code does not run.
# If it were true, the indented code would execute.

# Here is an example with a variable:
age = 30
if age > 25:
    print("You are older than 25!")  # This will print You are older than 25!

default_height = 1.8
john_height = 1.7

if john_height > default_height:
    print("John is taller than average!")  # This will not print anything

# NOTE: You can use a expression that evaluates to a boolean value in an if statement.

# Here is an example with a boolean variable:
is_married = False
if is_married:
    print("You are married!")  # This will not print anything

# Here is an example with a boolean expression:
age = 30
if age > 25 and age < 35:
    print(
        "You are between 25 and 35 years old!"
    )  # This will print You are between 25 and 35 years old!


# Here is an example with a boolean variable:
is_married = False
if not is_married:
    print("You are not married!")  # This will print You are not married!


# IF/ELSE STATEMENTS
# An if/else statement is a conditional statement that runs one
# block of code if a condition is true and another if it is false.

# Here is an example:
age = 30
if age > 25:
    print("You are older than 25!")  # This will print You are older than 25!
else:
    print("You are younger than 25!")

# In the example above, the condition age > 25 is true, so the first indented code block runs.
# The second indented code block does not run because it is not indented under the else statement.
# If the condition were false, the first indented code block would not run and the second one would.

# Here is another example:
password = "12345"
if password == "12345":
    print("Password accepted!")  # This will print Password accepted!
else:
    print("Password incorrect!")

# What if we want to check more than one condition?
# We can use elif statements to check additional conditions.
# Here is an example:
age = 30
if age > 25:
    print("You are older than 25!")  # This will print You are older than 25!
elif age == 25:
    print("You are 25 years old!")
else:
    print("You are younger than 25!")

# Note: You can have as many elif statements as you want. Example:
price = 100
if price > 100:
    print("The price is greater than 100!")
elif price == 100:
    print("The price is equal to 100!")
elif price < 100:
    print("The price is less than 100!")
else:
    print("The price is not a number!")
