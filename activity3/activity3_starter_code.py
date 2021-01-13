import requests
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
db = SQLAlchemy(app)

class WeatherModel(db.Model):
    name = db.Column(db.String(30), primary_key=True)

db.create_all()

class weather(Resource):
    def get(self):
        cities = WeatherModel.query.all()
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID="

        pass

class weather_upload(Resource):
    def post(self, name):

        return 

api.add_resource(weather, '/weather')
api.add_resource(weather_upload, '/weather/<string:name>')

if __name__ == "__main__":
    app.run(debug=True)

