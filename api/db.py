from flask import g, current_app
import os
import psycopg2
import configparser

def get_db():
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('config.ini')

    if 'db' not in g:
        g.db = psycopg2.connect(
            dbname=current_app.config['DATABASE']['dbname'],
            user=current_app.config['DATABASE']['user'],
            password=current_app.config['DATABASE']['password'],
            host=current_app.config['DATABASE']['host'],
            port=current_app.config['DATABASE']['port']
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

