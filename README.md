Introduction to Web API with Python and Flask
===

## Table of Contents

[TOC]

## Making a request to an API

We will be using the Astronomy Picture of the Day API by NASA

### Method 1 

1. Open up your preferred modern browser
2. Paste `https://api.nasa.gov/planetary/apod?api_key=pNYC2hpSuDjKQ9IhbKszZ5IctGbGjuTe91oTohlS`

### Method 2

1. Open up your terminal
2. Paste 
```gherkin
$ curl --request GET \
       --url 'https://api.nasa.gov/planetary/apod?api_key=pNYC2hpSuDjKQ9IhbKszZ5IctGbGjuTe91oTohlS' \
       --header 'Accept: application/json'
```

## Flask RESTful

Install dependencies
```python
pip install flask flask_restful flask_sqlalchemy
pip install requests
```

Your First API
```python
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
```

## SQLite
To check your sqlite database, you can use the following commands in your terminal.

1. To launch the database service: `sqlite3 weather.db`
2. To list the available tables: `.table`

A list of fundamental SQL query

1. To list the entries inside the table: `SELECT * FROM weather_model;`
2. To insert an entry into the table: 
`INSERT INTO (column1, column2, ..) VALUES (value1, value2, ..);`
3. To update an entry: 
`UPDATE table
SET column_1 = new_value_1,
    column_2 = new_value_2
WHERE search_condition;`
4. To delete an entry: `DELETE FROM table
WHERE search_condition;`

## Author
Jun Wei