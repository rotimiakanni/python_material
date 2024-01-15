# Defining classes and objects in Python. Here'e what you need to know.
# - Classes are a way to group functions and data together. They are a way to create your own data types.
# - Objects are instances of classes. They are created by calling the class as if it were a function.
# - Classes are defined with the class keyword. They are followed by a colon and then the class body.
# - The class body is indented.
# - Classes have a special function called __init__. This function is called when you create an object.
# - The __init__ function is called with the object as the first argument. It is called with the other arguments
#   that you pass to the class when you create the object.
# - The __init__ function is used to set up the object. It is used to set the values of the object's attributes.

# Let's create a class called Person. It will have a name and an age.
class Person:
    def __init__(
        self, name, age
    ):  # The __init__ function is a constructor. It is called when you create an object.
        self.name = name
        self.age = age

    # The following is called a method. It is a function that is defined inside a class.
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Let's create an object of type Person.
john = Person("John", 30)
peter = Person("Peter", 40)  # We can create as many objects as we want.

# Let's call the say_hello method on the john object.
john.say_hello()
peter.say_hello()


# Let's create a class called Dog. It will have a name and an age.
class User:
    def __init__(self, first_name, last_name, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_password(self):
        return self.password

    def validate_password(self, password):
        return self.password == password


# Let's create an object of type User.
john = User("John", "Doe", "johndoe", "password")
peter = User("Peter", "Smith", "petersmith", "password123")

# Let's call the get_full_name method on the john object.
print(john.get_full_name())
print(peter.get_full_name())

# Let's call the get_password method on the john object.
print(john.get_password())
print(peter.get_password())


#  Class with properties
class Student:
    # This is a class attribute. It is shared by all objects of this class.
    num_of_students = 0

    def __init__(self, first_name, last_name, age, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade = grade
        # Increment the number of students anytime a new student is created.
        Student.num_of_students += 1

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_grade(self):
        return self.grade

    def get_student_details(self):
        return f"{self.get_full_name()} is {self.age} years old and is in grade {self.get_grade()}"


# Let's create an object of type Student.
abel = Student("Abel", "Tuter", 20, 12)
ola = Student("Ola", "Makanaki", 19, 23)

# We can access the class attribute
print(Student.num_of_students)
print(abel.num_of_students)
