""" Tests for utils package """

from sample.utils import csv2tree

def test_csv2tree():
    """ Test built tree is correct"""

    data = csv2tree("data/data.csv")
    assert isinstance(data, dict)
    assert "header" in data
    assert "body" in data
