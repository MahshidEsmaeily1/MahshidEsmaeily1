# This project implements a simple  Library Management System
# where users can:
# 1.Add books to a library.
# 2.View all books stored in the library.
# 3.Search for books by title or author.
# 4. Delete books by their unique ID.
#
# The code is written in Python and uses a
# SQLite database  to store book information
#



import sqlite3
from tabulate import tabulate
class Library:
  def __init__(self, db_name="library.db"):
    self.conn = sqlite3.connect(db_name)
    self.cursor = self.conn.cursor()
    self.create_table()


  def create_table(self):
    query = """ 
    CREATE TABLE IF NOT EXISTS books  (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         title TEXT NOT NULL, 
         author TEXT NOT NULL,
         year INTEGER NOT NULL 
    );
    """
    self.cursor.execute(query)
    self.conn.commit()


  def add_book(self, title, author, year):
    query = "INSERT INTO books (title, author, year) VALUES (?, ?, ?)"
    self.cursor.execute(query, (title, author, year))
    self.conn.commit()
    print("Book added successfully!")


  def view_books(self):
    query = "SELECT * FROM books"
    self.cursor.execute(query)
    books = self.cursor.fetchall()
    if books:
        print(tabulate(books, headers=["ID", "Title", "Author", "Year"], tablefmt="grid"))
    else:
        print("No books found.")

  def search_books(self, keyword):
    query = "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?"

    self.cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
    books = self.cursor.fetchall()
    if books:
        print(tabulate(books, headers=["ID", "Title", "Author", "Year"], tablefmt="grid"))
    else:
        print("No matching books found.")

  def delete_book(self, book_id):
    query = "DELETE FROM books WHERE id = ?"
    self.cursor.execute(query, (book_id,))
    self.conn.commit()
    print("Book deleted successfully!")

  def close_connection(self):
    self.conn.close()

def main():
  library = Library()
  while True:
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. View all books")
    print("3. Search for a book")
    print("4. Delete a book")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = int(input("Enter publication year: "))
        library.add_book(title, author, year)
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        keyword = input("Enter keyword to search: ")
        library.search_books(keyword)
    elif choice == "4":
        book_id = int(input("Enter book ID to delete: "))
        library.delete_book(book_id)
    elif choice == "5":
        library.close_connection()
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
if __name__ == "__main__":
 main()