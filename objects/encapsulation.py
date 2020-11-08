class Computer:
    def __init__(self):
        # __xxx: private member
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# change the price directly, won't work
c.__maxprice = 1000
c.sell()

# using the setter member function
c.setMaxPrice(1000)
c.sell()


# Property
class Smartphone:
    def __init__(self, value):
        self._price = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        assert isinstance(value, int)
        assert value >= 0 and value <= 1500


iPhone = Smartphone()
iPhone.price = 1000
print("iPhone.price: " + iPhone.price.__str__())
