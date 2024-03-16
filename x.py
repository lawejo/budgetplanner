import os
from dotenv import find_dotenv, load_dotenv
import psycopg2
import psycopg2.extras
from config import config

##############################
## Load env
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
connection_string = os.getenv('DATABASE_URL')

##############################
## Load database
def database_connection():
    connection = None
    try:
        
        params = config()
        print('Connecting to the postgreSQL database ...')
        connection = psycopg2.connect(connection_string)
        # connection = psycopg2.connect(**params)
        return connection
    except(Exception, psycopg2.DatabaseError) as e:
        print(e)
 
        

def database_query(query, is_modification):
    try:
        connection = database_connection()
        cur = connection.cursor()
        cur.execute(query)
        ## If the query is a modification there is no result i.e == None 
        result = cur.fetchall() if not is_modification else None
        if is_modification==True:
            connection.commit()

        connection.close() 
        return result
    except Exception as e:
        print(e.args[1])
        if connection is not None and is_modification:
            connection.rollback()
        raise 
   