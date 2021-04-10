"""
If there is a time consuming evaluation then its not done during object instantiation
    and evaluated only when its value is really needed
    and avoids repeated evaluations.
"""
import time


# The slow way. Assume getting all relatives is a very very slow process and part of instantiation
# Every time you create a new instance its going take a lot of time
# Every time you call get_all_relatives() it will take lot of time again
class SlowPerson:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.relatives = self.get_all_relatives()

    # time consuming process
    def get_all_relatives(self):
        time.sleep(5)
        return "All relatives"


# The fast way using lazily-evaluated property Pattern in python

# Method1
# Time consuming operation not part of instantiation AND does not get called repeatedly
class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self._relatives = None

    # time consuming process and should not be accessed via object
    def __get_all_relatives(self):
        time.sleep(5)
        return "All relatives"

    @property
    def relatives(self):
        if self._relatives is None:
            self._relatives = self.__get_all_relatives()
        return self._relatives


# Method2 : Pythonic way of doing
def lazy_property(fn):
    attr = '_lazy_' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr):
            setattr(self, attr, fn(self))
        return getattr(self, attr)
    return _lazy_property


class PyPerson:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self._relatives = None

    # time consuming process and should not be accessed via object
    def __get_all_relatives(self):
        time.sleep(5)
        return "All relatives"

    @property
    def relatives(self):
        if self._relatives is None:
            self._relatives = self.__get_all_relatives()
        return self._relatives


# Testing the lazily-evaluated property
input("Hit enter to instantiate SlowPerson object")
j = SlowPerson("Ashish", "Engg")
print(j)
input("Hit enter to compute SlowPerson's relatives ")
print(j.relatives)
input("Hit enter to compute SlowPerson's relatives again")
print(j.get_all_relatives())

input("Hit enter to instantiate fast Person object quickly .... using lazily-evaluated property Pattern in python")
p = PyPerson("Ashish", "Engg")
print(p)
input("Hit enter to compute ONCE relatives WHEN needed")
print(p.relatives)
input("Hit enter to compute relatives again ")
print(p.relatives)
input("Hit enter to compute relatives again ")
print(p.relatives)
input("Hit enter to compute relatives again")
print(p.relatives)
