# A program to demonstrate the use of class method in Python 

class Book:
    total_books = 0  # Class variable to keep track of total books
    
    def __init__ (self, title ):
        self.title = title
        Book.total_books += 1


    @classmethod
    def display_total_books(cls):
        print(f"Total books: {cls.total_books}")
    

book1 =Book("Python Programming")
book2 =Book("Data Science with Python")
book3 =Book("Machine Learning Basics")
Book.display_total_books()
