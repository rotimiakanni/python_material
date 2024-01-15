# A list is an ordered collection of data that can be changed.
#   - A list is defined using square brackets.
#   - A list can contain zero or more elements.
#   - A list can contain elements of different types. including other lists.
#   - A list can contain duplicate elements.

names = ["Bella", "Charlie", "Luna", "Lucy", "Max", "Bailey"]  # a list of strings
numbers = [1, 2, 3, 4, 5]  # a list of integers
mixed = ["Bella", 1, "Charlie", 2, "Luna", 3]  # a list of strings and integers
nested = [["Bella", "Charlie"], ["Luna", "Lucy"], ["Max", "Bailey"]]  # a list of lists
empty = []  # an empty list

print(names)  # ['Bella', 'Charlie', 'Luna', 'Lucy', 'Max', 'Bailey']
print(numbers)  # [1, 2, 3, 4, 5]
print(mixed)  # ['Bella', 1, 'Charlie', 2, 'Luna', 3]
print(nested)  # [['Bella', 'Charlie'], ['Luna', 'Lucy'], ['Max', 'Bailey']]
print(empty)  # []

#  - A list can be accessed by index.
#  - The index of the first element is 0.
#  - The index of the last element is -1.
#  - The index of the second last element is -2, and so on.
#  - The index of an element can be used to access the element.
#  - The index of an element can be used to modify the element in the list.

# Accessing elements in a list
print(names[0])  # Bella
print(names[1])  # Charlie
print(names[-1])  # Bailey
print(names[-2])  # Max
print(names[30])  # IndexError: list index out of range

# Modifying elements in a list
names[0] = "Buddy"
print(names)  # ['Buddy', 'Charlie', 'Luna', 'Lucy', 'Max', 'Bailey']
nested[0][0] = "Buddy"
print(nested)  # [['Buddy', 'Charlie'], ['Luna', 'Lucy'], ['Max', 'Bailey']]

# Slicing a list
#  - A list can be sliced.
#  - A slice of a list can be accessed by using the start and end indices.
#  - The start index is inclusive.
#  - The end index is exclusive.
#  - The start and end indices are optional.
#  - If the start index is not specified, it defaults to 0.
#  - If the end index is not specified, it defaults to the length of the list.

print(names[0:2])  # ['Buddy', 'Charlie']
print(names[:2])  # ['Buddy', 'Charlie'] - same as names[0:2]
print(names[2:])  # ['Luna', 'Lucy', 'Max', 'Bailey'] - same as names[2:6]
print(
    names[:]
)  # ['Buddy', 'Charlie', 'Luna', 'Lucy', 'Max', 'Bailey'] - same as names[0:6]

# Adding elements to a list
#  - An element can be added to the end of a list using the append() method.
#  - An element can be added to a specific index in a list using the insert() method.

names.append("Milo")
print(names)  # ['Buddy', 'Charlie', 'Luna', 'Lucy', 'Max', 'Bailey', 'Milo']
names.insert(0, "Milo")
print(names)  # ['Milo', 'Buddy', 'Charlie', 'Luna', 'Lucy', 'Max', 'Bailey', 'Milo']

# Removing elements from a list
#  - An element can be removed from a list using the remove() method.
#  - An element can be removed from a list using the pop() method.
#  - The pop() method removes the last element if the index is not specified.
#  - The pop() method returns the removed element.

names.remove("Milo")  # removes the first occurrence of the element
print(names)  # ['Buddy', 'Charlie', 'Luna', 'Lucy', 'Max', 'Bailey', 'Milo']

removed = names.pop()  # removes the last element
print(removed)  # Milo

removed = names.pop(0)  # removes the element at the specified index
print(removed)  # Buddy


# Looping through a list
#  - A list can be looped through using a for loop.
#  - The for loop iterates through each element in the list.
#  - The for loop iterates through each element in the list in order.

for name in names:
    print(name)
