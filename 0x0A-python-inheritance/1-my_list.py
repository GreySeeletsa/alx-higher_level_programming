#!/usr/bin/python3
"""Defines inherited list class"""


class MyList(list):
    """Sorted printing for built-in list class."""

    def print_sorted(self):
        """Print list sorted in ascending order."""
        print(sorted(self))
