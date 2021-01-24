class Post:
    def __init__(self, title=None, content=None):
        self.title = title
        self.content = content

    def __repr__(self):
        return f"{self.title}\n\n{self.content}"

    def json(self):
        return {
            'title': self.title, 
            'content': self.content,
            }

