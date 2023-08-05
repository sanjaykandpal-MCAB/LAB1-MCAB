# Enter your domain name as characters and count any number of characters and print the count (for example – (‘p’,’r’,’o’,’g’,’r’,’a’,’m’) count of ‘r’ = 2)

def count_characters_in_blog_name():
    # Get the blog application name as characters
    blog_name_chars = input("Enter characters for the blog application name: ")

    # Create an empty dictionary to store character counts
    char_count_dict = {}

    # Count the occurrences of each character
    for char in blog_name_chars:
        char_count_dict[char] = char_count_dict.get(char, 0) + 1

    # Print the count of each character
    for char, count in char_count_dict.items():
        print(f"Count of '{char}' = {count}")


# calling function
count_characters_in_blog_name()
