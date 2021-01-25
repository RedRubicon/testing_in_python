blogs = dict() # blog_name: Blog object

def menu():
    # Show user the available logs
    # Let user make a choice
    # Act on the user choice
    # exit

    print_blogs()

def print_blogs():
    for key, blog in blogs.items():
        print(f"- {blog}")
