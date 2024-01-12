import sqlite3
from flask import g
import json

DATABASE = './datastore.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = make_dicts
    return db

def make_dicts(cursor, row):
    return dict(processColumn(cursor.description[index][0], value) 
                for index, value in enumerate(row))

def processColumn(key, value):
  return (key, value if key != 'attributes' else json.loads(value))