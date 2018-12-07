""" Application databse package. """

from flask import current_app, g
from flask_pymongo import PyMongo

def get_db():
    """ Get database instance.
    """

    if 'mongo' not in g:
        g.mongo = PyMongo(current_app)

    return g.mongo.db
