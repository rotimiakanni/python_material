# Multiple Inheritance in Python
# This is where a class can be derived from more than one base class in Python.

# Example of Multiple Inheritance in Python
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def printName(self):
        print("Name  = " + self.name)

    def printRole(self):
        print("Role  = " + self.role)


class UserSettings:
    def __init__(self, bgColor, fontSize):
        self.bgColor = bgColor
        self.fontSize = fontSize

    def setBgColor(self, newBgColor):
        self.bgColor = newBgColor

    def setFontSize(self, newFontSize):
        self.fontSize = newFontSize


class AdminUser(User, UserSettings):
    def __init__(self, name, role, bgColor, fontSize):
        User.__init__(self, name, role)
        UserSettings.__init__(self, bgColor, fontSize)


# Now we can create an object of the AdminUser class and access the methods of both the base classes.
johnson = AdminUser("Johnson", "Admin", "Blue", 12)
johnson.printName()
johnson.printRole()
johnson.setBgColor("Red")
johnson.setFontSize(14)

print(johnson.bgColor)
print(johnson.fontSize)


# We can also check if the object is an instance of a particular class or not.
print(isinstance(johnson, User))
print(isinstance(johnson, UserSettings))
