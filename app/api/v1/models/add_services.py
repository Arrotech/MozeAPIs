import json
from werkzeug.security import generate_password_hash
from app.api.v1.models.database import Database
from datetime import datetime
import psycopg2


class AddServicesModel(Database):
    """A registered user can add a service."""

    def __init__(self, name=None, business_name=None, portfolio=None, occupation=None, social_link=None, description=None, phone=None, location=None, working_hours=None, cost=None):
        super().__init__()
        self.name = name
        self.business_name = business_name
        self.portfolio = portfolio
        self.occupation = occupation
        self.social_link = social_link
        self.description = description
        self.phone = phone
        self.location = location
        self.working_hours = working_hours
        self.cost = cost

    def save(self):
        """Save information of the service."""
        self.curr.execute(
            ''' INSERT INTO add_services(name, business_name, portfolio, occupation, social_link, description, phone, location, working_hours, cost)\
                VALUES('{}', '{}', '{}', '{}', '{}','{}','{}','{}','{}','{}') RETURNING name, business_name, portfolio, occupation, social_link, description, phone, location, working_hours, cost'''
            .format(self.name, self.business_name, self.portfolio, self.occupation, self.social_link, self.description, self.phone, self.location, self.working_hours, self.cost))
        service = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return service

    def get_services(self):
        """Fetch all services."""
        query = "SELECT * from add_services"
        services = Database().fetch(query)
        return services

    def get_service(self, occupation):
        """Get a service with specific occupation."""
        self.curr.execute(
            ''' SELECT * FROM add_services WHERE occupation=%s''', (occupation,))
        service = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return service

    def get_service_by_id(self, service_id):
        """Fetch a single service by ID."""

        self.curr.execute(""" SELECT * FROM add_services WHERE service_id={}""".format(service_id))
        service = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(service, default=str)

    def get_service_by_location(self, occupation, location):
        """Get a service by location."""
        self.curr.execute(
            ''' SELECT * FROM add_services WHERE occupation=%s and location=%s''', (occupation, location))
        service = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return service

    def delete(self, service_id):
        ''' Delete service by ID.'''

        self.curr.execute(''' DELETE FROM add_services WHERE service_id=%s''', (service_id,))
        self.conn.commit()
        self.curr.close()
