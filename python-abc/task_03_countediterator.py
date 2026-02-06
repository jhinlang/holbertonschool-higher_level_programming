#!/usr/bin/env python3
"""
Module defining a CountedIterator that keeps track of
how many items have been iterated over.
"""


class CountedIterator:
    """
    An iterator that counts how many items have been fetched.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator.

        Args:
            iterable: Any iterable object (list, tuple, etc.).
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
            CountedIterator: The iterator instance.
        """
        return self

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.

        Raises:
            StopIteration: When there are no more items.

        Returns:
            The next item from the iterable.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Get the number of items that have been iterated over.

        Returns:
            int: The number of items fetched.
        """
        return self.count
