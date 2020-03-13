from pathlib import Path
import sqlite3

class Backend:
    """
    Class defining the backend side of the app.
    """
    def __init__(self):
        self.dbPath = Path(__file__).parent.parent # book_store
        self.dbPath = self.dbPath.joinpath('resources', 'books.db')
        
        self.connection = sqlite3.connect(self.dbPath)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Book
            (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)"""
        )
        self.connection.commit()

    def __del__(self):
        self.connection.close()

    def insert(self, title, author, year, isbn):
        self.cursor.execute("""
            INSERT INTO Book VALUES (NULL, ?, ?, ?, ?)
            """, (title, author, year, isbn)
        )
        self.connection.commit()

    def view(self):
        self.cursor.execute("""
            SELECT * FROM Book"""
        )
        rows = self.cursor.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cursor.execute("""
            SELECT * FROM Book WHERE title=? OR author=? OR year=? OR isbn=?""", (title, author, year, isbn)
        )
        rows = self.cursor.fetchall()
        return rows

    def delete(self, id):
        self.cursor.execute("""
            DELETE FROM Book WHERE id=?""", (id,)
        )
        connection.commit()

    def update(self, id, title, author, year, isbn):
        self.cursor.execute("""
            UPDATE Book SET title=?, author=?, year=?, isbn=? WHERE id=?""", (title, author, year, isbn, id)
        )
        connection.commit()