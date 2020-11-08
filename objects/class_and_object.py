# A class is a blueprint for the object
class Parrot:
    # class attribute
    species = "bird"

    # constructor
    def __init__(self, name, age):
        # instance attribute
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


# An object (instance) is an instantiation of a class
blueParrot = Parrot("Blue", 10)
greenParrot = Parrot("Green", 5)

# access the class attributes
print("Blue parrot is a {}".format(blueParrot.__class__.species))
print("Green parrot is a {}".format(greenParrot.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blueParrot.name, blueParrot.age))
print("{} is {} years old".format(greenParrot.name, greenParrot.age))

# call instance methods
print(blueParrot.sing("'Happy'"))
print(blueParrot.dance())
