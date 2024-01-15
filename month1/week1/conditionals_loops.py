# Looping constructs, such as for loops and while loops,
# are used to repeat blocks of code until a certain condition is met.

# FOR LOOPS
# A for loop is used to iterate over a sequence (i.e. a list, tuple, set, dictionary, or string).
# Here is a simple example:
for i in range(5):
    print(i)  # This will print 0, 1, 2, 3, 4

# In the example above, range(5) is the sequence being iterated over.
# The variable i is assigned to each element in the sequence in order.
# The indented code is executed for each element in the sequence.
# The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and stops before a specified number.

# Here is another example:
for i in "Hello":
    print(i)  # This will print H, e, l, l, o

# In the example above, the sequence is the string "Hello".
# string is a sequence of characters, so each character is assigned to the variable i in order.
# The indented code is executed for each character in the string.

# Here is another example:
for i in [1, 2, 3, 4, 5]:
    print(i)  # This will print 1, 2, 3, 4, 5

# In the example above, the sequence is the list [1, 2, 3, 4, 5].
# The indented code is executed for each element in the list.

# Here is another example:
for i in (1, 2, 3, 4, 5):
    print(i)  # This will print 1, 2, 3, 4, 5

# In the example above, the sequence is the tuple (1, 2, 3, 4, 5).
# The indented code is executed for each element in the tuple.


# WHILE LOOPS
# A while loop is used to repeat a block of code while a condition is true.
# Here is a simple example:
i = 0
while i < 5:
    print(i)  # This will print 0, 1, 2, 3, 4
    i += 1

# In the example above, the condition i < 5 is true, so the indented code runs.
# The variable i is incremented by 1 each time the indented code runs.
# The condition is checked again, and the indented code runs again.
# NB: The condition must eventually become false, otherwise the loop will run forever.


# BREAK STATEMENTS
# A break statement is used to exit a loop.
# Here is an example wth a for loop:
for i in range(5):
    print(i)  # This will print 0, 1, 2, 3, 4
    if i == 3:
        break  # This will exit the loop when i is 3

# In the example above, the condition i < 5 is true, so the indented code runs.
# The variable i is incremented by 1 each time the indented code runs.
# An if statement is used to check if i is 3. If it is, the break statement is executed
# and the loop is exited. If it is not, the loop continues.

# Here is the smae example wth a while loop:
i = 0

while i < 5:
    print(i)  # This will print 0, 1, 2, 3, 4
    i += 1
    if i == 3:
        break  # This will exit the loop when i is 3

# In the example above, the condition i < 5 is true, so the indented code runs.
# The variable i is incremented by 1 each time the indented code runs.
# An if statement is used to check if i is 3. If it is, the break statement is executed
# and the loop is exited. If it is not, the loop continues.

# CONTINUE STATEMENTS
# A continue statement is used to skip the rest of the code in a loop and start the next iteration.
# Here is an example wth a for loop:
for i in [0, 1, "skip me", 3, 4]:
    if i == "skip me":
        continue  # This will skip the rest of the code in the loop when i is 3
    print(f"i: {i}")  # This will print 0, 1, 2, 4

# In the example above, the condition i < 5 is true, so the indented code runs.
# An if statement is used to check if i is 3. If it is, the continue statement is executed
# and the rest of the code in the loop is skipped. If it is not, the rest of the code in the loop runs.
