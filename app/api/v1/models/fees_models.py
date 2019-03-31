import json

from app.api.v1.models.database import Database

Database().create_table()


class FeesModels(Database):
    """Initiallization."""

    def __init__(
            self,
            fees=None,
            fee_paid=None,
            fee_balance=None):
        super().__init__()
        self.fees = fees
        self.fee_paid = fee_paid
        self.fee_balance = fee_balance

    def save(self, fees, fee_paid, fee_balance):
        """Create a new fee entry."""

        print(fees, fee_paid, fee_balance)
        self.curr.execute(
            ''' INSERT INTO fees(fees, fee_paid, fee_balance)\
            VALUES({},{},{})\
             RETURNING fees, fee_paid, fee_balance''' \
                .format(fees, fee_paid, fee_balance))
        fees = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return fees

    def get_all_fees(self):
        """Fetch all comments"""

        self.curr.execute(''' SELECT * FROM fees''')
        fees = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return json.dumps(fees, default=str)

    def get_one_fee(self, fee_id):
        """Fetch a single comment"""

        self.curr.execute(""" SELECT * FROM fees WHERE fee_id={}""".format(fee_id))
        fee = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(fee, default=str)
