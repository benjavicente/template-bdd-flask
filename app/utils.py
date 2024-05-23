from flask import g
import psycopg
from os import environ

def get_db() -> psycopg.Connection:
    if 'db' in g and isinstance(g.db, psycopg.Connection):
        return g.db
    g.db = psycopg.connect(environ['DATABASE_URL'])
    return g.db

def get_cursor() -> psycopg.Cursor:
    return get_db().cursor()
