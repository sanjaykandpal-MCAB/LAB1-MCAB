    # Enter your domain name, execute all the slicing possibilities and also negative indexing.

def slicing_and_negative_indexing():
    
    blog_app_name = "MyBlogApp"

    # Slicing examples
    slice_1 = blog_app_name[0:2] #[0,1] index will print
    slice_2 = blog_app_name[:2]  #[0,1] index will print
    slice_3 = blog_app_name[2:]  #[2,7] index will print
    slice_4 = blog_app_name[:]   #whole string will be printed

    # Negative indexing examples
    neg_index_1 = blog_app_name[-1]  #character from the end
    neg_index_2 = blog_app_name[-3:] #at the end three character will print
    neg_index_3 = blog_app_name[:-3] 

    # Display the results
    print("Slicing:")
    print("1. blog_app_name[0:2] =", slice_1)
    print("2. blog_app_name[:2] =", slice_2)
    print("3. blog_app_name[2:] =", slice_3)
    print("4. blog_app_name[:] =", slice_4)

    print("\nNegative Indexing:")
    print("1. blog_app_name[-1] =", neg_index_1)
    print("2. blog_app_name[-3:] =", neg_index_2)
    print("3. blog_app_name[:-3] =", neg_index_3)


# CALLING FUNCTION
slicing_and_negative_indexing()
