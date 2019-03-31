import json

from app.api.v1.models.database import Database


class StudentIdModel(Database):
    """Initialization."""

    def __init__(self, surname=None, first_name=None, last_name=None, admission_no=None, subjects=None):
        super().__init__()
        self.surname = surname
        self.first_name = first_name
        self.last_name = last_name
        self.admission_no = admission_no
        self.subjects = subjects

    def save(self, surname, first_name, last_name, admission_no, subjects):
        """Save information of the new user"""

        self.curr.execute(
            ''' INSERT INTO studentId(surname, first_name, last_name, admission_no, subjects)\
             VALUES('{}','{}','{}','{}','{}') RETURNING surname, first_name, last_name, admission_no, subjects''' \
                .format(surname, first_name, last_name, admission_no, subjects))
        studentId = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return studentId

    def get_id(self):
        """Fetch all users"""

        self.curr.execute(''' SELECT * FROM studentId''')
        studentId = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return json.dumps(studentId, default=str)
