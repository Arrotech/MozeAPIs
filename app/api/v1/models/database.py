import os

import psycopg2
from psycopg2.extras import RealDictCursor


class Database:
    """Initialization."""

    def __init__(self):
        self.db_name = os.getenv('DB_NAME')
        self.db_host = os.getenv('DB_HOST')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.conn = psycopg2.connect(
            database=self.db_name, host=self.db_host, user=self.db_user, password=self.db_password)
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)

    def create_table(self):
        """Create tables."""
        queries = [
            """
            CREATE TABLE IF NOT EXISTS users(
                user_id serial PRIMARY KEY,
                firstname varchar NOT NULL,
                lastname varchar NOT NULL,
                phone varchar NOT NULL,
                username varchar NOT NULL,
                email varchar NOT NULL,
                password varchar NOT NULL,
                date TIMESTAMP
            )""",
            """
            CREATE TABLE IF NOT EXISTS add_services(
                service_id serial UNIQUE,
                name varchar NOT NULL,
                business_name varchar NOT NULL,
                portfolio varchar NOT NULL,
                occupation varchar NOT NULL,
                social_link varchar NOT NULL,
                description varchar NOT NULL,
                phone varchar NOT NULL,
                location varchar NOT NULL,
                working_hours varchar NOT NULL,
                cost varchar NOT NULL
            )"""
        ]
        try:
            for query in queries:
                self.curr.execute(query)
            self.conn.commit()
            self.curr.close()
        except Exception as e:
            return e

    def fetch(self, query):
        """Manipulate query."""
        self.curr.execute(query)
        fetch_all = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return fetch_all

    def destroy_table(self):
        """Destroy tables"""
        users = "DROP TABLE IF EXISTS  users CASCADE"
        add_services = "DROP TABLE IF EXISTS  add_services CASCADE"
        queries = [users, add_services]
        try:
            for query in queries:
                self.curr.execute(query)
            self.conn.commit()
            self.curr.close()
        except Exception as e:
            return e

if __name__ == '__main__':
    Database().destroy_table()
    Database().create_table()
