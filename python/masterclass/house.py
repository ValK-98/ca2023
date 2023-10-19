
class House: 
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return float(self.__price)

    @price.setter
    def price(self, price):
        if price > 0:
            self.__price = price
        else:
            raise ValueError("Price must be positive")

my_house = House(650000)
my_house.price = 700000
print(my_house.price)
my_house.price = -500