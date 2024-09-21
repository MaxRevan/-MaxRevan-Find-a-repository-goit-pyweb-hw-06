import psycopg2
from contextlib import contextmanager


@contextmanager
def create_connection():
    """ create a database connection to a Postgres database """
    try:
        conn = psycopg2.connect(host='localhost', database='univer', user='postgres', password='12345')
        yield conn
        conn.close()
    except psycopg2.OperationalError as err:
        raise RuntimeError(f"Failed to connect to the database: {err}")