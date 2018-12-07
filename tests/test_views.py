""" Tests for views package. """

import json
from flask import url_for
from sample.database import get_db

def test_index(client):
    """ Test main page is alive.
    """

    assert client.get('/').status_code == 200

def test_definitions(client, app):
    """ Test main page is alive.
    """

    with app.app_context():
        category = get_db().categories.find_one({})
        assert_definition(client, app, category)

def assert_definition(client, app, category):
    """ Test first definition is STANDARD.
    """
    
    with app.test_request_context():
        response = client.get(url_for("views.definitions", category=str(category["_id"])))
        data = json.loads(response.data)
        assert data["name"] == "STANDARD"
