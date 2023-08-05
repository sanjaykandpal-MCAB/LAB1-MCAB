# Write a python program to count the frequency of any specific word (in your domain) in the paragraph.

def count_word_frequency_in_paragraph():
    
    def get_word_frequency(word_list):
        word_frequency = {}
        for word in word_list:
            word_frequency[word] = word_frequency.get(word, 0) + 1
        return word_frequency

    def count_specific_word(word, word_frequency):
        return word_frequency.get(word, 0)

    paragraph = input("Enter the paragraph: ")
    word_to_count = input("Enter the specific word to count: ")

    # Convert the paragraph to lowercase to make the search case-insensitive
    paragraph = paragraph.lower()

    # Split the paragraph into words
    words = paragraph.split()

    # Get the frequency of each word
    word_frequency = get_word_frequency(words)

    # Count the specific word
    count = count_specific_word(word_to_count.lower(), word_frequency)

    return count

# Call the function to count the frequency of a specific word
result = count_word_frequency_in_paragraph()
print("Frequency of the specific word:", result)
