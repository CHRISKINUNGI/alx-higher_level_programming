#!/usr/bin/python3
""" module containing function  """


def text_indentation(text):
    """
        text_indentation(text): function to prints a
        text with 2 new lines after each of these characters: ., ? and :

        args:
            text (string): string to
        raise:
            TypeError(text must be a string)

    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i])
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1
