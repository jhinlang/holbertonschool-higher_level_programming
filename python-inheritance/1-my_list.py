class MyList(list):
    """A class that inherits from list and has a method to print the list in sorted order."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
