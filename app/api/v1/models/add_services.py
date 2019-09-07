import json
from werkzeug.security import generate_password_hash
from app.api.v1.models.database import Database
from datetime import datetime
import psycopg2


class AddServicesModel(Database):
    """A registered user can add a service."""

    def __init__(self, portfolio=None, occupation=None, phone=None, location=None, img=None, cost=None):
        super().__init__()
        self.portfolio = portfolio
        self.occupation = occupation
        self.phone = phone
        self.location = location
        self.img = img
        self.cost = cost

    def save(self):
        """Save information of the service."""
        self.curr.execute(
            ''' INSERT INTO add_services(portfolio, occupation, phone, location, img, cost)\
                VALUES('{}','{}','{}','{}','{}','{}') RETURNING portfolio, occupation, phone, location, img, cost'''
            .format(self.portfolio, self.occupation, self.phone, self.location, self.img, self.cost))
        service = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return service

    def get_services(self):
        """Fetch all services."""
        query = "SELECT * from add_services"
        services = Database().fetch(query)
        return json.dumps(services, default=str)

    def get_service(self, occupation):
        """Get a service with specific occupation."""
        self.curr.execute(
            ''' SELECT * FROM add_services WHERE occupation=%s''', (occupation,))
        service = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return json.dumps(service, default=str)
