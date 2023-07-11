#!/usr/bin/python3
"""Define Python class to JSON function"""


def class_to_json(obj):
    """returns dict description with simple data
    structure for JSON serialization of obj"""
    return obj.__dict__
