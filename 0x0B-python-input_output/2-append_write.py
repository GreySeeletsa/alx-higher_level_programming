#!/usr/bin/python3
"""Define file-appending function"""


def append_write(filename="", text=""):
    """Appends string to the end of a UTF8 text file

    Args:
        filename: Name of the file to append to
        text: The string to append to the file
    Returns: The number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
