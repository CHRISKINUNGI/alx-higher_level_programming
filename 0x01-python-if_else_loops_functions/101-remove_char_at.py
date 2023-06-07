def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str  # Return the original string if n is out of bounds

    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]

    return new_str

