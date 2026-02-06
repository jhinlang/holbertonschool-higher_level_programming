#!/usr/bin/env python3
"""
Module demonstrating the use of mixins to compose behaviors
for a Dragon class.
"""


class SwimMixin:
    """
    Mixin providing swimming capability.
    """

    def swim(self):
        """
        Print a message indicating the creature swims.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin providing flying capability.
    """

    def fly(self):
        """
        Print a message indicating the creature flies.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that combines swimming and flying abilities
    using mixins.
    """

    def roar(self):
        """
        Print a message indicating the dragon roars.
        """
        print("The dragon roars!")
