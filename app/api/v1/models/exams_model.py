"""Json package."""
import json

from app.api.v1.models.database import Database

Database().create_table()


class ExamsModel(Database):
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
        """Initialization."""
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

    def save(self, admission_no, maths, english, kiswahili, chemistry, biology, physics, history, geography, cre,
             agriculture, business):
        """Create a new orders."""
        print(admission_no, maths, english, kiswahili, chemistry, biology, physics, history, geography, cre,
              agriculture, business)
        self.curr.execute(
            ''' INSERT INTO exams(admission_no, maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture, business)\
            VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')\
             RETURNING admission_no, maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture, business''' \
                .format(admission_no, maths, english, kiswahili, chemistry, biology, physics, history, geography, cre,
                        agriculture, business))
        exam = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(exam, default=str)

    def get_all_exams(self):
        """Fetch all orders"""

        self.curr.execute(''' SELECT * FROM exams''')
        exams = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return json.dumps(exams, default=str)

    def get_exam_by_id(self, exam_id):
        """Fetch a single order"""

        self.curr.execute(""" SELECT * FROM exams WHERE exam_id={}""".format(exam_id))
        exam = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(exam, default=str)

    def get_admission_no(self, admission_no):
        """Get an exam with specific admission no."""

        self.curr.execute(""" SELECT * FROM exams WHERE admission_no=%s""", (admission_no,))
        user = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(user, default=str)

    def update_scores(self, exam_id, admission_no, maths, english, kiswahili, chemistry, biology, physics, history,
                      geography, cre, agriculture, business):
        """User can Change information of the office."""

        self.curr.execute("""UPDATE exams\
            SET admission_no='{}', maths='{}', english='{}', kiswahili='{}', chemistry='{}', biology='{}', physics='{}', history='{}', geography='{}', cre='{}', agriculture='{}', business='{}'\
            WHERE exam_id={} RETURNING admission_no, maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture, business""" \
                          .format(exam_id, admission_no, maths, english, kiswahili, chemistry, biology, physics,
                                  history, geography, cre, agriculture, business))
        exam = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(exam, default=str)

    def delete_exam(self, exam_id):
        ''' Delete exam.'''

        self.curr.execute(''' DELETE FROM exams WHERE exam_id=%s''', (exam_id,))
        self.conn.commit()
        self.curr.close()
