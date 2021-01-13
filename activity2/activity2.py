from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

class Weather(Resource):
    def get(self):
        link = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="
        r = requests.get(link.format("Singapore")).json()

        weather = {
            'city': r['name'],
            'description': r['weather'],
            'temperature': r['main']['temp']
        }

        return weather

api.add_resource(Weather, '/weather')

if __name__ == '__main__':
    app.run(debug=True)