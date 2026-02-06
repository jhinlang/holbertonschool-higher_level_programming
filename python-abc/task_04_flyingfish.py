#!/usr/bin/env python3
"""
Module demonstrating multiple inheritance and method resolution order (MRO)
with Fish, Bird, and FlyingFish classes.
"""


class Fish:
    """
    Class representing a fish.
    """

    def swim(self):
        """
        Print how the fish swims.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print the habitat of the fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Class representing a bird.
    """

    def fly(self):
        """
        Print how the bird flies.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print the habitat of the bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a flying fish, inheriting from Fish and Bird.
    """

    def swim(self):
        """
        Override swim behavior for the flying fish.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Override fly behavior for the flying fish.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Override habitat to describe both environments.
        """
        print("The flying fish lives both in water and the sky!")
