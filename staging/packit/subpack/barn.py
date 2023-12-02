"""
Barn Modules of Subpack Example Subpackage

The barn contains a collection of barnyarn related
OOP objects we can use for our farm.
"""

class Barn:
    """ Class barn holds animals """
    def __init__(self, capacity, animals = None):
        self.capacity = capacity
        self.stock = animals if not None else []

    def fromlist(self, animals):
        """ Create a Barn from a list of animals """
        self.capacity = len(animals)
        self.stock = animals

    def add(self, animal):
        """ Add a single animal to your barn """
        if len(self.stock) == self.capacity:
            raise ValueError("cannot add animal, barn at capacity")

        self.stock.append(animal)

    def __repr__(self):
        return f"Barn({len(self.stock)}, {self.capacity})"


class Feed:
    """ Class feed provides nutrients """
    def __init__(self, nutrients, name, stock=0):
        self.name = name
        self.nutrients = nutrients
        self.stock = stock

    def feed(self, amount):
        """ Feed your livestock some amount """
        if amount > self.stock:
            err = f"requested amount ({amount}) is greater \
                than available stock ({self.stock})."
            raise ValueError(err)

        print(f"Feeding livestock {amount} of {self.name}.")
        self.stock -= amount
        print(f"Remaining stock: {self.stock}.")

    def increase_stock(self, amount):
        """ Add to your stock """
        self.stock += amount
