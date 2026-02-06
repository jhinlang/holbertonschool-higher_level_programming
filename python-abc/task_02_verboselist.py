#!/usr/bin/env python3
"""
Module defining a VerboseList class that extends Python's built-in list
and prints notifications when items are added or removed.
"""


class VerboseList(list):
    """
    A custom list that prints messages when it is modified.
    """

    def append(self, item):
        """
        Append an item to the list and print a notification.

        Args:
            item: The item to be added to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with multiple items and print a notification.

        Args:
            iterable: An iterable of items to add to the list.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Remove an item from the list and print a notification.

        Args:
            item: The item to be removed from the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pop an item from the list at the given index and print a notification.

        Args:
            index (int, optional): The index of the item to pop.
                                   Defaults to -1 (last item).

        Returns:
            The item that was removed.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
