"""General ideas for abstract base classes in Python."""

import abc

class HouseCat(abc.ABC):    # or: class Dog(metaclass=abc.ABCMeta): ...ABC is subclassed from this
    @abc.abstractmethod     # decorator marks methods as abstract; all derived classes must have
    def purr(self):         # the same method
        pass

class Calico(HouseCat):
    def purr(self):         # class will not instantiate if Hound doesn't have a bark() method
        print("Purrr.")

c = Calico()
c.purr()
print(isinstance(c, HouseCat))   # will run successfully to here!

# --------------------

class BigCat(abc.ABC):
    @abc.abstractmethod
    def purr(self):
        pass

class Tiger(BigCat):
    def purr(self):
        print("Purrr.")

t = Tiger()
t.purr()                        # this is the same as last time, but...

print(isinstance(c, BigCat))    # these will both eval to false, even though the base classes for
print(isinstance(t, HouseCat))  # the two have the same methods

# --------------------

# register a class as a virtual subclass of an ABC
@BigCat.register
class Lion:
    pass

l = Lion()                          # doesn't subclass ABC, but is treated as one

print(isinstance(l, BigCat))        # will eval as true
print(issubclass(Lion, BigCat))     # will eval as true
