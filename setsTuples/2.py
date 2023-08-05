# Update the Set with minimum 5 string attributes of your domain and arrange the Set in descending order.
def update_and_sort_set():
    # Update the set with five string attributes from the blog application
    blog_attributes = {"title", "author", "category", "tags", "content"}
    
    # updating set
    update_attributes = {"Date","Comments","Likes and shares","Image","URl"}

    blog_attributes.update(update_attributes)
    # Sort the set in descending order
    sorted_set = sorted(blog_attributes, reverse=True)

    # Display the sorted set
    print("Set arranged in descending order:")
    print(sorted_set)


# Calling function
update_and_sort_set()
