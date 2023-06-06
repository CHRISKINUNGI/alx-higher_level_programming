def print_alphabet_reverse():
    for i in range(ord('Z'), ord('A') - 1, -1):
        print("{}{}".format(chr(i + 32) if i % 2 == 1 else chr(i), ""), end="")

print_alphabet_reverse()

