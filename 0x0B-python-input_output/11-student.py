#!/usr/bin/python3
"""Defines the class Student."""


class Student:
    """Rep a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student

        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is list of strings represents only those attributes
        included

        Args:attrs:The attributes to represent
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student

            json (dict): The value pairs to replace attributes with.
        """
        for x, y in json.items():
            setattr(self, x, y)
