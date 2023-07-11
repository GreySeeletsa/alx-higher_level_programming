#!/usr/bin/python3
"""Define file-writing function"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file

    Args:
        filename: Name of the file to write
        text: Text to be written to file
    Returns: Number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
