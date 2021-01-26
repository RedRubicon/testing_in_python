MENU_PROMPT = 'Enter "c" to create blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit'

blogs = dict() # blog_name: Blog object

def menu():
    # Show user the available logs
    # Let user make a choice
    # Act on the user choice
    # exit

    print_blogs()
    selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():
        print(f"- {blog}")
