# A dictionary is an unordered collection of key-value pairs
# A dictionary is mutable, which means that its values can be changed
# A dictionary can be created by placing key-value pairs inside curly braces
#  - It can be created by using the dict() constructor
#  - It can contain values of different types

# Creating a dictionary
user_details = {}  # an empty dictionary
user_profile = {
    "name": "John",
    "age": 30,
    "is_admin": True,
}  # a dictionary with string keys

color = {
    1: "red",
    2: "green",
    3: "blue",
}  # a dictionary with integer keys

# Accessing elements in a dictionary
# A dictionary element can be accessed by key
print(user_profile["name"])  # John
print(user_profile["age"])  # 30
print(user_profile["is_admin"])  # True

# Modifying elements in a dictionary
# A dictionary is mutable, which means that its values can be changed
user_profile["name"] = "Jane"
print(user_profile["name"])  # Jane
print(user_profile)  # {'name': 'Jane', 'age': 30, 'is_admin': True}

# Adding elements to a dictionary
# A dictionary element can be added by using a new key
user_profile["email"] = "janedoe@test.com"
