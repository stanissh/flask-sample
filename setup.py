"""Installation."""

from setuptools import find_packages, setup

setup(
    name="sample",
    description="Sample API application",
    version="0.0.1",
    author="Stas Shevyakov",
    author_email="stas.shevyakov@gmail.com",
    maintainer="Stas Shevyakov",
    maintainer_email="stas.shevyakov@gmail.com",
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "sample": ['templates/*.html', 'templates/**/*.html']
    },
    install_requires=[
        "flask",
        "python-dotenv",
        "flask-pymongo"
    ],
    extras_require={
        "test": [
            "pytest",
        ],
    },
)
