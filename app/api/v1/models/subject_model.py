import json

from app.api.v1.models.database import Database

Database().create_table()


class SubjectsModel(Database):
    """Initiallization."""

    def __init__(
            self,
            admission_no=None,
            maths=None,
            english=None,
            kiswahili=None,
            chemistry=None,
            biology=None,
            physics=None,
            history=None,
            geography=None,
            cre=None,
            agriculture=None,
            business=None):
        super().__init__()
        self.admission_no = admission_no
        self.maths = maths
        self.english = english
        self.kiswahili = kiswahili
        self.chemistry = chemistry
        self.biology = biology
        self.physics = physics
        self.history = history
        self.geography = geography
        self.cre = cre
        self.agriculture = agriculture
        self.business = business

    def save(self, admission_no, maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture,
             business):
        """Create a new orders."""
        self.curr.execute(
            ''' INSERT INTO subjects(admission_no, maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture, business)\
            VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')\
             RETURNING admission_no, maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture, business''' \
                .format(admission_no, maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture,
                        business))
        subjects = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return subjects

    def get_subjects(self):
        """Fetch all registered subjects."""
        self.curr.execute(''' SELECT * FROM subjects''')
        subjects = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return json.dumps(subjects, default=str)

    def get_admission_no(self, admission_no):
        """Get an exam with specific admission no."""
        self.curr.execute(""" SELECT * FROM subjects WHERE admission_no=%s""", (admission_no,))
        subject = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(subject, default=str)
