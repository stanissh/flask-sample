""" Installation """

from setuptools import find_packages, setup

setup(
    name="sample",
    description="Sample API application",
    license="BSD",
    maintainer="Stas Shevyakov",
    maintainer_email="stas.shevyakov@gmail.com",
    packages=find_packages(),
    install_requires=[
        "flask",
        "python-dotenv",
        "flask-pymongo"
    ],
)
