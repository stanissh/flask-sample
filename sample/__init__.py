""" Main application package """

import os
from flask import Flask
from dotenv import load_dotenv
from .views import blueprint
from .commands import load

load_dotenv()

def create_app(config=None):
    """ Application factory
    """

    app = Flask(__name__, instance_relative_config=True)
    app.static_folder += "/public"
    app.config["MONGO_URI"] = os.environ.get('DB')

    if config is not None:
        app.config.update(config)

    app.register_blueprint(blueprint)
    app.cli.add_command(load)

    return app
