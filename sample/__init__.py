""" Main application package """

import os
from flask import Flask, g
from sample.views import blueprint
from sample.commands import load

def create_app():
    """ Application factory
    """

    app = Flask(__name__)
    app.static_folder += "/public"
    app.config["MONGO_URI"] = os.environ.get('DB')

    app.register_blueprint(blueprint)
    app.cli.add_command(load)

    return app
