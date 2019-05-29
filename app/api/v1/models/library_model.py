import json

from app.api.v1.models.database import Database

Database().create_table()


class LibraryModel(Database):
    """Initiallization."""

    def __init__(
            self,
            admission_no=None,
            author=None,
            title=None,
            subject=None):
        super().__init__()
        self.admission_no = admission_no
        self.author = author
        self.title = title
        self.subject = subject

    def save(self, admission_no, author, title, subject):
        """Add a new book."""

        print(admission_no, author, title, subject)
        self.curr.execute(
            ''' INSERT INTO library(admission_no, author, title, subject)\
            VALUES('{}','{}','{}','{}')\
             RETURNING admission_no, author, title, subject''' \
                .format(admission_no, author, title, subject))
        book = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(book, default=str)

    def get_all_books(self):
        """Fetch all books."""

        self.curr.execute(''' SELECT * FROM library''')
        books = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return json.dumps(books, default=str)

    def get_admission_no(self, admission_no):
        """Get an exam with specific admission no."""
        self.curr.execute(""" SELECT * FROM library WHERE admission_no=%s""", (admission_no,))
        book = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(book, default=str)
