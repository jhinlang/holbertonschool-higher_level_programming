"""
Module demonstrating abstract base classes and polymorphism in Python.

This module shows how to use the ABC (Abstract Base Classes) module to define
abstract classes with abstract methods that must be implemented by subclasses.
It demonstrates the concept of polymorphism through Animal subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    An abstract base class representing an animal.

    This class defines the interface that all animal subclasses must follow
    by declaring abstract methods that must be implemented by concrete
    subclasses.
    """

    @abstractmethod
    def sound(self) -> str:
        """
        Return the sound that the animal makes.

        This is an abstract method that must be implemented by all
        concrete subclasses of Animal.

        Returns:
            str: A string representation of the sound the animal makes.

        Raises:
            TypeError: If called on an abstract class directly.
        """
        pass


class Dog(Animal):
    """
    A concrete implementation of Animal representing a dog.

    This class implements the abstract methods defined in the Animal
    base class.
    """

    def sound(self) -> str:
        """
        Return the sound that a dog makes.

        Returns:
            str: The string "Bark" representing a dog's sound.
        """
        return "Bark"


class Cat(Animal):
    """
    A concrete implementation of Animal representing a cat.

    This class implements the abstract methods defined in the Animal
    base class.
    """

    def sound(self) -> str:
        """
        Return the sound that a cat makes.

        Returns:
            str: The string "Meow" representing a cat's sound.
        """
        return "Meow"
