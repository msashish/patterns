from abc import ABC


class Building(ABC):

    def __init__(self):
        print("Building init called")
        self.build_floor()
        self.build_size()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

    def __repr__(self):
        return "Floor: {0.floor} | Size: {0.size}".format(self)


#  If no __init__() method is implemented in the inherited class, then the parent __init__()
#  will be called automatically when an object of the inherited class is created.

class House(Building):

    def build_floor(self):
        self.floor = 1

    def build_size(self):
        self.size = "BIG"


class Flat(Building):

    def build_floor(self):
        self.floor = 10

    def build_size(self):
        self.size = "SMALL"


h = House()
print(h)

f = Flat()
print(f)
