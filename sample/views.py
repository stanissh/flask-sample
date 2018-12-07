""" Application routes """

from bson.objectid import ObjectId
from bson.json_util import dumps
from flask import Blueprint, jsonify, render_template
from sample.database import get_db
from sample.utils import csv2tree

blueprint = Blueprint('views', __name__)

@blueprint.route("/")
def index():
    """ Index page
    """

    cat = get_db().categories.find_one({})

    return render_template("index.html", category=cat)

@blueprint.route('/v1/category/<category>', defaults={"pid": None})
@blueprint.route('/v1/category/<category>/items/<pid>')
def definitions(category, pid):
    """ Shows definitions
    """

    # Category titles
    cdata = get_db().categories.find_one_or_404({"_id": ObjectId(category)})["data"]
    filters = {"category_id": ObjectId(category)}

    if pid:
        filters["pid"] = ObjectId(pid)
    else:
        filters["pid"] = pid

    items = get_db().definitions.find(filters)
    data = {"id": None, "name": None, "definitions": []}

    for i in items:
        if not data["id"]:
            data["id"] = i["tag"]
            data["name"] = cdata[i["tag"]]
        tmp = dict(id=str(i["_id"]), name=i["name"], cat=category)
        if i["desc"]:
            tmp["desc"] = i["desc"]
        data["definitions"].append(tmp)

    return dumps(data)

@blueprint.route('/csv/<filename>')
def show_csv(filename):
    """ Shows csv as a tree
    """

    data = csv2tree("data/%s.csv" % filename)
    return jsonify(data)
