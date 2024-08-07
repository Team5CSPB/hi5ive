# db.py

import psycopg2
from configparser import ConfigParser

def config(filename='config.ini', section='database'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db

def get_db():
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        print("Database connection established.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error connecting to database: {error}")
    
    return connection

def fetch_interest_id(interest_name):
    conn = get_db()
    if conn is None:
        print("Connection not established.")
        return None

    try:
        cur = conn.cursor()
        cur.execute("SELECT id FROM interests WHERE name = %s", (interest_name,))
        interest_id = cur.fetchone()
        cur.close()
        if interest_id:
            print(f"Found interest ID: {interest_id[0]}")
            return interest_id[0]
        else:
            print(f"Interest '{interest_name}' not found.")
            return None
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error fetching interest ID: {error}")
        return None
    finally:
        conn.close()
