# Create a Tuple and Execute the packing and unpacking operations of tuples using the attributes of your domain.
def tuple_packing_unpacking():
    
    # Create a tuple representing a blog post
    blog_post = ("Introduction to Python", "John Doe", "Programming", "Python, Tutorial", "This is a beginner's guide to Python.")

    # Unpacking the tuple into individual variables
    title, author, category, tags, content = blog_post

    # Packing individual variables into a tuple
    packed_post = title, author, category, tags, content

    # Display the unpacked values and the packed tuple
    print("Unpacked values:")
    print("Title:", title)
    print("Author:", author)
    print("Category:", category)
    print("Tags:", tags)
    print("Content:", content)
    print("Packed tuple:", packed_post)


# Calling function
tuple_packing_unpacking()
