from post import Post

class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f"{self.title}: {self.author} ({len(self.posts)} post{'' if len(self.posts) == 1 else 's'})"

    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self):
        posts_dict_list = []

        for post in self.posts:
            posts_dict_list.append(post.json())

        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
        }