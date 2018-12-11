# Simple Flask application

Tools:

-	Flask
-	MongoDB
-	ReactJS

## Installation:

Create .env file with configuration options:

```bash
DB=mongodb://{MONGO_HOST}/{DATABASE_NAME}
DB_TEST=mongodb://{MONGO_HOST}/{TEST_DATABASE_NAME}
````

Install dependencies:

	$ pip install -e .

Or using Pipenv:

	$ pipenv install

## Run

Load data from csv into database:

	$ flask load data.csv

Run server:

	$ flask run

## Docker

Simply run:

	$ docker-compose up

	