# Inheritance allows you to create new classes that are based on existing classes,
# inheriting their properties and methods. This makes it easy to reuse existing code
# and create complex hierarchies of classes.


class Human:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_age(self):
        return self.age

    def get_details(self):
        return f"{self.get_full_name()} is {self.age} years old."


# Let's create a class called Student that inherits from the Human class.
class Student(Human):
    def __init__(self, first_name, last_name, age, grade, school):
        # Call the __init__ method of the parent class.
        super().__init__(first_name, last_name, age)

        # Here we add extra properties that are specific to the Student class.
        self.grade = grade
        self.school = school

    def get_grade(self):
        return self.grade

    # Here we override the get_details method of the parent class
    # to include the grade and school properties.
    def get_details(self):
        return f"{self.get_full_name()} is {self.age} years old and is in grade {self.get_grade()}"


# Now student has access to all the methods of the Human class.
alex = Student("Alex", "Smith", 15, 9, "High School")
print(alex.get_full_name())
print(alex.get_age())

print(alex.get_details())
print(alex.get_grade())


# Let's create a class called Teacher that inherits from the Human class.
class Teacher(Human):
    def __init__(self, first_name, last_name, age, subject, school):
        # Call the __init__ method of the parent class.
        super().__init__(first_name, last_name, age)

        # Here we add extra properties that are specific to the Teacher class.
        self.subject = subject
        self.school = school

    def get_subject(self):
        return self.subject

    # Here we override the get_details method of the parent class
    # to include the subject and school properties.
    def get_details(self):
        return f"{self.get_full_name()} is {self.age} years old and teaches {self.get_subject()} at {self.school}"


mike = Teacher("Micheal", "Jack", 35, "Math", "High School")
print(mike.get_full_name())
print(mike.get_age())

print(mike.get_details())
print(mike.get_subject())
