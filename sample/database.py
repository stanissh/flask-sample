"""Application databse package."""

from flask import current_app, g
from flask_pymongo import PyMongo

def get_db():
    """Singleton method for retrieving database instance.
    """

    if 'mongo' not in g:
        g.mongo = PyMongo(current_app)

    return g.mongo.db
