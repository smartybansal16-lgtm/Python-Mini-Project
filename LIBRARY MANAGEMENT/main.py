class Book:
    def _init_(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def _str_(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | Status: {self.status}"

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        self.status = "available"

    def is_available(self):
        return self.status == "available"

    def to_dict(self):
        return self._dict_

    @staticmethod
    def from_dict(data):
        return Book(**data)
import json
import os
import logging

class LibraryInventory:
    def init(self, filepath='books.json'):
        format='%(asctime)s - %(levelname)s - %(message)s'
def menu():
    inventory = LibraryInventory()
    
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            inventory.add_book(Book(title, author, isbn))
            print("Book added.")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.issue():
                inventory.save_books()
                print("Book issued.")
            else:
                print("Book not available or not found.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if book:
                book.return_book()
                inventory.save_books()
                print("Book returned.")
            else:
                print("Book not found.")

        elif choice == "4":
            books = inventory.display_all()
            if books:
                for b in books:
                    print(b)
            else:
                print("No books available.")

        elif choice == "5":
            term = input("Search title: ")
            results = inventory.search_by_title(term)
            if results:
                for b in results:
                    print(b)
            else:
                print("No matching books found.")

        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


