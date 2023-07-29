#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line
    containing a specific string in the file.

    Args:
        filename (str): The name of the file to process.
        search_string (str): The specific string to
        look for in each line.
        new_string (str): The line of text to insert
        after the lines containing the search string.

    Returns:
        None
    """
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as file:
        file.write("".join(lines))
