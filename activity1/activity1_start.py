from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
'''
TODO 1: Declare arguments to be used in your request parser
Eg. parser.add_argument("", type=, help="", required=)
'''

class HelloWorld(Resource):
    def get(self):
        return {"Hello": "World"}

def not_found(name):
    '''
    TODO 2: Create function to check if entry is not found in database
    Call abort with 2 arguments, error code and message to display
    '''
    pass

def dupe_entry(name):
    '''
    TODO 3: Create function to check if entry already exists in database
    Call abort with 2 arguments, error code and message to display
    '''
    pass

class Basics(Resource):
    '''
    TODO 4: Fill in the 4 HTTP methods, GET, POST, PUT and DELETE
    Each method should return a tuple, 1st Arg is the Data, 2nd Arg is the Status Code (200, 201, ...)
    '''
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