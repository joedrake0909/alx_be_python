class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
    
    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages!r})"
    

if __name__ == "__main__":
    b = Book("1984", "George Orwell", 328)
    print("print(book) ->", str(b))   # user-friendly representation
    print("repr(book) ->", repr(b))  # developer-friendly representation
        
        