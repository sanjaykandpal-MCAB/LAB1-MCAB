# Write a python program to display all the datatypes of selected specific elements in the paragraph. (For example:– name - string, reg.no - int, marks - float, etc.)
def get_datatype(element):
    try:
        int(element)
        return "int"
    except ValueError:
        pass
    
    try:
        float(element)
        return "float"
    except ValueError:
        pass
    
    return "string"


def takeInput():
    paragraph = input("Enter the paragraph: ")
    specific_words = input("Enter specific words (separated by commas): ").split(',')

    print("Data Types of Selected Specific Elements:")
    for word in specific_words:
        element = None
        for w in paragraph.split():
            # Convert the word from the paragraph and the specific word
            # to lowercase to handle case-insensitivity in matching.
            if w.lower().strip('.,') == word.lower().strip('.,'):
                element = w
                break

        if element is not None:
            datatype = get_datatype(element)
            print(f"{element} - {datatype}")
        else:
            print(f"{word} - Not found in the paragraph.")

takeInput()