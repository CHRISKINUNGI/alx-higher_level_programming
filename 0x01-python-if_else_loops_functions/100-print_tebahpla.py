def print_alphabet_reverse():
    """ the ord function converts the ASCII value
    back to its corresponding character. """
    
    uppercase = chr(90)  # ASCII value of 'Z'
    lowercase = chr(122)  # ASCII value of 'z'

    for i in range(26):
        char = uppercase if i % 2 == 0 else lowercase
        print("{}".format(char), end="")
        uppercase = chr(ord(uppercase) - 1)
        lowercase = chr(ord(lowercase) - 1)

    print()

print_alphabet_reverse()
