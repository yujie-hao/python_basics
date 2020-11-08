# A class is a blueprint for the object
class Parrot:
    # docstring: a brief description about the class.
    """This is a Parrot class"""
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


print("Parrot.__doc__: {}".format(Parrot.__doc__))
print("species: " + Parrot.species)
print(Parrot.sing)

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
print(blueParrot.dance)


# Constructors
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')


# Create a new ComplexNumber object
num1 = ComplexNumber(2, 3)

# Call get_data() method
num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
num2 = ComplexNumber(5)
num2.attr = 10

print(num2.real, num2.imag, num2.attr)
# print(num1.attr) # AttributeError: 'ComplexNumber' object has no attribute 'attr'

# delete attributes and objects
num1.get_data()
del num1.imag
# num1.get_data() # AttributeError: 'ComplexNumber' object has no attribute 'imag'

num2.get_data()
del ComplexNumber.get_data
# num2.get_data() # AttributeError: 'ComplexNumber' object has no attribute 'get_data'

c1 = ComplexNumber(1, 3)
del c1
# c1.get_data() # NameError: name 'c1' is not defined

