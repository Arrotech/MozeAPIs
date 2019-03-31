import json

from app.api.v1.models.database import Database

Database().create_table()


class EvaluationModels(Database):
    """Initiallization."""

    def __init__(
            self,
            name=None,
            subject=None,
            attendance=None,
            homework=None,
            rate=None,
            comment=None):
        super().__init__()
        self.name = name
        self.subject = subject
        self.attendance = attendance
        self.homework = homework
        self.rate = rate
        self.comment = comment

    def save(self, name, subject, attendance, homework, rate, comment):
        """Create a new comment."""

        print(name, subject, attendance, homework, rate, comment)
        self.curr.execute(
            ''' INSERT INTO evaluation(name, subject, attendance, homework, rate, comment)\
            VALUES('{}','{}','{}','{}','{}','{}')\
             RETURNING name, subject, attendance, homework, rate, comment''' \
                .format(name, subject, attendance, homework, rate, comment))
        comments = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return comments

    def get_all_comments(self):
        """Fetch all comments"""

        self.curr.execute(''' SELECT * FROM evaluation''')
        comments = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return json.dumps(comments, default=str)

    def get_one_comment(self, comment_id):
        """Fetch a single comment"""

        self.curr.execute(""" SELECT * FROM evaluation WHERE comment_id={}""".format(comment_id))
        comment = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(comment, default=str)

    def get_name(self, name):
        """Fetch a single order"""

        self.curr.execute(""" SELECT * FROM evaluation WHERE name='{}'""".format(name))
        name = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(name, default=str)
