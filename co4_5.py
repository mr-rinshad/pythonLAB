# Base class
class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher Name:", self.name)


# Derived class
class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Book Title:", self.title)
        print("Author:", self.author)


# Derived class
class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)
        self.price = price
        self.pages = pages

    def display(self):
        super().display()
        print("Price:", self.price)
        print("Number of Pages:", self.pages)


# -------- MAIN PROGRAM WITH USER INPUT --------

pub_name = input("Enter Publisher Name: ")
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
price = float(input("Enter Price: "))
pages = int(input("Enter Number of Pages: "))

# Creating Python book object
p = Python(pub_name, title, author, price, pages)

print("\n----- PYTHON BOOK DETAILS -----")
p.display()

