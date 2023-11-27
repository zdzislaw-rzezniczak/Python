class Post:
    def __init__(self, post_id, title, subtitle, body):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.body = body

    def __str__(self):
        return self.title + " " + self.subtitle + " " + self.body
