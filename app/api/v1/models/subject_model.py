import json

from app.api.v1.models.database import Database

Database().create_table()


class SubjectsModel(Database):
    """Initiallization."""

    def __init__(
            self,
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

    def save(self, maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture,
             business):
        """Create a new orders."""

        print(maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture, business)
        self.curr.execute(
            ''' INSERT INTO subjects(maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture, business)\
            VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')\
             RETURNING maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture, business''' \
                .format(maths, english, kiswahili, chemistry, biology, physics, history, geography, cre, agriculture,
                        business))
        subjects = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return subjects

    def get_all_subjects(self):
        """Fetch all registered subjects."""

        self.curr.execute(''' SELECT * FROM subjects''')
        subjects = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return json.dumps(subjects, default=str)
