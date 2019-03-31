import json

from app.api.v1.models.database import Database

Database().create_table()


class LibraryModel(Database):
    """Initiallization."""

    def __init__(
            self,
            author=None,
            title=None,
            subject=None,
            book_identity=None):
        super().__init__()
        self.author = author
        self.title = title
        self.subject = subject
        self.book_identity = book_identity

    def save(self, author, title, subject, book_identity):
        """Add a new book."""

        print(author, title, subject, book_identity)
        self.curr.execute(
            ''' INSERT INTO library(author, title, subject, book_identity)\
            VALUES('{}','{}','{}','{}')\
             RETURNING author, title, subject, book_identity''' \
                .format(author, title, subject, book_identity))
        books = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return books

    def get_all_books(self):
        """Fetch all books."""

        self.curr.execute(''' SELECT * FROM library''')
        books = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return json.dumps(books, default=str)

    def get_one_book(self, book_id):
        """Fetch a single book."""

        self.curr.execute(""" SELECT * FROM library WHERE book_id={}""".format(book_id))
        book = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(book, default=str)

    def get_book_identity(self, book_identity):
        """Fetch a single book."""

        self.curr.execute(""" SELECT * FROM library WHERE book_identity='{}'""".format(book_identity))
        book = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(book, default=str)
