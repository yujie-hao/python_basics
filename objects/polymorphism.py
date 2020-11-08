class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")

# In the above program, we defined two classes Parrot and Penguin.
# Each of them have a common fly() method. However, their functions are different.


# common interface
def flying_test(bird):
    bird.fly()


# instantiate objects
blueParrot = Parrot()
peggy = Penguin()

# passing the object
flying_test(blueParrot)
flying_test(peggy)
