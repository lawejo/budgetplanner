import psycopg2
from config import config

def connect():
    connection = None
    params = config()
    print('Connecting to the postgreSQL database...')
    connection = psycopg2.connect(**params)

    crsr = connection.cursor()
    
