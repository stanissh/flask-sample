""" Console commands """

import click
from flask.cli import with_appcontext
from .utils import csv2tree
from .database import get_db

def import_data(filename):
    """ Load csv data by file name into database.
    """

    def save(data, category_id, pid=None):
        """ Recursively save data as a tree in database.
        """

        for name, val in data.items():
            _data = {
                "tag": val["tag"],
                "name": name,
                "desc": val.get("desc"),
                "pid": pid,
                "category_id": category_id
            }
            pid = get_db().definitions.insert_one(_data).inserted_id

            if "_items" in val:
                for i, item in val["_items"].items():
                    save({i: item}, category_id, pid)

    data = csv2tree("data/" + filename)
    # Separate category for each definition set for scalability
    category = {"name": "Initial category", "data": data["header"]}
    category_id = get_db().categories.insert_one(category).inserted_id
    save(data["body"], category_id)


@click.command()
@click.argument("filename")
@with_appcontext
def load(filename):
    """ Load csv data by file name into database.

    Example: flask load data.csv.
    """

    import_data(filename)
