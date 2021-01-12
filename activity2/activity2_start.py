from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

class Weather(Resource):
    def get(self):
        
        return 

api.add_resource(Weather, '/weather')

if __name__ == '__main__':
    app.run(debug=True)