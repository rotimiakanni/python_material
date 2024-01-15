# A tuple is a collection of values separated by commas.
# A tuple is immutable, which means that its values cannot be changed.
# - A tuple can be created by placing values inside parentheses.
# - A tuple can be created by placing values separated by commas.
# - A tuple can be created by using the tuple() constructor.
# - A tuple can contain values of different types.
# - A tuple can contain duplicate values.
# - A tuple can contain another tuple.

names = ("Bella", "Charlie", "Luna", "Lucy", "Max", "Bailey")  # a tuple of strings
numbers = (1, 2, 3, 4, 5)  # a tuple of integers
mixed = ("Bella", 1, "Charlie", 2, "Luna", 3)  # a list of strings and integers
nested = (["Bella", "Charlie"], ["Luna", "Lucy"], ["Max", "Bailey"])  # a tuple of lists
empty = ()  # an empty list

print(names)  # ('Bella', 'Charlie', 'Luna', 'Lucy', 'Max', 'Bailey')
print(numbers)  # (1, 2, 3, 4, 5)
print(mixed)  # ('Bella', 1, 'Charlie', 2, 'Luna', 3)
print(nested)  # (['Bella', 'Charlie'], ['Luna', 'Lucy'], ['Max', 'Bailey'])
print(empty)  # ()

# Accessing elements in a tuple
# A tuple can be accessed by index just like a list.
print(names[0])  # Bella
print(names[1])  # Charlie
print(names[-1])  # Bailey
print(names[-2])  # Max

# Modifying elements in a tuple
# A tuple is immutable, which means that its values cannot be changed.
# names[0] = "Buddy"  # TypeError: 'tuple' object does not support item assignment

# Slicing a tuple
# A tuple can be sliced just like a list.
print(names[0:2])  # ('Bella', 'Charlie')
print(names[:2])  # ('Bella', 'Charlie') - same as names[0:2]
print(names[2:])  # ('Luna', 'Lucy', 'Max', 'Bailey') - same as names[2:6]
print(
    names[:]
)  # ('Bella', 'Charlie', 'Luna', 'Lucy', 'Max', 'Bailey') - same as names[0:6]

# Iterating over a tuple
# A tuple can be iterated over just like a list.
for name in names:
    print(name)
