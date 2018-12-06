""" Helpers """

import collections
import csv

def update_dict(orgdict, newdict):
    """ Recursively update dictionary
    """

    for key, val in newdict.items():
        if isinstance(val, collections.Mapping):
            orgdict[key] = update_dict(orgdict.get(key, {}), val)
        else:
            orgdict[key] = val

    return orgdict

def csv2tree(filepath):
    """ load csv data by file name into database
    """

    resource = open(filepath, newline='')
    reader = csv.reader(resource)

    def create_dict(row, titles: list, pos=0):
        """ Creates tree by input list recursively
        """

        data = {}
        if len(row) > 1:
            value = row[0]
            child = create_dict(row[1:], titles, pos + 1)
            data[value] = {"tag": titles[pos]}
            if len(row) > 2:
                data[value]["_items"] = child
            else:
                data[value]["desc"] = child
        else:
            return row[0]

        return data

    titles = list()
    data = dict()
    for i, row in enumerate(reader):
        if i == 0:
            titles = {item: item for item in row}
        else:
            data = update_dict(data, create_dict(row, list(titles.keys())))

    return {"header": titles, "body": data}
