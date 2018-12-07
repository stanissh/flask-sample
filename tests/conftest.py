""" Testing fixtures and configuration. """

import os
import pytest
from dotenv import load_dotenv
from sample import create_app
from sample.commands import import_data

load_dotenv()

@pytest.fixture
def app():
    """ Create and app instance for each test """

    db_test = os.getenv("DB_TEST")

    _app = create_app({"MONGO_URI": db_test})
    _app.testing = True

    with _app.app_context():
        import_data("data.csv")

    return _app

@pytest.fixture
def client(app):
    """ A test client for the app """

    return app.test_client()
