from flask import Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

class Weather(Resource):
    # TODO Using the Open Weather API, create your own app to retrieve temperature and weather descriptions of a particular city
    def get(self):
        link = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="
        r = requests.get(link.format("Singapore")).json()
        weather = {
            "Temp": r["main"]["temp"],
            "Weather": r["weather"][0]["main"],
            "Description": r["weather"][0]["description"]
        }
        return weather

api.add_resource(Weather, '/weather')

if __name__ == '__main__':
    app.run(debug=True)