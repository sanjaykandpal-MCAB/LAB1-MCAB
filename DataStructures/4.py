# Write a python program to count the number of alphabets, numeric and other special symbols in the paragraph.

def count_symbols(paragraph):
    # Initialize counters for alphabets, numeric characters, and special symbols
    num_alphabets = 0
    num_numerics = 0
    num_specials = 0

    for char in paragraph:
        if char.isalpha():
            num_alphabets += 1
        elif char.isdigit():
            num_numerics += 1
        else:
            num_specials += 1

    return num_alphabets, num_numerics, num_specials


def takingInput():
    paragraph = input("Enter the paragraph: ")
    alphabets, numerics, specials = count_symbols(paragraph)

    print("Number of Alphabets:", alphabets)
    print("Number of Numeric characters:", numerics)
    print("Number of Special symbols:", specials)


takingInput()