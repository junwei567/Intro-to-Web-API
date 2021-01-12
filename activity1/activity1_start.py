from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
# parser.add_argument("", type=, help="", required=)

class HelloWorld(Resource):
    def get(self):
        return {"Hello": "World"}

def not_found():
    # if the entry is not found
    pass

def dupe_entry():
    # if entry already exists
    pass

class Basics(Resource):
    def get(self, name):
        return 

    def post(self, name):
        return 

    def put(self, name):
        return 

    def delete(self,name):
        return 

api.add_resource(HelloWorld, '/')
api.add_resource(Basics, '/basic/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)