from datetime import datetime

class User:
    """ Defines a User object """
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.posts = []

    def create_post(self, content, date = None):
        post = Post(content, date, self)
        self.posts.append(post)
        return post

    def list_posts(self):
        for post in self.posts:
            print(post)

    def __str__(self):
        return f"{self.username} ({self.email})"

class Post:
    """ Defines a Post object """
    def __init__(self, content, date, author):
        self.content = content
        self.author = author
        self.date = date if date else datetime.today()

    def __str__(self):
        return f"Post by {self.author.username} ({self.date:%d/%M/%Y}): {self.content}"

if __name__ == "__main__":
    user1 = User("Alice", "alice@example.com")
    user2 = User("Bob", "bob@example.com")
    
    post1 = user1.create_post("Hello, world!")
    post2 = user2.create_post("Just another day in data science.")
    user2.create_post("Slinging code again!")

    print(user1)
    user1.list_posts()
    user2.list_posts()
    # Alice (alice@example.com)
    # Post by Alice (06/43/2023): Hello, world!
    # Post by Bob (06/43/2023): Just another day in data science.
    # Post by Bob (06/43/2023): Slinging code again!