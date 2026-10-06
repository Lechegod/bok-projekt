
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("1984", "George Orwell", 328)

book1.show_info()
print()
book2.show_info()