"""Helpers."""

import collections
import csv

def update_dict(orgdict, newdict):
    """Recursively update dictionary.
    """

    for key, val in newdict.items():
        if isinstance(val, collections.Mapping):
            orgdict[key] = update_dict(orgdict.get(key, {}), val)
        else:
            orgdict[key] = val

    return orgdict

def csv2tree(filepath):
    """load csv data by file name into database.

    Example of resulting tree:
    http://localhost:5000/csv/data (port :5050 for docker-compose)
    """

    resource = open(filepath, newline='')
    reader = csv.reader(resource)

    def create_dict(row: list, titles: list, pos=0):
        """Create nested dict by input list recursively.
        """

        data = {}
        if len(row) > 1:
            value = row[0]
            child = create_dict(row[1:], titles, pos + 1)
            # Key of the dict is a value of first list element.
            data[value] = {"tag": titles[pos]}
            if len(row) > 2:
                # If length of given row more then 2
                # value of the dict is another dict built from the
                # next elements of list recursively.
                data[value]["_items"] = child
            else:
                # If length of given row is equel "1" then we deal with "list" of the tree.
                # Set up "list" as description of the "node".
                data[value]["desc"] = child
        else:
            return row[0]

        return data

    titles = list()
    tree = dict()
    for i, row in enumerate(reader):
        if i == 0:
            titles = {item: item for item in row}
        else:
            tree = update_dict(tree, create_dict(row, list(titles.keys())))

    return {"header": titles, "body": tree}
