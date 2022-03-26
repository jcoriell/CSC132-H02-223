# Abstract Methods: Methods that are intended to be implemented by a subclass


# Two ways to implement:

# 1. raise a NotImplementedError

class Animal:

    def __init__(self):
        """Constructor for animal class"""

    def communicate(self):
        raise NotImplementedError("Abstract Method Communicate Not Implemented in Subclass")

class Bird(Animal):

    def __init__(self):
        "Whatever a bird has"
    
    def communicate(self):
        print("CHIIIIIIRRRP!")

b = Bird()
b.communicate()

# 2. Use the abc module
import abc

class Pokemon(metaclass=abc.ABCMeta):

    def __init__(self):
        """Gotta catchem all!"""

    @abc.abstractclassmethod
    def communicate(self):
        """How a pokemon communicates 🎉"""


class Bulbasaur(Pokemon):

    def __init__(self):
        """Bubasaur stuff"""

    def communicate(self):
        print("Bulba Bulbasaur")

bulb = Bulbasaur()
bulb.communicate()


# Abstract Class: A class designed to never be instantiated 
# (ex: can use as a template for other classes)

# Concrete class: a class that can be instantiated.

p = Pokemon()


