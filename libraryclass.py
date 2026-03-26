class Library:
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    def check_out(self):
        if self.available:
            self.available = False
            print("Book issued")
        else:
            print("Book not available")

    def return_book(self):
        self.available = True
        print("Book returned")

    def display(self):
        print(self.book_name, "-", self.author, "| Available:", self.available)


# Example
book = Library("Python Basics", "ABC")
book.display()
book.check_out()
book.display()
book.return_book()