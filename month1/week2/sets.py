# A Set is an unordered collection of unique elements.
# - A set can be created by placing elements inside curly braces.
# - A set can be created by using the set() constructor.
# - A set can contain values of different types.
# - A set cannot contain duplicate values.

names = {"Bella", "Charlie", "Luna", "Lucy", "Max", "Bailey"}  # a set of strings
numbers = {1, 2, 3, 4, 5}  # a set of integers
mixed = {"Bella", 1, "Charlie", 2, "Luna", 3}  # a set of strings and integers
empty = set()  # an empty set

print(names)  # {'Lucy', 'Max', 'Luna', 'Charlie', 'Bailey', 'Bella'}

# Accessing elements in a set
# A set cannot be accessed by index because it is unordered.
# print(names[0])  # TypeError: 'set' object is not subscriptable

# Modifying elements in a set
# A set is mutable, which means that its values can be changed.
names.add("Buddy")
print(names)  # {'Lucy', 'Max', 'Luna', 'Charlie', 'Bailey', 'Bella', 'Buddy'}

names.remove("Buddy")
print(names)  # {'Lucy', 'Max', 'Luna', 'Charlie', 'Bailey', 'Bella'}

# Slicing a set
# A set cannot be sliced because it is unordered.
# print(names[0:2])  # TypeError: 'set' object is not subscriptable

# Iterating over a set
# A set can be iterated over just like a list.
for name in names:
    print(name)


# Set methods
# A set has several methods that can be used to modify and manipulate the set.
# - add(): Adds an element to the set.
# - remove(): Removes an element from the set.

# add()
names = {"Bella", "Charlie", "Luna", "Lucy", "Max", "Bailey"}
names.add("Buddy")
print(names)  # {'Lucy', 'Max', 'Luna', 'Charlie', 'Bailey', 'Bella', 'Buddy'}

# remove()
names = {"Bella", "Charlie", "Luna", "Lucy", "Max", "Bailey"}
names.remove("Bella")
print(names)  # {'Lucy', 'Max', 'Luna', 'Charlie', 'Bailey'}


# Set operations
# A set can be used to perform set operations such as union, intersection, and difference
# - Union: A union of two sets contains all the unique elements from both sets.
# - Intersection: An intersection of two sets contains all the elements that are common to both sets.
# - Difference: A difference of two sets contains all the elements that are in one set but not the other.


# Union
# A union of two sets contains all the unique elements from both sets.
# A union of two sets can be performed using the union() method or the | operator.
# The union() method returns a new set containing all the unique elements from both sets.
# The | operator returns a new set containing all the unique elements from both sets.
names = {"Bella", "Charlie", "Luna", "Lucy", "Max", "Bailey"}
numbers = {1, 2, 3, 4, 5}

print(
    names.union(numbers)
)  # {1, 2, 3, 4, 5, 'Lucy', 'Max', 'Luna', 'Charlie', 'Bailey', 'Bella'}

print(
    names | numbers
)  # {1, 2, 3, 4, 5, 'Lucy', 'Max', 'Luna', 'Charlie', 'Bailey', 'Bella'}

# Intersection
# An intersection of two sets contains all the elements that are common to both sets.
# An intersection of two sets can be performed using the intersection() method or the & operator.
# The intersection() method returns a new set containing all the elements that are common to both sets.
# The & operator returns a new set containing all the elements that are common to both sets.
names = {"Bella", "Charlie", "Luna", "Lucy", "Max", "Bailey"}
numbers = {1, 2, 3, 4, 5}
print(names.intersection(numbers))  # set()
print(names & numbers)  # set()

names = {"Bella", "Charlie", "Luna", "Lucy", "Max", "Bailey"}
numbers = {1, 2, 3, 4, 5, "Bella"}
print(names.intersection(numbers))  # {'Bella'}

# Difference
# A difference of two sets contains all the elements that are in one set but not the other.
# A difference of two sets can be performed using the difference() method or the - operator.
# The difference() method returns a new set containing all the elements that are in one set but not the other.
# The - operator returns a new set containing all the elements that are in one set but not the other.
names = {"Bella", "Charlie", "Luna", "Lucy", "Max", "Bailey"}
names2 = {"Bella", "Ava", "Aaron"}
print(names.difference(numbers))  # {'Lucy', 'Max', 'Luna', 'Charlie', 'Bailey'}
